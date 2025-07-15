from fastapi import APIRouter
from app.schemas.predict_schema import LoanFeatures, PredictionResponse
from app.models.model_loader import load_model

router = APIRouter()

model = load_model()

@router.post("/predict", response_model=PredictionResponse)
def predict_default(features: LoanFeatures):
    data = [[features.income, features.loan_amount, features.term, features.credit_score]]
    prediction = model.predict(data)
    return PredictionResponse(default_risk=int(prediction[0]))
