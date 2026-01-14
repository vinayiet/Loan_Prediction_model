from db.database import get_connection


def add_applicant(data: dict):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO applicants (
            name, age, income, credit_score, employment_years,
            existing_loans, monthly_expense, education_level,
            marital_status, approved
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["name"],
        data["age"],
        data["income"],
        data["credit_score"],
        data["employment_years"],
        data["existing_loans"],
        data["monthly_expense"],
        data["education_level"],
        data["marital_status"],
        data.get("approved")
    ))

    conn.commit()
    applicant_id = cursor.lastrowid
    conn.close()

    return applicant_id


def get_applicant_by_id(applicant_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM applicants WHERE id = ?", (applicant_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        return dict(row)
    return None


def get_training_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT age, income, credit_score, employment_years,
               existing_loans, monthly_expense,
               education_level, marital_status, approved
        FROM applicants
        WHERE approved IS NOT NULL
    """)

    rows = cursor.fetchall()
    conn.close()

    return [dict(r) for r in rows]

