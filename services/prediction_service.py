from db.database import get_connection
from services.applicant_service import get_applicant_by_id
from models.logistic_model import predict


def predict_for_applicant(applicant_id: int):
    applicant = get_applicant_by_id(applicant_id)
    if not applicant:
        return None

    features = {
        "age": applicant["age"],
        "income": applicant["income"],
        "credit_score": applicant["credit_score"],
        "employment_years": applicant["employment_years"],
        "existing_loans": applicant["existing_loans"],
        "monthly_expense": applicant["monthly_expense"],
        "education_level": applicant["education_level"],
        "marital_status": applicant["marital_status"],
    }

    probability, predicted_status = predict(features)

    # Store prediction in SQL
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO loan_predictions (
            applicant_id, probability, predicted_status
        )
        VALUES (?, ?, ?)
    """, (applicant_id, probability, predicted_status))

    conn.commit()
    conn.close()

    return {
        "applicant_id": applicant_id,
        "probability": probability,
        "predicted_status": predicted_status
    }
