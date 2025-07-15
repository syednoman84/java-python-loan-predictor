# 🧠 Loan Default Predictor (Java + Python ML Integration)

This project demonstrates a full-stack, polyglot microservice architecture where:

- A **Python FastAPI service** trains and serves machine learning models to predict loan default risk.
- A **Java Spring Boot application** consumes these models via REST API calls for real-time scoring.
- Two models are supported:
    - A **dummy baseline model** with synthetic logic
    - A **real model** trained on LendingClub loan data

---

## 🚀 Tech Stack

| Layer             | Technology                     |
|------------------|---------------------------------|
| ML Model Training| Python (scikit-learn, pandas)   |
| Model Serving     | FastAPI                        |
| Backend API       | Spring Boot (Java)             |
| Interop           | REST (JSON)                    |

---

## 📁 Project Structure

### Python ML Service (`python-ml-api/`)

```
python-ml-api/
├── app/
│   ├── api/endpoints/
│   │   ├── predict.py         # Dummy model endpoint (/predict)
│   │   └── predict_lc.py      # LendingClub model endpoint (/predict/lc)
│   ├── models/
│   │   ├── model_loader.py
│   │   └── model_loader_lc.py
│   ├── schemas/
│   │   ├── predict_schema.py
│   │   └── predict_schema_lc.py
│   ├── main.py                # FastAPI entry point
├── training/
│   ├── train_model.py         # Trains dummy model
│   └── train_model_lc.py      # Trains LendingClub model
├── data/
│   └── loan_sample_data.csv   # LendingClub sample dataset (10k rows)
├── loan_default_model.pkl     # Saved dummy model
├── loan_default_model_lc.pkl  # Saved LendingClub model
```

### Java Spring Boot Client (`java-springboot-client/`)

```
java-springboot-client/
├── LoanPredictionRequest.java         # For /predict
├── LoanPredictionRequestLC.java       # For /predict/lc
├── LoanPredictionResponse.java
├── LoanPredictionService.java
├── LoanPredictionController.java
```

---

## ✅ Features

- [x] FastAPI ML model serving (2 models)
- [x] Java client integration
- [x] Swagger UI testing
- [x] Spring Boot endpoints mapping to ML models
- [x] Separation of logic and schema per model

---

## 🧪 API Testing

### Swagger UI

Start the Python FastAPI app:

```bash
uvicorn app.main:app --reload
```

Then open in browser:
- [http://localhost:8000/docs](http://localhost:8000/docs)

### Example Request Payload (LendingClub `/predict/lc`)

```json
{
  "loan_amnt": 25000,
  "term": 60,
  "int_rate": 23.5,
  "annual_inc": 22000,
  "emp_length": 0.5,
  "dti": 29.8,
  "fico_range_high": 600
}
```

### Expected Response

```json
{
  "default_risk": 1
}
```

---

## 🛠 How to Run

### 1. Train the models

```bash
# Train dummy model
python training/train_model.py

# Train LendingClub model
python training/train_model_lc.py
```

### 2. Start the FastAPI server

```bash
uvicorn app.main:app --reload
```

### 3. Run the Spring Boot app

From `java-springboot-client/`:

```bash
./mvnw spring-boot:run
```

Or from IDE like IntelliJ.

---

## 📬 Available Endpoints

| Endpoint URL         | Description                     |
|----------------------|---------------------------------|
| `POST /predict`      | Predict using dummy model        |
| `POST /predict/lc`   | Predict using LendingClub model  |

---

## 💡 Future Enhancements

- [ ] Add `/retrain` endpoint for dynamic retraining
- [ ] Add Docker support for full stack deployment
- [ ] Secure endpoints with API keys or OAuth
- [ ] Log predictions for monitoring & feedback
- [ ] Add frontend UI (React or Thymeleaf)


---

## 👨‍💻 Author

Built by Syed Noman Ahmed — a full-stack integration of ML + Java APIs.
