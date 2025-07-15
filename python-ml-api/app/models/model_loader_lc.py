import os
import joblib
from app.core.config import MODEL_PATH_LC

def load_model():
    if not os.path.exists(MODEL_PATH_LC):
        raise FileNotFoundError(f"Model not found at: {MODEL_PATH_LC}")
    return joblib.load(MODEL_PATH_LC)
