import os
from torchaudio.datasets import SPEECHCOMMANDS
import tqdm

# def _load_list(filename):
#     filepath = os.path.join(self._path, filename)
#     with open(filepath) as fileobj:
#         return [os.path.normpath(os.path.join(self._path, line.strip())) for line in tqdm(fileobj)]



class SubsetSC(SPEECHCOMMANDS):
    def __init__(self, subset: str = None):
        super().__init__("./", download=True)        

        def load_list(filename):
            filepath = os.path.join(self._path, filename)
            num_lines = sum(1 for line in open(filepath, 'r'))
            with open(filepath) as fileobj:
                mylist = []
                for line in tqdm.tqdm(fileobj, total=num_lines):
                    mylist.append(os.path.normpath(os.path.join(self._path, line.strip())))
                return mylist
                # return [os.path.normpath(os.path.join(self._path, line.strip())) for line in fileobj]

        if subset == "validation":
            self._walker = load_list("validation_list.txt")
        elif subset == "testing":
            self._walker = load_list("testing_list.txt")
        elif subset == "training":
            excludes = load_list("validation_list.txt") + load_list("testing_list.txt")
            excludes = set(excludes)
            self._walker = [w for w in self._walker if w not in excludes]