import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
import json
import pandas as pd


# load data
df=pd.read_csv('./training_data/featured_data.csv')
test_df=df.sample(5)
X=df.drop('Heart Attack Likelihood',axis=1)
y=df['Heart Attack Likelihood']

# Load transformers
pipeline_transformers = joblib.load("./models/transformers.pkl")


# Load model parameters
with open("./models/model_params.json", "r") as f:
    model_params = json.load(f)

# Rebuild RandomForest model
rf_model = RandomForestClassifier(**model_params)

# Add model back to pipeline
from sklearn.pipeline import Pipeline
pipeline = Pipeline(pipeline_transformers.steps + [("random_forest", rf_model)])
pipeline.fit(X,y)

# X_test=test_df.drop('Heart Attack Likelihood',axis=1)
# y_test=test_df['Heart Attack Likelihood']
# y_pred=pipeline.predict(X_test)
# print(X_test)


# Function to take user input and make predictions
def predict_heart_attack(df):
    prediction = pipeline.predict(df)
    probability = pipeline.predict_proba(df) # Probability of heart attack
    return prediction, probability

# if(app.submit_button):
#     a=predict_heart_attack(df)
#     print(a)