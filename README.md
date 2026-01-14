# Loan Approval Prediction System

**End-to-End Machine Learning System with SQL, API, and UI**

This project demonstrates how a real-world Machine Learning system is built — not just a model in a notebook, but a **production-style ML application** with:

* A trained Logistic Regression model
* A SQL database as the system backbone
* A modular FastAPI backend
* A Streamlit-based user interface
* Full ML lifecycle: data → train → predict → store → retrain

It mirrors how ML systems are designed and deployed in industry.

---

## 🚀 What This Project Solves

Banks receive thousands of loan applications daily.
Manual screening is slow and inconsistent.

This system predicts whether a loan should be:

* **Approved (1)**
* **Rejected (0)**

based on applicant details like:

* Age
* Income
* Credit Score
* Employment Experience
* Monthly Expenses
* Education Level
* Marital Status
* Previous Loan Defaults

Using **Logistic Regression**, the system outputs:

* Approval probability
* Final decision (Approved / Rejected)

---

## 🧱 Architecture Overview

```
User (Streamlit UI)
        │
        ▼
FastAPI Backend (Uvicorn)
        │
        ├── Applicant Service  ──► SQL Database (Applicants)
        │
        ├── Prediction Service ──► ML Model (Logistic Regression)
        │                              │
        │                              ▼
        └────────────────────────── SQL Database (Predictions)
```

**Flow:**

1. User enters details in UI
2. Data is stored in SQL
3. ML model predicts
4. Result is stored in SQL
5. Response is shown in UI

---

## 🧠 Key Features

* Modular backend (industry-style architecture)
* SQL as a single source of truth
* ML trained directly from database
* Prediction logging
* Retraining endpoint
* Clean preprocessing pipeline
* Production-ready API
* Interactive Streamlit UI

---

## 🛠 Tech Stack

* Python
* FastAPI
* Uvicorn
* SQLite / PostgreSQL
* Scikit-learn
* Pandas
* Streamlit
* Joblib

---

## 📁 Project Structure

```
loan_ml_system/
│
├── app.py
├── ui.py
├── load_data.py
├── loan_data.csv
│
├── db/
│   └── database.py
│
├── models/
│   └── logistic_model.py
│
├── services/
│   ├── applicant_service.py
│   └── prediction_service.py
│
├── routes/
│   └── api_routes.py
│
└── utils/
    └── preprocess.py
```

---

## ⚙️ How to Run Locally

### 1. Start Backend

```
uv run uvicorn app:app --reload
```

Open API docs:

```
http://127.0.0.1:8000/docs
```

### 2. Train Model

Call:

```
POST /retrain
```

### 3. Run UI

```
uv run streamlit run ui.py
```

---

## 🧪 ML Lifecycle in This System

1. Kaggle dataset loaded into SQL
2. Model trains directly from SQL
3. New user data is stored in SQL
4. Predictions are generated
5. Results are logged
6. Admin can retrain anytime

This demonstrates **real ML engineering**, not just model training.

---

## 🎯 Why This Project Stands Out

Most ML projects end at:

> “I trained a model in Jupyter Notebook.”

This project goes further:

* Shows **system design**
* Integrates **SQL with ML**
* Demonstrates **API-based ML**
* Implements **real data flow**
* Mimics **production ML pipelines**
* Separates concerns like real companies do

It proves understanding of:

* Backend engineering
* Data engineering
* ML pipelines
* Deployment mindset
* End-to-end system design

---

## 🌍 Deployment

* Backend: Render / Fly.io / Railway
* UI: Streamlit Cloud
* Database: SQLite (demo) / PostgreSQL (production)

---

## 👤 Author
