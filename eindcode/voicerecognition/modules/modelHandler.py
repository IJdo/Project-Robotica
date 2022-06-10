import torch
from os.path import abspath

class ModelHandler:
    def save_model(self, model, target_filename, target_path = abspath(".")):
        torch.save(model, target_path + "/" + target_filename)

    def load_model(self, source_filename, source_path = abspath(".")):
        model = torch.load(source_path + "/" + source_filename)
        model.eval()  # assume that the loaded model will be used for production purposes when it's loaded
        return model