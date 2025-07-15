from pydantic import BaseModel

class LoanFeatures(BaseModel):
    income: float
    loan_amount: float
    term: int
    credit_score: float

class PredictionResponse(BaseModel):
    default_risk: int
