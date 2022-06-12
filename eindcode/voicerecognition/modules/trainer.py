import torch.nn.functional as F
import torch
import torch.optim as optim
from modules.resampler import Resampler
from modules.subsetSC import SubsetSC
import tqdm

class Trainer:
    def __init__(self, model, train_set, test_set, resampler, batch_size = 2048, device="cpu"):
        self.device = device
        self.model = model        
        self.losses = []
        self.batch_size = batch_size
        self.train_set = train_set
        self.test_set = test_set
        self.resampler = resampler
        self.transform = resampler.transform.to(device)

        if device == "cuda":
            num_workers = 1
            pin_memory = True
            print("cuda working")
        else:
            num_workers = 0
            pin_memory = False
            print("cpu working")

        self.train_loader = torch.utils.data.DataLoader(
            self.train_set,
            batch_size=batch_size,
            shuffle=True,
            collate_fn=self.collate_fn,
            num_workers=num_workers,
            pin_memory=pin_memory,
        )
        self.test_loader = torch.utils.data.DataLoader(
            self.test_set,
            batch_size=batch_size,
            shuffle=False,
            drop_last=False,
            collate_fn=self.collate_fn,
            num_workers=num_workers,
            pin_memory=pin_memory,
        )

        self.pbar_update = 1 / (len(self.train_loader) + len(self.test_loader))


    def train(self, model, pbar):
        optimizer = optim.Adam(model.parameters(), lr=0.01, weight_decay=0.0001)
        scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=20, gamma=0.1)  # reduce the learning after 20 epochs by a factor of 10

        model.train()
        for batch_idx, (data, target) in enumerate(self.train_loader):

            data = data.to(self.device)
            target = target.to(self.device)

            # apply transform and model on whole batch directly on device
            data = self.transform(data)
            # print(data.size())
            output = model(data)

            # negative log-likelihood for a tensor of size (batch x 1 x n_output)
            loss = F.nll_loss(output.squeeze(), target)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            scheduler.step()

            # print training stats
            # if batch_idx % log_interval == 0:
            #     print(f"Train Epoch: {epoch} [{batch_idx * len(data)}/{len(self.train_loader.dataset)} ({100. * batch_idx / len(self.train_loader):.0f}%)]\tLoss: {loss.item():.6f}")

            # update progress bar
            pbar.update(self.pbar_update)
            # record loss
            self.losses.append(loss.item())


    def collate_fn(self, batch):

        tensors, targets = [], []

        # Gather in lists, and encode labels
        for waveform, _, label, *_ in batch:
            tensors += [waveform]
            targets += [self.resampler.label_to_index(label)]

        # Group the list of tensors into a batched tensor
        tensors = self.pad_sequence(tensors)
        targets = torch.stack(targets)

        return tensors, targets

    def test(self, model, epoch, pbar):
        model.eval()
        correct = 0
        for data, target in self.test_loader:

            data = data.to(self.device)
            target = target.to(self.device)

            # apply transform and model on whole batch directly on device
            data = self.transform(data)
            output = model(data)

            pred = self.get_likely_index(output)
            correct += self.number_of_correct(pred, target)

            # update progress bar
            pbar.update(self.pbar_update)

        print(f"\nTest Epoch: {epoch}\tAccuracy: {correct}/{len(self.test_loader.dataset)} ({100. * correct / len(self.test_loader.dataset):.0f}%)\n")


    def pad_sequence(self, batch):
        # Make all tensor in a batch the same length by padding with zeros
        batch = [item.t() for item in batch]
        batch = torch.nn.utils.rnn.pad_sequence(batch, batch_first=True, padding_value=0.)
        return batch.permute(0, 2, 1)


    def number_of_correct(self, pred, target):
        # count number of correct predictions
        return pred.squeeze().eq(target).sum().item()


    def get_likely_index(self, tensor):  # convert math to numbers in tensor
        # find most likely label index for each element in the batch
        return tensor.argmax(dim=-1)