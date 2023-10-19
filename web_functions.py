"""This module contains necessary function needed"""

# Import necessary modules
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import streamlit as st
from sklearn.ensemble import RandomForestRegressor


@st.cache_data
def load_data():
    """This function returns the preprocessed data"""

    # Load the Diabetes dataset into DataFrame.
    df = pd.read_csv('./preprocessed_traffic_dataset.csv')
    data1 = pd.read_csv('./traffic_volume_data.csv')

    # Perform feature and target split
    X = df[['is_holiday', 'temperature','weekday', 'hour', 'month_day', 'year', 'month','weather_type','weather_description']]
    y = df['traffic_volume']

    return df, X, y,data1

@st.cache_data
def train_model(X, y):
    """This function trains the model and return the model and model score"""
    # Create the model
    #instantiating an instance of the Random Forest Model
    random_model = RandomForestRegressor()
    
    # Fit the data on model
    random_model.fit(X,y)
    # Get the model score
    score = random_model.score(X, y)

    # Return the values
    return random_model, score

def predict(X, y, features):
    # Get model and model score
    model, score = train_model(X, y)
    # Predict the value
    prediction = model.predict(np.array(features).reshape(1, -1))

    return prediction, score
