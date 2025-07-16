import joblib
import pandas as pd
from sklearn.tree import export_graphviz
from sklearn import tree
import graphviz
import os
import matplotlib.pyplot as plt


# Load model
from app.core.config import MODEL_PATH_LC
model = joblib.load(MODEL_PATH_LC)

# Load a few rows of your training data
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
CSV_PATH = os.path.join(BASE_DIR, "data", "loan_sample_data.csv")
df = pd.read_csv(CSV_PATH)

# Clean just enough for consistent features (reuse logic from training script)
df = df[df['loan_status'].isin(['Fully Paid', 'Charged Off'])]
df['loan_status'] = df['loan_status'].map({'Fully Paid': 0, 'Charged Off': 1})
df['term'] = df['term'].str.extract(r'(\d+)').astype(float)

def parse_emp_length(emp):
    if pd.isna(emp): return 0
    if '<' in emp: return 0.5
    if '10+' in emp: return 10
    return float(''.join(filter(str.isdigit, emp)) or 0)

df['emp_length'] = df['emp_length'].apply(parse_emp_length)
df.dropna(inplace=True)

features = [
    'loan_amnt', 'term', 'int_rate', 'annual_inc',
    'emp_length', 'dti', 'fico_range_high'
]

X = df[features]

# Pick the first tree from the forest
estimator = model.estimators_[0]

# Export tree to DOT format
dot_data = tree.export_graphviz(
    estimator,
    out_file=None,
    feature_names=features,
    class_names=['Fully Paid', 'Defaulted'],
    filled=True,
    rounded=True,
    special_characters=True
)

# Generate visualization
graph = graphviz.Source(dot_data)
graph.render("tree_visualization", format="pdf", cleanup=True)

plt.figure(figsize=(20,10))
tree.plot_tree(estimator, feature_names=features, class_names=['Paid', 'Defaulted'], filled=True)
plt.show()

print("✅ Decision tree saved as tree_visualization.pdf")
