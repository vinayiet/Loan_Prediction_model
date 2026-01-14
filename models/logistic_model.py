import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from services.applicant_service import get_training_data

MODEL_PATH = "models/loan_model.joblib"

# True numeric columns
NUM_COLS = [
    "age",
    "income",
    "credit_score",
    "employment_years",
    "monthly_expense"
]

# Categorical columns
CAT_COLS = [
    "education_level",
    "marital_status",
    "existing_loans"
]

_model = None


def _clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Ensure numeric columns are numeric and have no NaN
    for col in NUM_COLS:
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Ensure categorical columns are strings and have no NaN
    for col in CAT_COLS:
        df[col] = df[col].astype(str).fillna("Unknown")

    return df


def train_model():
    global _model

    data = get_training_data()
    if not data:
        raise ValueError("No training data found in database.")

    df = pd.DataFrame(data)
    df = _clean_dataframe(df)

    X = df[NUM_COLS + CAT_COLS]
    y = df["approved"]

    pipeline = Pipeline(steps=[
        (
            "preprocess",
            ColumnTransformer(
                transformers=[
                    ("num", "passthrough", NUM_COLS),
                    ("cat", OneHotEncoder(handle_unknown="ignore"), CAT_COLS),
                ]
            ),
        ),
        ("model", LogisticRegression(max_iter=1000)),
    ])

    pipeline.fit(X, y)

    joblib.dump(pipeline, MODEL_PATH)
    _model = pipeline

    return "Model trained and saved."


def load_model():
    global _model
    try:
        _model = joblib.load(MODEL_PATH)
    except FileNotFoundError:
        _model = None


def predict(features: dict):
    if _model is None:
        raise ValueError("Model not loaded. Train the model first.")

    df = pd.DataFrame([features])
    df = _clean_dataframe(df)

    prob = _model.predict_proba(df)[0][1]
    pred = int(prob >= 0.5)

    return prob, pred
