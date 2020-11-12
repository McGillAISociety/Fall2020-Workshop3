# McGill AI Workshop 3

This workshop will cover the basics on:
- Creating a flask backend with a pytorch model
- Creating REST endpoints in flask for clients to call
- Create a reactjs frontend
- Having the frontend call the backend for predictions

## Slides
The slides for this workshop can be found [here](https://docs.google.com/presentation/d/1DkIez0tmL58wIh1P7Dr2Zb8r_wzbQIvlgxgOjs9U5HU/edit?usp=sharing)

## Backend

The backend is written in Flask and requires a Python version of 3.8+

We provide below 3 different ways of installing the needed dependencies to run the Flask app. Please run the following commands from within the backend folder

- Using pip:
```
pip install -r requirements.txt
```

- Using Pipenv:
```
pip install pipenv
pipenv shell
pipenv install
```

- Using Conda: 
```
conda env create -f environment.yml
```
For more info about creating and managing Conda environments, please refer to this [link](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)

## Frontend

Instantiate the frontend using the following command
```
npm init react-app frontend
```
