from fastapi import APIRouter
from app.schemas.predict_schema_lc import LoanFeatures, PredictionResponse
from app.models.model_loader_lc import load_model

router = APIRouter()

model = load_model()

@router.post("/predict/lc", response_model=PredictionResponse)
def predict_default(features: LoanFeatures):
    # Convert input to 2D array for model
    input_data = [[
        features.loan_amnt,
        features.term,
        features.int_rate,
        features.annual_inc,
        features.emp_length,
        features.dti,
        features.fico_range_high
    ]]

    prediction = model.predict(input_data)
    return PredictionResponse(default_risk=int(prediction[0]))
