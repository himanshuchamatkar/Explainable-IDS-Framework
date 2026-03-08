import joblib
import pandas as pd
import json
from datetime import datetime

from src.explainability.shap_explainer import IDSExplainer


class RealtimePredictor:

    def __init__(self):

        print("Loading trained model...")
        self.model = joblib.load("trained_models/xgboost_ids_model.pkl")
        print("Model loaded.")

        print("Initializing SHAP explainer...")
        self.explainer = IDSExplainer(self.model)
        print("SHAP Explainer ready.")

    def predict(self, features):

        X = pd.DataFrame([features])

        prediction = self.model.predict(X)[0]
        probability = self.model.predict_proba(X)[0][1]

        label = "ATTACK" if prediction == 1 else "BENIGN"

        # SHAP explanation
        shap_values = self.explainer.explain_prediction(features)

        timestamp = datetime.now().strftime("%H:%M:%S")

        result = {
            "timestamp": timestamp,
            "flow_packets": features["total_packets"],
            "prediction": label,
            "probability": float(probability),
            "explanation": shap_values
        }

        self.save_prediction(result)

        return result

    def save_prediction(self, data):

        file = "realtime_predictions.json"

        try:
            with open(file, "r") as f:
                existing = json.load(f)
        except:
            existing = []

        existing.append(data)

        with open(file, "w") as f:
            json.dump(existing, f, indent=2)