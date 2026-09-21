import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/rainfall_model.pkl.gz")

# Load feature list
features = joblib.load("models/features.pkl")

# Page configuration
st.set_page_config(
    page_title="Indian Rainfall Prediction",
    page_icon="🌧️",
    layout="centered"
)

# Title
st.title("🌧️ Indian Rainfall Prediction")
st.write(
    "Enter the weather conditions below to predict whether rainfall will occur."
)


# Weather input section
st.subheader("Enter Weather Details")

col1, col2 = st.columns(2)

with col1:
    avg_temp = st.number_input("Average Temperature (°C)", value=25.0)
    min_temp = st.number_input("Minimum Temperature (°C)", value=20.0)
    max_temp = st.number_input("Maximum Temperature (°C)", value=30.0)
    wind_speed = st.number_input("Wind Speed", value=8.0)

with col2:
    air_pressure = st.number_input("Air Pressure (hPa)", value=1008.0)
    elevation = st.number_input("Elevation (m)", value=200.0)
    latitude = st.number_input("Latitude", value=28.6)
    longitude = st.number_input("Longitude", value=77.2)


# Prediction button
if st.button("Predict Rainfall"):

    input_data = pd.DataFrame([[
        avg_temp,
        min_temp,
        max_temp,
        wind_speed,
        air_pressure,
        elevation,
        latitude,
        longitude
    ]], columns=features)

    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success("🌧️ Rainfall Expected")
    else:
        st.info("☀️ No Rainfall Expected")

    st.write(f"**Rain Probability:** {probability[1] * 100:.2f}%")
    st.write(f"**No Rain Probability:** {probability[0] * 100:.2f}%")