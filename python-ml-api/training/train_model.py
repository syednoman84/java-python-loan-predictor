import os
import sys
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier

# 🔧 Add root directory to import app.core.config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.config import MODEL_PATH

# 🧪 Dummy dataset
X = np.random.rand(1000, 4) * 10000
y = (X[:, 1] > 5000).astype(int)

model = RandomForestClassifier()
model.fit(X, y)

# 💾 Save model using absolute path
joblib.dump(model, MODEL_PATH)
print(f"✅ Model saved to: {MODEL_PATH}")
