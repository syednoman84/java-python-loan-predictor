import pandas as pd
import joblib
import os
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from app.core.config import MODEL_PATH_LC

# Load CSV
print("Looking for file at:", os.path.abspath("data/loan_sample_data.csv"))
# Resolve full path to CSV relative to project root
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(BASE_DIR, "data", "loan_sample_data.csv")
df = pd.read_csv(CSV_PATH)

# Keep only relevant loan statuses
df = df[df['loan_status'].isin(['Fully Paid', 'Charged Off'])]

# Map loan_status to binary
df['loan_status'] = df['loan_status'].map({'Fully Paid': 0, 'Charged Off': 1})

# Select useful features
features = [
    'loan_amnt', 'term', 'int_rate', 'annual_inc',
    'emp_length', 'dti', 'fico_range_high'
]

df = df[features + ['loan_status']].copy()

# Clean term ("36 months" → 36)
df['term'] = df['term'].str.extract(r'(\d+)').astype(float)

# Clean emp_length ("10+ years", "< 1 year", etc.)
def parse_emp_length(emp):
    if pd.isna(emp):
        return 0
    if '<' in emp:
        return 0.5
    if '10+' in emp:
        return 10
    return float(''.join(filter(str.isdigit, emp)) or 0)

df['emp_length'] = df['emp_length'].apply(parse_emp_length)

# Drop any rows with missing values
df.dropna(inplace=True)

# Split
X = df[features]
y = df['loan_status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save
joblib.dump(model, MODEL_PATH_LC)
print(f"✅ Model trained and saved to {MODEL_PATH_LC}")
