import pandas as pd
from db.database import get_connection

# Load CSV
df = pd.read_csv("/Users/vinaysharma/loan_ml_system/db/loan_data.csv")

# Rename columns to match DB schema
df = df.rename(columns={
    "person_age": "age",
    "person_income": "income",
    "credit_score": "credit_score",
    "person_emp_exp": "employment_years",
    "previous_loan_defaults_on_file": "existing_loans",
    "loan_amnt": "monthly_expense",
    "person_education": "education_level",
    "person_gender": "marital_status",
    "loan_status": "approved"
})

# Add columns that don't exist in CSV
df["name"] = "Unknown"

# Convert target to 0/1 if needed
# (If loan_status is already 0/1, this will keep it same)
if df["approved"].dtype == object:
    df["approved"] = df["approved"].map({"Y": 1, "N": 0})

# Keep only required columns in correct order
df = df[[
    "name",
    "age",
    "income",
    "credit_score",
    "employment_years",
    "existing_loans",
    "monthly_expense",
    "education_level",
    "marital_status",
    "approved"
]]

# Insert into SQL
conn = get_connection()
df.to_sql("applicants", conn, if_exists="append", index=False)
conn.close()

print("Data loaded into SQL successfully.")
