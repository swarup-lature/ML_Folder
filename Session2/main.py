import numpy as np
import joblib
import streamlit as st

model = joblib.load(Path(__file__).resolve().parent / "data.joblib")

# page title
st.title("Student package prediction")

# Input Value

cgpa = st.number_input("Enter cgpa :")

if st.button("Predict Package"):
    try:
        input_data=np.array([[cgpa]])

        prediction=model.predict(input_data)

        st.sucess(prediction)
    except Exception as e:
        print(e)
    