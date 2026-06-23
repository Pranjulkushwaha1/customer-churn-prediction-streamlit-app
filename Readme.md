# Customer Curn Prediction 1

## Problem Statement 2
Telecom Company ke customer Churn Kr rhe hai.
ML model banake hm predict krenge ki kaun kaun se customer Churn krenge.
Taki Company usnhe ya reward de ske jissse churn km ho.

## Dataset 3
- **Source:** IBM Telco Customer Churn Dataset
- **Rows:** 7043 customers
- **Columns:** 50 features
- **Target:** Churn Label (Yes/No)

## Tech Stack 4
- **Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Visualization:** Matplotlib, Seaborn
- **ML Library:** Scikit-learn, XGBoost
- **Web App:** Streamlit
- **API:** FastAPI
- **Containerization:** Docker
- **Dataset:** Kaggle

## Results 5

| Model | Accuracy | Churn Recall | F1 Score |
|---|---|---|---|
| Logistic Regression | 94.67% | 89% | 90% |
| Random Forest | 94.60% | 85% | 90% |
| XGBoost | 94.74% | 88% | 90% |
| Random Forest Tuned | 94.96% | 86% | 91% |

**Best Model:** Random Forest (Tuned)
**Accuracy:** 94.96%
**AUC Score:** 0.99 

## How to Run 6

### Streamlit App
```bash
streamlit run app.py
```

### FastAPI 7
```bash
uvicorn api:app --reload
```

### Docker 8
```bash
docker build -t churn-prediction .
docker run -p 8000:8000 churn-prediction
```

### Live Demo 9
🔗 [Streamlit App](https://customer-churn-prediction-app-app-ezgzctl7x8twnrxfjyqe4x.streamlit.app/)