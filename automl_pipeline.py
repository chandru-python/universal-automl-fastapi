# ============================================
# FULL AUTO ML PIPELINE (UNIVERSAL VERSION)
# Supports Classification + Regression
# ============================================

import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, r2_score

# Classification models
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

# Regression models
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


# ============================================
# MAIN AUTOML FUNCTION
# ============================================

def run_automl(data_path, target_column):

    print("\n====================================")
    print("AUTO ML PIPELINE STARTED")
    print("====================================")

    # ------------------------------------
    # LOAD DATASET
    # ------------------------------------

    print("\nLoading dataset...")
    df = pd.read_csv(data_path)

    print("Dataset shape:", df.shape)

    if df.shape[0] < 10:
        raise Exception("Dataset too small")

    if target_column not in df.columns:
        raise Exception("Target column not found")

    # ------------------------------------
    # HANDLE MISSING VALUES
    # ------------------------------------

    print("\nHandling missing values...")

    for col in df.columns:

        if df[col].dtype == "object":

            df[col].fillna(df[col].mode()[0], inplace=True)

        else:

            df[col].fillna(df[col].mean(), inplace=True)

    # ------------------------------------
    # ENCODE CATEGORICAL DATA
    # ------------------------------------

    print("\nEncoding categorical columns...")

    label_encoders = {}

    for col in df.columns:

        if df[col].dtype == "object":

            le = LabelEncoder()

            df[col] = le.fit_transform(df[col])

            label_encoders[col] = le

    # ------------------------------------
    # SPLIT FEATURES AND TARGET
    # ------------------------------------

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # ------------------------------------
    # DETECT PROBLEM TYPE
    # ------------------------------------

    if y.dtype == "float64":

        problem_type = "regression"

    elif y.dtype == "int64" and len(y.unique()) > 20:

        problem_type = "regression"

    else:

        problem_type = "classification"

    print("\nDetected problem type:", problem_type)

    # ------------------------------------
    # TRAIN TEST SPLIT
    # ------------------------------------

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,
        random_state=42
    )

    # ------------------------------------
    # SCALE FEATURES
    # ------------------------------------

    print("\nScaling features...")

    scaler = StandardScaler()

    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # ------------------------------------
    # SELECT MODELS
    # ------------------------------------

    if problem_type == "classification":

        models = {

            "LogisticRegression": LogisticRegression(max_iter=500),

            "RandomForestClassifier": RandomForestClassifier(),

            "SVM": SVC()

        }

        metric_function = accuracy_score
        metric_name = "accuracy"

    else:

        models = {

            "LinearRegression": LinearRegression(),

            "RandomForestRegressor": RandomForestRegressor()

        }

        metric_function = r2_score
        metric_name = "r2_score"

    # ------------------------------------
    # MLFLOW SETUP
    # ------------------------------------

    mlflow.set_experiment("AutoML")

    best_model = None
    best_score = -999999
    best_model_name = ""

    print("\nTraining models...")

    # ------------------------------------
    # TRAIN ALL MODELS
    # ------------------------------------

    for name, model in models.items():

        print("\nTraining:", name)

        with mlflow.start_run(run_name=name):

            model.fit(X_train, y_train)

            preds = model.predict(X_test)

            score = metric_function(y_test, preds)

            print(name, metric_name, ":", score)

            # log MLflow
            mlflow.log_param("model_name", name)
            mlflow.log_param("problem_type", problem_type)
            mlflow.log_metric(metric_name, score)

            mlflow.sklearn.log_model(model, name)

            # select best model
            if score > best_score:

                best_score = score
                best_model = model
                best_model_name = name


    # ------------------------------------
    # SAVE BEST MODEL (MOVE OUTSIDE LOOP)
    # ------------------------------------

    print("\n====================================")
    print("BEST MODEL:", best_model_name)
    print("BEST SCORE:", best_score)
    print("====================================")

    os.makedirs("models", exist_ok=True)

    joblib.dump(best_model, "models/best_model.pkl")

    joblib.dump(scaler, "models/scaler.pkl")

    joblib.dump(problem_type, "models/problem_type.pkl")

    joblib.dump(list(X.columns), "models/feature_names.pkl")

    joblib.dump(label_encoders, "models/label_encoders.pkl")

    print("\nSaved files:")
    print("models/best_model.pkl")
    print("models/scaler.pkl")
    print("models/problem_type.pkl")
    print("models/feature_names.pkl")
    print("models/label_encoders.pkl")

    print("\nAUTO ML PIPELINE COMPLETE")

    # RETURN MUST BE HERE (FINAL LINE)
    return best_model_name, problem_type, best_score
