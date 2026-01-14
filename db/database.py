import sqlite3

DB_NAME = "loan_ml.db"


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    # Applicants table (training + new data)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS applicants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            income REAL,
            credit_score INTEGER,
            employment_years INTEGER,
            existing_loans INTEGER,
            monthly_expense REAL,
            education_level TEXT,
            marital_status TEXT,
            approved INTEGER
        )
    """)

    # Predictions table (logging results)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS loan_predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            applicant_id INTEGER,
            probability REAL,
            predicted_status INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (applicant_id) REFERENCES applicants(id)
        )
    """)

    conn.commit()
    conn.close()

