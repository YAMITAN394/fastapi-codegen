import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
txt_model_name = "facebook/opt-1.3b"