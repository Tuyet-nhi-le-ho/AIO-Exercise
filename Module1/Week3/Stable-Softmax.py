import torch
import torch.nn as nn


class StablestSoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True)
        x_exp = torch.exp(x - x_max.values)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


data = torch.tensor([1.0, 2.0, 3.])
stable_softmax = StablestSoftmax()
output = stable_softmax(data)
print(output)
