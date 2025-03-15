import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import json
import pandas as pd


#load Model 
model=joblib.load("./models/model_rm.pkl")

# Function to take user input and make predictions
def predict_heart_attack(input):
    pred=model.predict(input)
    prob=model.predict_proba(input)
    return pred,prob


