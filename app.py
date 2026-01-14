from fastapi import FastAPI
from db.database import create_tables
from routes.api_routes import router
from models.logistic_model import load_model

app = FastAPI()

@app.on_event("startup")
def startup_event():
    create_tables()
    load_model()

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Loan ML System is running"}
