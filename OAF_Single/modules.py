import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
import torchvision.transforms as transforms
import mpm


class imgdataset(Dataset):
    def __init__(self, x, y=None, transform=None):
        self.x = x
        self.y = y
        self.transform = transform

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        X = self.x[index]
        if self.y is not None:
            Y = self.y[index]
        if self.transform is not None:
            X = self.transform(X)
            if self.y is not None:
                Y = self.transform(Y)

        if self.y is not None:
            return X, Y
        else:
            return X


class Denoise_conv(nn.Module):
    def __init__(self):
        super(Denoise_conv, self).__init__()
        self.cnn = nn.Sequential(
            #torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)
            nn.Conv2d(1, 64, 3, 1, 1),
            nn.ReLU(),
            mpm.StripPooling(64, (12, 20), nn.BatchNorm2d, {
                "mode": "bilinear"}),
            nn.Conv2d(64, 64, 3, 1, 1),
            nn.ReLU(),
            # customize.StripPooling(64,(12,20),nn.BatchNorm2d,{"mode":"bilinear"}),
            nn.Conv2d(64, 64, 3, 1, 1),
            nn.ReLU(),
            mpm.StripPooling(64, (12, 20), nn.BatchNorm2d, {
                "mode": "bilinear"}),
            nn.Conv2d(64, 64, 3, 1, 1),
            nn.ReLU(),
            mpm.StripPooling(64, (12, 20), nn.BatchNorm2d, {
                "mode": "bilinear"}),
            nn.Conv2d(64, 1, 3, 1, 1),
            nn.ReLU(),
            # customize.StripPooling(64,(12,20),nn.BatchNorm2d,{mode:"bilinear"})
        )

    def forward(self, x):
        out = self.cnn(x)
        return out
