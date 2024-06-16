# Wine Quality

## Overview
This project involves analyzing a wine dataset to predict wine quality based on various chemical properties. The steps undertaken include Exploratory Data Analysis (EDA), feature engineering, model training using Logistic Regression, and deploying the model using Streamlit.

## Dataset
The dataset used in this project is the Wine Quality dataset, which consists of various chemical properties of wine samples and their quality ratings. The data is provided in a CSV file named [wine.csv](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset/data).

## Project Steps

### 1. Exploratory Data Analysis (EDA)
EDA is performed to understand the structure and characteristics of the dataset. This includes:
- Descriptive statistics
- Data visualization
- Checking for missing values
- Finding outliers
- Identifying correlations between features

### 2. Feature Engineering
Feature engineering is applied to enhance the dataset's predictive power. This includes:
- Handling missing values
- Creating new features
- Encoding categorical variables (if any)
- Scaling numerical features

### 3. Model Training
A Logistic Regression model is trained to predict wine quality. The steps include:
- Splitting the data into training and test sets
- Training the Logistic Regression model
- Evaluating the model's performance using appropriate metrics (e.g., accuracy, precision, recall)

### 4. Model Serialization
The trained model is serialized into a pickle file (`model.pkl`) for future use without retraining.

### 5. Deployment with Streamlit
The model is deployed using Streamlit, allowing users to input wine characteristics and obtain quality predictions.

## Files in the Repository
- [wine.csv](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset/data): The original dataset.
- `wine.ipynb`: Jupyter notebook containing the Exploratory Data Analysis.
- `requirements.txt`: It contains the modules that are needed to create this project.
- `wine.pkl`: Serialized Logistic Regression model.
- [app.py](https://wine-qulity-4ja5kkfv5stfkjhfp9ghff.streamlit.app/): Streamlit application script for deploying the model.

## How to Run the Project

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Streamlit
- Pandas
- Scikit-learn

## Thank you!!
