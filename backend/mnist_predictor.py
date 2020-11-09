from model.model import MNISTModel
from PIL import Image
import matplotlib
import torch
import torchvision.transforms.functional as TF

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np

size = (28, 28)


def preprocess_img(image):
    """
    This method processes the image into the correct expected shape in the model (28, 28).
    """
    if (image.mode == 'RGB'):
        # Convert RGB to grayscale.
        image = image.convert('L')
    image = image.resize(size)
    return image


def image_loader(image):
    """
    This method loads the image into a PyTorch tensor.
    """
    image = TF.to_tensor(image)
    image = image.unsqueeze(0)
    return image


class MNIST_predictor:
    def __init__(self):
        self.model = MNISTModel()
        self.model.net.load_state_dict(torch.load('model/results/model.pth'))

    def predict(self, request):
        """
        This method reads the file uploaded from the Flask application POST request,
        and performs a prediction using the MNIST model.
        """
        f = request.files['image']
        image = Image.open(f)
        image = preprocess_img(image)
        image = image_loader(image)
        model_output = self.model.net(image)
        prediction = torch.argmax(model_output)
        return prediction.item()
