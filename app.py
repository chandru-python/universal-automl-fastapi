# ============================================
# FULL AUTOML FASTAPI SYSTEM
# Dynamic Prediction + Upload + Auth Pages
# ============================================

from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import shutil
import joblib
import numpy as np
import os

from automl_pipeline import run_automl

# ============================================
# INIT
# ============================================

app = FastAPI()

templates = Jinja2Templates(directory="templates")

MODEL_PATH = "models/best_model.pkl"
SCALER_PATH = "models/scaler.pkl"
FEATURE_PATH = "models/feature_names.pkl"


# ============================================
# LOAD FUNCTIONS
# ============================================

def load_model():
    return joblib.load(MODEL_PATH)


def load_scaler():
    return joblib.load(SCALER_PATH)


def load_features():
    return joblib.load(FEATURE_PATH)


# ============================================
# HOME
# ============================================

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


# ============================================
# ABOUT
# ============================================

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):

    return templates.TemplateResponse(
        "about.html",
        {"request": request}
    )


# ============================================
# LOGIN
# ============================================

@app.get("/login", response_class=HTMLResponse)
def login(request: Request):

    return templates.TemplateResponse(
        "login.html",
        {"request": request}
    )


# ============================================
# REGISTER
# ============================================

@app.get("/register", response_class=HTMLResponse)
def register(request: Request):

    return templates.TemplateResponse(
        "register.html",
        {"request": request}
    )


# ============================================
# UPLOAD PAGE
# ============================================

@app.get("/upload", response_class=HTMLResponse)
def upload_page(request: Request):

    return templates.TemplateResponse(
        "upload.html",
        {"request": request}
    )


# ============================================
# UPLOAD DATASET AND TRAIN
# ============================================

@app.post("/upload", response_class=HTMLResponse)
def upload_dataset(
    request: Request,
    file: UploadFile = File(...),
    target: str = Form(...)
):

    os.makedirs("uploads", exist_ok=True)

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    # RUN AUTOML TRAINING
    best_model_name, problem_type, score = run_automl(path, target)

    return templates.TemplateResponse(
        "upload.html",
        {
            "request": request,
            "model_name": best_model_name,
            "problem_type": problem_type,
            "score": round(score, 4)
        }
    )


# ============================================
# PREDICT PAGE (DYNAMIC FORM)
# ============================================

@app.get("/predict", response_class=HTMLResponse)
def predict_page(request: Request):

    if not os.path.exists(FEATURE_PATH):

        return templates.TemplateResponse(
            "predict.html",
            {
                "request": request,
                "features": [],
                "error": "No model trained yet. Upload dataset first."
            }
        )

    features = load_features()

    return templates.TemplateResponse(
        "predict.html",
        {
            "request": request,
            "features": features
        }
    )


# ============================================
# PREDICT RESULT (DYNAMIC)
# ============================================

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request):

    form = await request.form()

    model = load_model()
    scaler = load_scaler()
    features = load_features()

    values = []

    for feature in features:

        val = float(form.get(feature))
        values.append(val)

    data = np.array([values])

    data = scaler.transform(data)

    result = model.predict(data)[0]

    return templates.TemplateResponse(
        "predict.html",
        {
            "request": request,
            "features": features,
            "result": result
        }
    )
