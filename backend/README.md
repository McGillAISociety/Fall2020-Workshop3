# mais-flask-workshop-2019

The goal of this project is to demonstrate a simple example of how to integrate different machine learning models into real-life applications. To achieve this goal, this repository holds the source code for a flask application allowing users to upload images and evaluate the image to predict the handwritten digit. This application also uses the pre-trained model for GPT2 to generate text given a starting prompt.

This project is to be used for introductory workshops aimed at teaching the basics of integrating ML into a Flask App.

## Prerequisites

Install necessary python packages

`pip install -r requirements.txt`

## Running the Flask Application 

Run the **app.py** file from the **root** directory. 

`python app.py` 

Go to **localhost:5000** to access the application from the browser of your choice.

## Structure of the repository

```
├── README.md
├── app.py                      # Main code to run the flask app
├── gpt2_predictor.py           # Contains the predictor class for GPT2
├── mnist_predictor.py          # Contains the predictor class for MNIST
├── model
│   ├── model.py                # Contains the code for the mnist model
│   ├── nn.py                   # contains the code for the neural net
│   └── results
│       └── model.pth           # Weights of the trained mnist model
├── notebooks
│   └── pre_trained_gpt2.ipynb  # Notebook used to explore GPT2
├── requirements.txt            # File containing packages needed to run the code
├── static
│   ├── css
│   │   └── main.css            # Style sheet to make the front-end prettier
│   └── js
│       └── main.js             # Javascript file handling front-end actions
└── templates
    └── index.html              # HTML file that Flask renders
```

