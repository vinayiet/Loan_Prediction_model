import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="Loan Approval System", layout="centered")

st.title("Loan Approval Prediction System")

# Sidebar actions
st.sidebar.header("Model Actions")

if st.sidebar.button("Train / Retrain Model"):
    r = requests.post(f"{API_BASE}/retrain")
    if r.status_code == 200:
        st.sidebar.success(r.json()["message"])
    else:
        st.sidebar.error("Training failed")

st.subheader("Enter Applicant Details")

name = st.text_input("Name")
age = st.number_input("Age", min_value=18, max_value=100, value=25)
income = st.number_input("Monthly Income", min_value=0.0, value=30000.0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
employment_years = st.number_input("Employment Years", min_value=0, max_value=40, value=2)
monthly_expense = st.number_input("Monthly Expense", min_value=0.0, value=10000.0)

education_level = st.selectbox(
    "Education Level",
    ["High School", "Associate", "Bachelor", "Master", "PhD"]
)

marital_status = st.selectbox(
    "Marital Status",
    ["Single", "Married"]
)

existing_loans = st.selectbox(
    "Previous Loan Default",
    ["Yes", "No"]
)

if st.button("Predict Loan Approval"):
    payload = {
        "name": name,
        "age": age,
        "income": income,
        "credit_score": credit_score,
        "employment_years": employment_years,
        "existing_loans": existing_loans,
        "monthly_expense": monthly_expense,
        "education_level": education_level,
        "marital_status": marital_status,
        "approved": None
    }

    r = requests.post(f"{API_BASE}/add-applicant", json=payload)

    if r.status_code != 200:
        st.error("Failed to add applicant")
    else:
        applicant_id = r.json()["applicant_id"]

        pr = requests.get(f"{API_BASE}/predict/{applicant_id}")
        if pr.status_code != 200:
            st.error("Prediction failed")
        else:
            result = pr.json()
            prob = result["probability"]
            status = "Approved" if result["predicted_status"] == 1 else "Rejected"

            st.success(f"Prediction: {status}")
            st.info(f"Approval Probability: {round(prob * 100, 2)}%")
