import torch

has_cuda=torch.cuda.is_available()
default_device="cuda" if has_cuda else "cpu"
