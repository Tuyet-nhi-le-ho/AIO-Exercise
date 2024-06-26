import torch
import torch.nn as nn


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


data = torch.tensor([5., 2., 4.])
my_softmax = MySoftmax()
output = my_softmax(data)
print(output)
