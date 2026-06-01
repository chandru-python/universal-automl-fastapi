# 🚀 AutoML FastAPI System

<div align="center">

### 🤖 Upload Any Dataset → Train Automatically → Predict Instantly

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green)
![MLflow](https://img.shields.io/badge/MLflow-Tracking-orange)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

</div>

---

# 📌 Project Overview

This project is a **Universal AutoML Platform** built using **FastAPI**, **Scikit-Learn**, and **MLflow**.

Users can:

✅ Upload any CSV dataset

✅ Select target column

✅ Automatically detect Classification or Regression

✅ Train multiple machine learning models

✅ Select the best performing model

✅ Track experiments with MLflow

✅ Save trained model automatically

✅ Generate dynamic prediction forms

✅ Predict new data through web interface

✅ Run inside Docker container

---

# 🎯 Key Features

## 📂 Dataset Upload

Upload any CSV dataset through web interface.

Supported:

* Classification datasets
* Regression datasets

---

## 🤖 Automatic Machine Learning

The system automatically:

* Loads dataset
* Cleans missing values
* Encodes categorical features
* Splits training/testing data
* Scales features
* Trains multiple algorithms
* Selects best model
* Saves trained artifacts

---

## 🧠 Supported Models

### Classification Models

* Logistic Regression
* Random Forest Classifier
* Support Vector Machine (SVM)

### Regression Models

* Linear Regression
* Random Forest Regressor

---

## 📊 Automatic Problem Detection

The system automatically detects:

### Classification

Example:

* Churn Prediction
* Disease Prediction
* Customer Segmentation

### Regression

Example:

* House Price Prediction
* Salary Prediction
* Sales Forecasting

---

## 📈 MLflow Integration

Every training run is logged with:

* Model Name
* Problem Type
* Accuracy Score
* R² Score

MLflow helps monitor model performance and experiments.

---

## 🔥 Dynamic Prediction System

After training:

* Feature names are extracted automatically
* Prediction form is generated dynamically
* User enters feature values
* Best model predicts output instantly

No manual coding required.

---

# 🏗️ Project Architecture

```text
AutoML-System/
│
├── app.py
├── automl_pipeline.py
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── login.html
│   ├── register.html
│   ├── upload.html
│   └── predict.html
│
├── uploads/
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── feature_names.pkl
│   ├── problem_type.pkl
│   └── label_encoders.pkl
│
├── requirements.txt
│
├── Dockerfile
│
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/automl-fastapi.git

cd automl-fastapi
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Requirements

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
uvicorn app:app --reload
```

Application:

```text
http://127.0.0.1:8000
```

---

# 📥 Upload Dataset

Navigate to:

```text
/upload
```

Upload:

* CSV Dataset
* Target Column Name

Example:

```text
Target = Species
```

or

```text
Target = Price
```

---

# 🧠 Training Workflow

```text
Dataset Upload
        ↓
Data Cleaning
        ↓
Encoding
        ↓
Feature Scaling
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Best Model Selection
        ↓
Save Model
        ↓
Prediction Ready
```

---

# 🔮 Prediction

Navigate to:

```text
/predict
```

The system automatically:

* Reads feature_names.pkl
* Creates input fields
* Accepts user values
* Predicts result

---

# 💾 Saved Artifacts

After training:

```text
models/

best_model.pkl
scaler.pkl
feature_names.pkl
problem_type.pkl
label_encoders.pkl
```

These files are reused for future predictions.

---

# 📊 MLflow Dashboard

Start MLflow:

```bash
mlflow ui
```

Open:

```text
http://127.0.0.1:5000
```

Track:

* Experiments
* Metrics
* Models
* Parameters

---

# 🐳 Docker Support

## Build Docker Image

```bash
docker build -t automl-fastapi .
```

---

## Run Container

```bash
docker run -p 8000:8000 automl-fastapi
```

Application:

```text
http://localhost:8000
```

---

# 📦 Requirements

```text
fastapi
uvicorn
jinja2
python-multipart
pandas
numpy
scikit-learn
joblib
mlflow
```

---

# 🌟 Future Enhancements

✅ XGBoost

✅ LightGBM

✅ CatBoost

✅ Hyperparameter Tuning

✅ Auto Feature Engineering

✅ Explainable AI (SHAP)

✅ User Authentication Database

✅ Cloud Deployment

✅ Model Download

✅ Auto Report Generation

---

# 🔐 Authentication Pages

Included Pages:

* Login
* Register
* About
* Upload
* Predict

Can be extended using:

* JWT Authentication
* OAuth2
* Google Login
* Role-Based Access

---

# 🎯 Use Cases

### Healthcare

* Disease Prediction
* Patient Risk Analysis

### Finance

* Credit Score Prediction
* Loan Approval

### Agriculture

* Crop Yield Prediction
* Soil Analysis

### Education

* Student Performance Prediction

### Business

* Customer Churn Prediction
* Sales Forecasting

---

# 👨‍💻 Developed With

❤️ FastAPI

❤️ Scikit-Learn

❤️ MLflow

❤️ NumPy

❤️ Pandas

❤️ Docker

---

# 📜 License

MIT License

Free to use, modify, and distribute.

---

<div align="center">

## 🚀 AutoML + FastAPI + MLflow = Production Ready Machine Learning

### Train Any Dataset In Minutes!

⭐ Star the repository if you found this project useful.

</div>
