# Movie Genere Classification

## Demo
Link: [https://movie-genre-classification.herokuapp.com](https://movie-genre-classification.herokuapp.com/)

## Overview
This is a simple movie genere classification and scraping website built on django and the trained model takes text as input and predicts the genre.

## Technical Aspect
This project is divided into two part:
1. Training a machine learning model and create a web application
2. Building and hosting a Django web app on Heroku.

## Installation
The Code is written in Python 3.6 If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can run this or upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries, run this command in the project directory after [cloning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/) the repository:
```bash
pip install -r requirements.txt
```
## Directory Tree 
```
├── .idea 
├── movie_genere_prediction 
│   ├── movie_genere_classification
|       ├── migrations
|       ├── templates
|       ├── admin.py
|       ├── apps.py
|       ├── models.py
|       ├── tests.py
|       ├── urls.py
|       └── views.py
│   ├── movie_genere_prediction
│       ├── asgi.py
|       ├── settings.py
|       ├── urls.py
|       └── wsgi.py
|   ├── requirements.txt
|   ├── cv-transform.pkl
|   ├── kaggle_movie_train.csv
|   ├── Procfile
|   ├── README.md
|   ├── trainer.py
|   ├── manage.py
|   └── movie-genre-mnb-model.pkl
```
