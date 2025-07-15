from pydantic import BaseModel

class LoanFeatures(BaseModel):
    loan_amnt: float
    term: float                   # already converted from string like "36 months"
    int_rate: float
    annual_inc: float
    emp_length: float             # parsed to numeric in training
    dti: float
    fico_range_high: float

class PredictionResponse(BaseModel):
    default_risk: int
