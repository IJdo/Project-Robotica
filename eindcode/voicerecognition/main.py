sys.path.append(os.path.dirname(os.path.realpath(__file__)))

import os, sys
import torch
import torch.nn.functional as F
import torch.optim as optim
import torchaudio

from modules.record import Recorder
from modules.subsetSC import SubsetSC
from modules.trainer import Trainer
from modules.model import M5
from modules.resampler import Resampler
from modules.filehandling import *
import IPython.display as ipd

from tqdm import tqdm

# Check if Cuda GPU is available, print device to be used in training/testing
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

# Get subest of training data and testing data 
train_set = SubsetSC("training")       
test_set = SubsetSC("testing")

waveform, sample_rate, label, speaker_id, utterance_number = train_set[0]
labels = sorted(list(set(datapoint[2] for datapoint in train_set)))

# resample each label to 8KHz for faster learning
resampler = Resampler(labels)

# Used M5-algorithm with inputted resampled waveforms for learning
model = M5(n_input=resampler.transform(waveform).shape[0], n_output=len(labels))
model.to(device)
trainer = Trainer(model, train_set, test_set, resampler, device=device)
print(model)


def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)


n = count_parameters(model)
print("Number of parameters: %s" % n)


# Start with learning rate of 0.01, reduce to 0.001 after 20 epochs for detailed learning
optimizer = optim.Adam(model.parameters(), lr=0.01, weight_decay=0.0001)  # Same optimization technique as M5-algorithm from paper
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.1)  # reduce the learningrate after 20 epochs by a factor of 10


# Train settings
log_interval = 20
n_epoch = 50  # amount of epochs (learning cycles)

pbar_update = 1 / (len(trainer.train_loader) + len(trainer.test_loader))
losses = []

# The transform needs to live on the same device as the model and the data.
transform = resampler.transform.to(device)
with tqdm(total=n_epoch) as pbar:
    for epoch in range(1, n_epoch + 1):
        trainer.train(model, pbar)
        trainer.test(model, epoch, pbar)
        # scheduler.step()


def predict(tensor):
    # Use the model to predict the label of the waveform
    tensor = tensor.to(device)
    tensor = transform(tensor)
    tensor = model(tensor.unsqueeze(0))
    print(tensor)
    tensor = trainer.get_likely_index(tensor)
    print(tensor)
    tensor = resampler.index_to_label(tensor.squeeze())
    print(tensor)
    return tensor


waveform, sample_rate, utterance, *_ = trainer.train_set[-1]
ipd.Audio(waveform.numpy(), rate=sample_rate)

print(f"Expected: {utterance}. Predicted: {predict(waveform)}.")



# Let’s find an example that isn’t classified correctly, if there is one.
for i, (waveform, sample_rate, utterance, *_) in enumerate(trainer.test_set):
    output = predict(waveform)
    if output != utterance:
        ipd.Audio(waveform.numpy(), rate=sample_rate)
        print(f"Data point #{i}. Expected: {utterance}. Predicted: {output}.")
        break
else:
    print("All examples in this dataset were correctly classified!")
    ipd.Audio(waveform.numpy(), rate=sample_rate)
    print(f"Data point #{i}. Expected: {utterance}. Predicted: {output}.")


# Save learning model in .pt file
torch.save(model, "model.pt")
# model = ModelHandler.load_model("model.pt")  # reload and rewrite model.pt
model = torch.load("model.pt").to(device)
model.eval()  # assume that the loaded model will be used for production purposes when it's loaded
input("press enter")

# Record audio from microphone run once
Recorder.record()

# Get prediction 
waveform, sample_rate = torchaudio.load("output.wav")
print(f"Predicted: {predict(waveform)}.")

# Write predicted command to file
fileObj = File("temporalCommand", predict(waveform))
fileWriter = FileHandler.setFileContents(fileObj)
ipd.Audio(waveform.numpy(), rate=sample_rate)