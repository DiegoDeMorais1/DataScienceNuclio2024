"""Feed Forward Neural Network in PyTorch."""
from typing import Any

import torch.nn as nn


class NeuralNet(nn.Module):
    """Main neural network."""

    def __init__(
        self, input_size: int = 784, hidden_size: int = 100, num_classes: int = 10
    ) -> None:
        """Initialize the neural network."""
        super(NeuralNet, self).__init__()
        self.input = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(hidden_size, hidden_size)
        self.output = nn.Linear(hidden_size, num_classes)

    def forward(self, x: Any) -> Any:
        """Forward pass."""
        x = self.input(x)
        x = self.relu(x)
        x = self.fc(x)
        x = self.relu(x)
        x = self.output(x)
        return nn.LogSoftmax(dim=1)(x)
