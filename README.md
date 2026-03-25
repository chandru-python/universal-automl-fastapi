# Universal AutoML Web Application using FastAPI

A complete **FastAPI-based AutoML web application** that allows users to upload datasets, automatically train machine learning models, and make predictions through a dynamic web interface.  
The system supports both **Classification** and **Regression** tasks and automatically selects the **best-performing model**.

---

## 🚀 Features

- Upload custom CSV datasets
- Automatically detect **Classification** or **Regression**
- Handle missing values automatically
- Encode categorical columns automatically
- Scale feature columns using **StandardScaler**
- Train multiple machine learning models automatically
- Select and save the **best model**
- Dynamic prediction form generation based on dataset features
- Supports **FastAPI + Jinja2 HTML templates**
- Integrated **MLflow logging** for experiment tracking
- User-friendly pages:
  - Home
  - About
  - Login
  - Register
  - Upload Dataset
  - Predict Output

---

## 🧠 Supported Machine Learning Models

### For Classification:
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)

### For Regression:
- Linear Regression
- Random Forest Regressor

---

## 🏗️ Project Architecture

1. User uploads dataset (`.csv`)
2. User provides target column
3. System preprocesses data:
   - Missing value handling
   - Categorical encoding
   - Feature scaling
4. AutoML pipeline trains multiple models
5. Best model is selected based on performance
6. Best model and preprocessing files are saved
7. Prediction page dynamically generates input fields
8. User enters values and gets prediction result

---

## 📂 Project Structure

```bash
universal-automl-fastapi/
│
├── main.py
├── automl_pipeline.py
├── requirements.txt
├── README.md
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── login.html
│   ├── register.html
│   ├── upload.html
│   └── predict.html
│
├── models/
│   ├── best_model.pkl
│   ├── scaler.pkl
│   ├── problem_type.pkl
│   ├── feature_names.pkl
│   └── label_encoders.pkl
│
├── uploads/
│   └── uploaded_dataset.csv
│
└── mlruns/
```

---

## ⚙️ Technologies Used

- **Python**
- **FastAPI**
- **Jinja2**
- **Scikit-learn**
- **Pandas**
- **NumPy**
- **Joblib**
- **MLflow**
- **HTML / CSS**

---

## 📊 How It Works

### Step 1: Upload Dataset
Users upload a CSV dataset and specify the target column.

### Step 2: Automatic Preprocessing
The system automatically:
- fills missing values
- encodes categorical values
- scales feature values

### Step 3: AutoML Training
The application trains multiple ML models and compares their performance.

### Step 4: Best Model Selection
The best-performing model is selected and saved.

### Step 5: Dynamic Prediction
The prediction page generates a form dynamically based on the trained model’s input features.

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/chandru-python/universal-automl-fastapi.git
cd universal-automl-fastapi
```

### 2. Create Virtual Environment

#### Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / Mac:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

Then open your browser:

```bash
http://127.0.0.1:8000
```

---

## 🌐 Available Pages

| Route | Description |
|------|-------------|
| `/` | Home Page |
| `/about` | About Page |
| `/login` | Login Page |
| `/register` | Register Page |
| `/upload` | Upload Dataset Page |
| `/predict` | Prediction Page |

---

## 📈 MLflow Tracking

This project uses **MLflow** to log:

- model name
- problem type
- accuracy / R² score
- trained models

To view MLflow UI:

```bash
mlflow ui
```

Then open:

```bash
http://127.0.0.1:5000
```

---

## 🧪 Example Use Cases

- Student ML mini projects
- Academic research projects
- Generic prediction systems
- Auto model comparison
- Dynamic machine learning deployment
- Rapid prototyping of ML solutions

---

## 🔐 Future Improvements

- User authentication with database
- Support for Excel datasets (`.xlsx`)
- Download trained models
- Model explainability (SHAP / feature importance)
- Better AutoML model search
- Hyperparameter tuning
- Visualization dashboard
- Deployment on Render / Railway / AWS / Azure

---

## 📌 Advantages of This Project

- Beginner-friendly AutoML system
- Works for **any tabular dataset**
- No need to manually code separate ML models each time
- Dynamic web interface
- Real-world deployment-ready structure

---

## 👨‍💻 Author

**Chandru M**  
Machine Learning Engineer  

- GitHub: [chandru-python](https://github.com/chandru-python)
- LinkedIn: [Chandru M](https://www.linkedin.com/in/chandrum071202/)
- Email: chandrum071202@gmail.com

---

## ⭐ If You Like This Project

If you found this project useful, please consider:

- ⭐ Starring this repository
- 🍴 Forking it
- 🛠️ Improving it
- 📢 Sharing it with others

---

## 📜 License

This project is created for **educational and development purposes**.  
You can modify and extend it for learning and project development.

---
