import torch

from src.get_data import download_data, get_data_loader
from src.pytorch_ff import NeuralNet

EPOCHS = 2

train_dataset, test_dataset = download_data()

train_loader, test_loader = get_data_loader(train_dataset, test_dataset)

net = NeuralNet(input_size=784, hidden_size=100, num_classes=10)

torch.manual_seed(42)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

net.to(device)

optimzer = torch.optim.Adam(net.parameters(), lr=0.001)
loss_fn = torch.nn.NLLLoss()


for epoch in range(EPOCHS):
    net.train()
    for batch_idx, (data, target) in enumerate(train_loader):
        data = data.reshape(data.shape[0], 28 * 28).to(device)
        target = target.to(device)
        optimzer.zero_grad()
        output = net(data)
        loss = loss_fn(output, target)
        loss.backward()
        optimzer.step()
        print("\r", f"Epoch: {epoch}, Batch {batch_idx}, Loss: {loss.item():.4f}", end="\r")

    net.eval()
    test_loss = 0
    with torch.no_grad():
        for batch_idx, (data, target) in enumerate(test_loader):
            data = data.reshape(data.shape[0], 28 * 28).to(device)
            target = target.to(device)
            output = net(data)
            loss = loss_fn(output, target)
            test_loss += loss.item()

    print("\n", f"Epoch: {epoch}, Test Loss: {test_loss/batch_idx}")

torch.save(net, "pytorch_ff.pt")
