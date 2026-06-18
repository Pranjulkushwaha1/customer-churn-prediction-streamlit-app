import streamlit as st
import pickle
import numpy as np

# ab hm model ko load krenge
model = pickle.load(open('churn_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

st.title("Welcome to Cusomer Churn Prediction")
tenure = st.slider("Tenure in Months",min_value=1,
                                        max_value=72,
                                        value=12)

monthly_charge = st.number_input("Monthly Charge",
                                min_value=18.250000,
                                max_value=118.750000,
                                value=50.0)

contract = st.selectbox("Contract Type",['Month-to-Month', 'One Year', 'Two Year'])
internet_type = st.selectbox("Internet Type", 
                              ['DSL', 'Fiber Optic', 'Cable', 'No Internet'])

payment_method = st.selectbox("Payment Method",
                               ['Bank Withdrawal', 'Credit Card', 'Mailed Check'])

number_of_referrals = st.number_input("Number of Referrals",
                                       min_value=0,
                                       max_value=11,
                                       value=0)

satisfaction_score = st.slider("Satisfaction Score",
                                min_value=1,
                                max_value=5,
                                value=3)

offer = st.selectbox("Offer",
                      ['No Offer', 'Offer A', 'Offer B', 
                       'Offer C', 'Offer D', 'Offer E'])

# Ab hm prediction Logic likhenge

# prediction ki button
if st.button("Predict Churn"):

    # Step 1 41 column ko zeros ka array banana hai.
    input_data = np.zeros(41)

    # Step 2 User Input shi postion me dalo.
    input_data[5] = number_of_referrals
    input_data[6] = tenure
    input_data[21] = monthly_charge
    input_data[23] = satisfaction_score

    # Step 3 Offer Encoading
    offer_mapping = {
        'No Offer':25,'Offer A':26, 'Offer B':27,
        'Offer C':28, 'Offer D':29, 'Offer E':30
    }
    input_data[offer_mapping[offer]] = 1

    # step 4 Internet type Encoding
    internet_mapping = {
        'Cable':31, 'DSL':32,
        'Fiber Optic':33, 'No Internet':34
    }
    input_data[internet_mapping[internet_type]] = 1

    # Step COntract Encoading
    Contract_mapping = {
        'Month-to-Month':35,
        'One Year':36,
        'Two Year':37
    }
    input_data[Contract_mapping[contract]] = 1

    # Step 6 Payment method encoading
    payment_mapping = {
        'Bank Withdrawal':38,
        'Credit Card':39,
        'Mailed Check':40
    }
    input_data[payment_mapping[payment_method]] = 1
    
    # Step 7 — Scale karo
    input_scaled = scaler.transform([input_data])
    
    # Step 8 — Predict karo
    prediction = model.predict(input_scaled)[0]
    
    # Step 9 — Result dikhao
    if prediction == 1:
        st.error("⚠️ Customer Churn Karega!")
    else:
        st.success("✅ Customer Nahi Jaayega!")