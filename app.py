import streamlit as st
import pandas as pd 
import numpy as np
from server import predict_heart_attack

# Custom CSS for Heart-Themed UI
st.markdown("""
    <style>
    /* Background Image */
    .stApp {
        background-image: url("https://source.unsplash.com/1600x900/?heart,health");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    /* Title Styling */
    .title {
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        color: #E63946;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Centered Form Styling */
    .centered-form {
        max-width: 600px;
        margin: auto;
        padding: 2rem;
        border-radius: 15px;
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0px 4px 10px rgba(0,0,0,0.2);
    }
    
    /* Button Styling */
    .stButton>button {
        background-color: #E63946;
        color: white;
        border-radius: 10px;
        font-size: 1rem;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #D62828;
    }
    </style>
""", unsafe_allow_html=True)



# App Title
st.markdown('<h1 class="title"> Heart Attack Prediction</h1>', unsafe_allow_html=True)
st.header("Enter your Health details")

# Centered Form
with st.container():
    st.markdown('<div class="centered-form">', unsafe_allow_html=True)

    # User Inputs
    #Demography
    gender = st.selectbox("Gender", ["Male", "Female","Other"])
    age = st.number_input("Age", 18, 100, 40)
    location=st.selectbox("Region",['North ', 'South', 'East', 'West','North-East','Central'])
    urb_rur=st.selectbox('Urban/Rural',['Urban','Rural'])
    SES=st.selectbox("Socioeconomic Status",['Low','Middle','High'])
    #Lifestyle Factors
    smoking =st.selectbox("Smoking Status",['Never','Occasionally','Regularly'])
    Alcohol=st.selectbox("Alcohol Status",['Never','Occasionally','Regularly'])
    diet=st.selectbox("Diet Type",['Non-Vegetarian','Vegan','Vegetarian'])
    Phy_act=st.selectbox("Physical Activity",['Sedentary','High','Moderate'])
    sleep_t=st.number_input("Sleep time (Hr/day)",1,24,8)
    screen_t=st.number_input("Screen time (Hr/day)",1,24,24)
    #Medical Histroy
    fam_med_hist=st.selectbox("Family History of Heart Disease",['No','Yes'])
    hypertension = st.selectbox("Hypertension", ["No", "Yes"])
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    cholesterol = st.number_input("Cholesterol Levels (mg/dL)", 100, 300, 180)
    bmi = st.number_input("BMI (kg/m²)", 10.0, 50.0, 24.0)
    stress_level = st.selectbox("Stress Level",['Low','Medium','High'])
    #Clinical and test Results
    Sy_bp=st.number_input("Systolic ",20,150,75)
    Di_bp=st.number_input("Diastolic ",20,150,60)
    resting_heart_rate = st.number_input("Resting Heart Rate (bpm)", 40, 120, 70)
    ecg_res=st.selectbox("ECG Results",['Normal','Abnormal'])
    chest_pain=st.selectbox("Chest Pain Type",['Non-anginal','Typical','Atypical','Asymptomatic'])
    max_heart_rate = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)
    exer_in=st.selectbox("Exercise Induced Angina",['No','Yes'])
    blood_o2=st.number_input("Blood Oxygen Levels(SpO2%)",20,100,80)
    trigly_level=st.number_input("Triglyceride Levels",1,500,500)
    
    #Submit Button
    submit_button = st.button("Predict")
    # Closing div tag for styling
    st.markdown('</div>', unsafe_allow_html=True)
    

if(submit_button):
    pulse=Sy_bp-Di_bp
    #Predicting Heart Attack
    df = pd.DataFrame({
    'Age': [age],  # Wrap values in lists to ensure they are 2D
    'Gender': [gender],
    'Region': [location],
    'Urban/Rural': [urb_rur],
    'SES': [SES],
    'Smoking Status': [smoking],
    'Alcohol Consumption': [Alcohol],
    'Diet Type': [diet],
    'Physical Activity Level': [Phy_act],
    'Screen Time (hrs/day)': [screen_t],
    'Sleep Duration (hrs/day)': [sleep_t],
    'Family History of Heart Disease': [fam_med_hist],
    'Diabetes': [diabetes],
    'Hypertension': [hypertension],
    'Cholesterol Levels (mg/dL)': [cholesterol],
    'BMI (kg/m²)': [bmi],
    'Stress Level': [stress_level],
    'Resting Heart Rate (bpm)': [resting_heart_rate],
    'ECG Results': [ecg_res],
    'Chest Pain Type': [chest_pain],
    'Maximum Heart Rate Achieved': [max_heart_rate],
    'Exercise Induced Angina': [exer_in],
    'Blood Oxygen Levels (SpO2%)': [blood_o2],
    'Triglyceride Levels (mg/dL)': [trigly_level],
    'Pluse Pressure': [pulse]
    })

    # print(df.shape)
   
    #Prediction
    prediction,prob=predict_heart_attack(df)
    print(prediction)
    
   
    # Display result
    st.subheader("🔍 Prediction Result")
    st.write(f"**Probability of No Heart Attack (0):** {prob[0][0]:.2%}")
    st.write(f"**Probability of Heart Attack (1):** {prob[0][1]:.2%}")
    st.write(f"**Predicted Class:** {'🛑 Heart Attack (1)' if prediction == 'Yes' else '✅ No Heart Attack (0)'}")

    # Conditional formatting based on risk
    if prediction == 1:
        st.error("⚠️ High Risk! Please consult a doctor.")
    else:
        st.success("✅ Low Risk! Maintain a healthy lifestyle.")