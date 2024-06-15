"""Download data and load data."""
from typing import Any

import torch
import torchvision
import torchvision.transforms as transforms


def download_data() -> tuple[Any, Any]:
    """Get data from the internet."""
    # MNIST dataset
    train_dataset = torchvision.datasets.MNIST(
        root="../data", train=True, transform=transforms.ToTensor(), download=True
    )

    test_dataset = torchvision.datasets.MNIST(
        root="../../data", train=False, transform=transforms.ToTensor(), download=True
    )

    return train_dataset, test_dataset


def get_data_loader(
    train_dataset: tuple[Any], test_dataset: tuple[Any], batch_size: int = 128
) -> tuple[Any, Any]:
    """Get data loader."""
    train_loader = torch.utils.data.DataLoader(
        dataset=train_dataset, batch_size=batch_size, shuffle=True
    )

    test_loader = torch.utils.data.DataLoader(
        dataset=test_dataset, batch_size=batch_size, shuffle=False
    )

    return train_loader, test_loader
