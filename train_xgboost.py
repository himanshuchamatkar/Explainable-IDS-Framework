import pandas as pd

from src.models.data_splitter import DataSplitter
from src.models.xgboost_model import XGBoostModel
from src.evaluation.metrics import ModelEvaluator


DATA_PATH = "data/processed/cicids2017_binary.csv"

print("Loading processed dataset...")
df = pd.read_csv(DATA_PATH)

# Train/Test split
splitter = DataSplitter(df)
X_train, X_test, y_train, y_test = splitter.split()

# Train XGBoost
xgb = XGBoostModel()
xgb.train(X_train, y_train)

model = xgb.get_model()

# Evaluate
evaluator = ModelEvaluator(model, X_test, y_test)
evaluator.evaluate()

import joblib

joblib.dump(model, "trained_models/xgboost_ids_model.pkl")

print("Model saved to trained_models/xgboost_ids_model.pkl")