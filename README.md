# Heart Attack Prediction Web App

## 🚀 Project Overview
This project aims to predict the likelihood of a heart attack based on various health and lifestyle factors. The model is deployed as a web application using **Streamlit**.

## 📂 Dataset Details
- **Source:** Kaggle
- **Features:**
  - **Numerical:** Age, Screen Time, Sleep Duration, Cholesterol Levels, BMI, Resting Heart Rate, Maximum Heart Rate Achieved, Blood Oxygen Levels, Triglyceride Levels, Pulse Pressure
  - **Categorical:** Gender, Region, Urban/Rural, Socioeconomic Status (SES), Smoking Status, Alcohol Consumption, Diet Type, Physical Activity Level, Family History of Heart Disease, Diabetes, Hypertension, Stress Level, ECG Results, Chest Pain Type, Exercise Induced Angina
- **Target Variable:** Heart Attack Likelihood (Binary: 0 = No, 1 = Yes)

## 🛠 Tools & Libraries
- **Programming Language:** Python
- **Libraries:** Scikit-learn, Pandas, NumPy, Matplotlib, Seaborn, Streamlit, Joblib

## 🔄 Data Preprocessing
- **Handled Missing Values**
- **Encoded Categorical Features** using Label Encoding & Ordinal Encoding
- **Standardized Numerical Features** using StandardScaler

## ✨ Feature Selection
- Used **correlation analysis** and **feature importance techniques** to select the most relevant features.

## 🤖 Model Building
- **Algorithms Tried:** Logistic Regression, Decision Tree, Random Forest, XGBoost
- **Final Model:** [Selected Model]
- **Hyperparameter Tuning:** Used GridSearchCV for optimization

## 📊 Model Evaluation
- **Metrics:** Accuracy, Precision, Recall, F1-score, AUC-ROC Curve
- **Final Model Performance:** [Add metrics]

## 🌍 Web App Deployment
- **Framework:** Streamlit
- **How It Works:**
  1. Users input their health details.
  2. The model predicts the likelihood of a heart attack.
  3. The result is displayed with a risk indication.

## 🚀 Running the App
### 🔹 Prerequisites
- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
### 🔹 Start the App
  ```bash
  streamlit run app.py
  ```

## 🛠 Future Improvements
- Improve model accuracy with advanced deep learning techniques.
- Add more interpretability using SHAP or LIME.
- Enhance UI/UX with better visualizations.

---
📌 **Developed by:** Rohit Shere  
📆 **Date:** 10-03-2025



