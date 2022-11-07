import torch
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

from torch.utils.data import Dataset, DataLoader
from torch import nn
from torch.nn import functional as F

# Load the data
data = load_breast_cancer()
x = data['data']
y = data['target']
print("shape of x: {}\nshape of y: {}".format(x.shape, y.shape))

# Scale features
sc = StandardScaler()
x = sc.fit_transform(x)


class dataset(Dataset):
    """ Torch Dataset loaders allows applying shuffling,
        mini-batch etc.
    """

    def __init__(self, x, y):

        self.x = torch.tensor(x, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.float32)
        self.length = self.x.shape[0]

    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]

    def __len__(self):
        return self.length


class NeuralNet(nn.Module):

    def __init__(self, input_shape):
        super(NeuralNet, self).__init__()
        self.fc1 = nn.Linear(input_shape, 32)
        self.fc2 = nn.Linear(32, 64)
        self.fc3 = nn.Linear(64, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.sigmoid(self.fc3(x))
        return x


trainset = dataset(x, y)
trainloader = DataLoader(trainset, batch_size=64, shuffle=False)

# Network parameters
learning_rate = 0.01
epochs = 700
model = NeuralNet(input_shape=x.shape[1])
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)
loss_fn = nn.BCELoss()

# Training loop
losses = []
accur = []
for i in range(epochs):
    for j, (x_train, y_train) in enumerate(trainloader):
        # Network predictions
        preds = model(x_train)
        loss = loss_fn(preds, y_train.reshape(-1, 1))

        # Accuracy
        predicted = model(torch.tensor(x, dtype=torch.float32))
        acc = (predicted.reshape(-1).detach().numpy().round() == y).mean()

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    if i % 50 == 0:
        losses.append(loss.detach().numpy())
        accur.append(acc)
        print("epoch {}\tloss : {}\t accuracy : {}".format(i, loss, acc))

plt.plot(losses)
plt.title('Loss vs Epochs')
plt.xlabel('Epochs')
plt.ylabel('loss')

plt.show()

plt.plot(accur)
plt.title('Accuracy vs Epochs')
plt.xlabel('Accuracy')
plt.ylabel('loss')

plt.show()