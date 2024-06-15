
import streamlit as st
import pickle
import pandas as pd

st.set_page_config(page_title="Wine")
st.title("Quality of Wine")

filename = 'Wine.pkl'
with open(filename, 'rb') as file:
    Model = pickle.load(file)

st.header("Input Features")

fixed_acidity = st.text_input("fixed acidity",value=2.0)
volatile_acidity = st.text_input("volatile acidity")
citric_acid = st.text_input("citric acid")
residual_sugar = st.text_input("residual sugar")
chlorides = st.text_input("chlorides")
free_sulfur_dioxide = st.text_input("free sulfur dioxide")
total_sulfur_dioxide = st.text_input("total sulfur dioxide")
density = st.text_input("density")
pH = st.text_input("pH")
sulphates = st.text_input("sulphates")
alcohol = st.text_input("alcohol")

test_input = {
    "fixed acidity": [fixed_acidity],
    "volatile acidity": [volatile_acidity],
    "citric acid": [citric_acid],
    "residual sugar": [residual_sugar],
    "chlorides": [chlorides],
    "free sulfur dioxide": [free_sulfur_dioxide],
    "total sulfur dioxide": [total_sulfur_dioxide],
    "density": [density],
    "pH": [pH],
    "sulphates": [sulphates],
    "alcohol": [alcohol]
}

test_df = pd.DataFrame(test_input)

# Prediction
if st.button("Predict"):
    prediction = Model.predict(test_df)
    prediction_proba = Model.predict_proba(test_df)

    st.subheader("Prediction")
    if int(prediction[0])==0:
        st.markdown("## Quality of Wine is Bad!")
    else:
        st.markdown("## Quality of Wine is Good!")
    # st.write(f"The predicted quality of wine is: {prediction[0]}")

    st.write("Prediction probabilities:")
    st.write(prediction_proba)