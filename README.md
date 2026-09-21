# Indian Rainfall Prediction 🌧️

**[🌍 Live Demo: Play with the Web App here!](https://rainfall-prediction-bnunqbsj5eccfvp6dumfd9.streamlit.app/)**

This project is a Machine Learning web application built with **Streamlit** that predicts the likelihood of rainfall in India based on various weather conditions.

## Project Structure
- `app.py`: The main Streamlit web application.
- `models/`: Contains the pre-trained machine learning model (`rainfall_model.pkl`) and feature list (`features.pkl`).
- `01_EDA_Rainfall_Prediction.ipynb.ipynb`: Jupyter notebook containing Exploratory Data Analysis (EDA) and model training code.
- `india_weather_rainfall_data.xlsx`: The dataset used for training the model (Note: Ignored in version control due to large file size).

## Features
The web app takes the following inputs to predict rainfall:
- Average, Minimum, and Maximum Temperature (°C)
- Wind Speed
- Air Pressure (hPa)
- Elevation (m)
- Latitude & Longitude

## How to Run

1. Make sure you have Python installed.
2. Install the required dependencies:
   ```bash
   pip install streamlit pandas joblib scikit-learn
   ```
3. Run the application:
   ```bash
   streamlit run app.py
   ```
4. Open the provided local URL in your browser to interact with the app.

## Note on Large Files
Due to GitHub's file size limit (100MB), the raw dataset (`india_weather_rainfall_data.xlsx`, ~64MB) and the trained model (`rainfall_model.pkl`, ~110MB) are ignored via `.gitignore` and are not hosted on this repository. Ensure you have trained the model locally or have the `models/` folder populated before running the web app!
