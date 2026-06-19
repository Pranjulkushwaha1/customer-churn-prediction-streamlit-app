from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

model = pickle.load(open('churn_model.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))

@app.get('/')
def home():
    return {"Message":"Customer Churn Prediction API"}

class CustomerData(BaseModel):
    tenure: int
    monthly_charge: float
    satisfaction_score: int
    number_of_referrals: int
    contract: str
    internet_type: str
    payment_method: str
    offer: str
@app.post("/predict")
def predict(data: CustomerData):
    input_data = np.zeros(41)

    input_data[5] = data.number_of_referrals
    input_data[6] = data.tenure
    input_data[21] = data.monthly_charge
    input_data[23] = data.satisfaction_score

    offer_mapping = {
        'No Offer':25, 'Offer A':26, 'Offer B':27,
        'Offer C':28, 'Offer D':29, 'Offer E':30,
    }
    input_data[offer_mapping[data.offer]] = 1

    internet_mapping = {
        'Cable':31, 'DSL':32,
        'Fiber Optic':33, 'No Internet':34
    }
    input_data[internet_mapping[data.internet_type]] = 1

    contract_mapping = {
        'Month-to-Month':35,
        'One Year':36,
        'Two Year':37
    }
    input_data[contract_mapping[data.contract]] = 1

    payment_mapping = {
        'Bank Withdrawal':38,
        'Credit Card':39,
        'Mailed Check':40
    }
    input_data[payment_mapping[data.payment_method]] = 1

    input_scaled = scaler.transform([input_data])
    Prediction = int(model.predict(input_scaled)[0])

    return{
        "Prediction":Prediction,
        "result":"Churn Karega" if Prediction == 1 else "Nahi Jayega"
    }