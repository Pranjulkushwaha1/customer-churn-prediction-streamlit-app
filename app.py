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