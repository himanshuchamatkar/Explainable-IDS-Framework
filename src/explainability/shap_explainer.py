import shap
import pandas as pd


class IDSExplainer:

    def __init__(self, model):

        print("Initializing SHAP explainer...")

        self.model = model

        self.explainer = shap.TreeExplainer(self.model)

        print("SHAP Explainer ready.")

    def explain_prediction(self, features_dict):

        df = pd.DataFrame([features_dict])

        shap_values = self.explainer.shap_values(df)

        explanation = {}

        for i, feature in enumerate(df.columns):
            explanation[feature] = float(shap_values[0][i])

        return explanation