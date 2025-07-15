import pandas as pd
from app.core.config import MASTER_DATA_PATH
from app.core.config import SAMPLE_DATA_PATH

# Load with low memory usage
df = pd.read_csv(MASTER_DATA_PATH, low_memory=False)

# Keep only rows with valid loan status
df = df[df['loan_status'].isin(['Fully Paid', 'Charged Off'])]

# Sample 10,000 rows
sample_df = df.sample(n=10000, random_state=42)

# Save to a smaller CSV
sample_df.to_csv(SAMPLE_DATA_PATH, index=False)
