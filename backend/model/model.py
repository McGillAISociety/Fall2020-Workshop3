from .nn import Net

import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import os
import torch
import torchvision
import torch.optim as optim
import torch.nn.functional as F
import torchvision.transforms.functional as TF

# Look to the path of your current working directory
save_model_path = './model/results/model.pth'
save_optimizer_path = './model/results/optimizer.pth'

size = (28, 28)


def load_data(batch_size_train=64, batch_size_test=1000):
    '''
    This method loads the MNIST dataset from Pytorch. It takes care of the normalization
    and pretraining transformation.
    '''

    train_loader = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST('../data', train=True, download=True,
                                   transform=torchvision.transforms.Compose([
                                       torchvision.transforms.ToTensor(),
                                       torchvision.transforms.Normalize(
                                           (0.1307,), (0.3081,))
                                   ])),
        batch_size=batch_size_train, shuffle=True)

    test_loader = torch.utils.data.DataLoader(
        torchvision.datasets.MNIST('../data', train=False, download=True,
                                   transform=torchvision.transforms.Compose([
                                       torchvision.transforms.ToTensor(),
                                       torchvision.transforms.Normalize(
                                           (0.1307,), (0.3081,))
                                   ])),
        batch_size=batch_size_test, shuffle=True)

    return train_loader, test_loader


class MNISTModel:
    def __init__(self, learning_rate=0.01, momentum=0.5):
        self.net = Net()
        self.optimizer = optim.SGD(self.net.parameters(), lr=learning_rate, momentum=momentum)

    def train_model(self, train_data, test_data, n_epochs=3, log_interval=100):
        '''
        This method trains the model at a higher level. Calls train and test methods.
        '''

        for epoch in range(1, n_epochs + 1):
            model.train(train_data, epoch, log_interval)
            model.test(test_data)

    def train(self, train_data, epoch, log_interval):
        '''
        This method trains the neural network.
        The model is saved after each epoch in `./results/`
        '''
        self.net.train()
        for batch_idx, (data, target) in enumerate(train_data):
            self.optimizer.zero_grad()
            output = self.net(data)
            loss = F.nll_loss(output, target)
            loss.backward()
            self.optimizer.step()
            if batch_idx % log_interval == 0:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(train_data.dataset),
                           100. * batch_idx / len(train_data), loss.item()))
                torch.save(self.net.state_dict(), save_model_path)
                torch.save(self.optimizer.state_dict(), save_optimizer_path)

    def test(self, test_data):
        '''
        This method evaluates the train model and outputs the final accuracy results.
        '''
        self.net.eval()
        test_loss = 0
        correct = 0
        with torch.no_grad():
            for data, target in test_data:
                output = self.net(data)
                test_loss += F.nll_loss(output, target, size_average=False).item()
                pred = output.data.max(1, keepdim=True)[1]
                correct += pred.eq(target.data.view_as(pred)).sum()
        test_loss /= len(test_data.dataset)
        print('\nTest set: Avg. loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
            test_loss, correct, len(test_data.dataset),
            100. * correct / len(test_data.dataset)))


if __name__ == "__main__":
    model = MNISTModel()
    random_seed = 1
    torch.manual_seed(random_seed)

    # Load the data.
    train_loader, test_loader = load_data()

    # Train the model
    model.train_model(train_loader, test_loader, 6)
