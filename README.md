# Indian Rainfall Prediction 🌧️

A Machine Learning web application that predicts whether rainfall will occur based on meteorological and geographical conditions.

## 🌍 Live Demo

[**Try the Indian Rainfall Prediction Web App**](https://rainfall-prediction-bnunqbsj5eccfvp6dumfd9.streamlit.app/)

---

## 📌 Project Overview

Rainfall prediction is an important application of Machine Learning in areas such as agriculture, water resource management, disaster preparedness, and weather analysis.

This project uses historical Indian weather data to build a **binary classification model** that predicts:

- `1` → Rain
- `0` → No Rain

A **Random Forest Classifier** was trained and tuned using meteorological and geographical features.

The trained model is integrated into a **Streamlit web application**, where users can enter weather conditions and receive a rainfall prediction along with the predicted probabilities.

---

## 🎯 Objective

The main objective of this project is to build an end-to-end Machine Learning system that can:

1. Analyze historical rainfall and weather data.
2. Clean and preprocess the dataset.
3. Perform Exploratory Data Analysis (EDA).
4. Create a binary rainfall target.
5. Train multiple classification models.
6. Tune the Random Forest model.
7. Evaluate model performance.
8. Analyze feature importance.
9. Save the trained model.
10. Deploy the model through a Streamlit application.

---

## 📊 Dataset

The project uses an Indian weather and rainfall dataset containing meteorological and geographical information.

The original dataset contains **970,000+ records**.

For development on a system with limited resources, a **100,000-row working subset** was used for EDA and model development.

### Dataset Features

| Feature | Description |
|---|---|
| `date_of_record` | Date of observation |
| `month` | Month of observation |
| `season` | Season |
| `station_name` | Weather station |
| `state` | State |
| `district` | District |
| `avg_temp` | Average temperature |
| `min_temp` | Minimum temperature |
| `max_temp` | Maximum temperature |
| `wind_speed` | Wind speed |
| `air_pressure` | Atmospheric pressure |
| `elevation` | Elevation of the location |
| `latitude` | Latitude |
| `longitude` | Longitude |
| `rainfall` | Daily rainfall in millimeters |

The raw dataset is not included in this repository to keep the repository lightweight.

---

## 🔍 Exploratory Data Analysis

The project includes analysis of:

- Dataset dimensions
- Data types
- Missing values
- Duplicate records
- Categorical variables
- Numerical variables
- Rainfall distribution
- Rainfall frequency
- Seasonal rainfall patterns
- Monthly rainfall patterns
- Rain/No Rain distribution
- Feature relationships
- Feature importance

### Important EDA Findings

The working dataset contained:

- **100,000 records**
- **15 original features**
- **43 weather stations**
- **9 states**
- **4 seasons**
- **12 months**

Rainfall was highly skewed, with a large number of observations having zero rainfall.

After removing rows with missing rainfall values:

- Original rows: `100,000`
- Rows used for modeling: `74,835`

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

1. Checked missing values.
2. Checked duplicate records.
3. Removed records with missing rainfall values.
4. Filled missing numerical weather values using their median.
5. Created the binary target variable:

```text
Rainfall = 0       → No Rain
Rainfall > 0       → Rain
```

---

## 📈 Model Performance

The machine learning model (Tuned Random Forest) was evaluated on a test dataset and achieved the following metrics:
- **Accuracy:** ~80.0%
- **Precision (Rain):** ~77.0%
- **Recall (Rain):** ~74.0%
- **F1-Score (Rain):** ~75.0%
- **ROC-AUC Score:** ~87.9%
