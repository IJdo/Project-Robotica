import torchaudio
import IPython.display as ipd
import torch

class Resampler:
    def __init__(self, labels, sample_rate=16000, new_sample_rate=8000, word_start="right"):
        self.sample_rate = sample_rate
        self.new_sample_rate = new_sample_rate
        self.transform = torchaudio.transforms.Resample(orig_freq=self.sample_rate, new_freq=self.new_sample_rate)
        self.labels = labels
        self.word_start = word_start


    # def transform(self, waveform):
    #     return self.transform(waveform)


    def audioTransform(self, waveform):
        return ipd.Audio(self.transform(waveform).numpy(), rate=self.new_sample_rate)


    def label_to_index(self, word):
        # Return the position of the word in labels
        return torch.tensor(self.labels.index(word))


    def index_to_label(self, index):
        # Return the word corresponding to the index in labels
        # This is the inverse of label_to_index
        return self.labels[index]


    # word_start = "right"
    # index = label_to_index(word_start)
    # word_recovered = index_to_label(index)

    # print(word_start, "-->", index, "-->", word_recovered)