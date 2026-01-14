from fastapi import APIRouter, HTTPException
from services.applicant_service import add_applicant
from services.prediction_service import predict_for_applicant
from models.logistic_model import train_model

router = APIRouter()


@router.post("/add-applicant")
def add_new_applicant(data: dict):
    try:
        applicant_id = add_applicant(data)
        return {"message": "Applicant added", "applicant_id": applicant_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/predict/{applicant_id}")
def predict(applicant_id: int):
    result = predict_for_applicant(applicant_id)
    if not result:
        raise HTTPException(status_code=404, detail="Applicant not found")
    return result


@router.post("/retrain")
def retrain():
    msg = train_model()
    return {"message": msg}
