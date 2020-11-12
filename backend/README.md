## Running the Flask Application 

Run the **app.py** file from the **root** directory. 

`python app.py` 

Go to **localhost:5000** to access the application from the browser of your choice.

## Structure of the folder

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

