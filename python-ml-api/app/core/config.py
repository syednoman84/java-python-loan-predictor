import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODEL_PATH = os.path.join(BASE_DIR, "loan_default_model.pkl")
MODEL_PATH_LC = os.path.join(BASE_DIR, "loan_default_model_lc.pkl")
MASTER_DATA_PATH = "/Users/NomanAhmed/Documents/Noman/code/github/accepted_2007_to_2018Q4.csv.gz"
SAMPLE_DATA_PATH = os.path.join(BASE_DIR, "loan_sample_data.csv")