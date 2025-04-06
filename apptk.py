import streamlit as st
import joblib
st.title("Heart Disease Prediction by Tanay")
model=joblib.load('ld.joblib')
sex=st.number_input("Enter the Gender Male:0, Female:1 : ")
age=st.number_input("Enter the Age of the patient: ")
cp=st.number_input("Enter the cp of the patient: ")
trestbps=st.number_input("Enter the trestbps of the patient: ")
if st.button("Predict to find out if the patient has a chance of Heart Disease"):
    prediction=model.predict([[sex,age,cp,trestbps]])
    if prediction=='1':
        st.text("Heart Disease may occur once go to the doctor")
    else:
        st.text("Heart Disease will not occur")
