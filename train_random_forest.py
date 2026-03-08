import pandas as pd
from src.models.data_splitter import DataSplitter
from src.models.random_forest_model import RandomForestModel
from src.evaluation.metrics import ModelEvaluator
from src.explainability.feature_importance import FeatureImportanceAnalyzer

DATA_PATH = "data/processed/cicids2017_binary.csv"

print("Loading processed dataset...")
df = pd.read_csv(DATA_PATH)

splitter = DataSplitter(df)
X_train, X_test, y_train, y_test = splitter.split()

rf = RandomForestModel()
rf.train(X_train, y_train)

model = rf.get_model()

evaluator = ModelEvaluator(model, X_test, y_test)
evaluator.evaluate()

# Feature Importance
analyzer = FeatureImportanceAnalyzer(model, X_train.columns)
importance_df = analyzer.get_importance()
from src.explainability.shap_explainer import SHAPExplainer

# Sample small subset for SHAP
X_sample = X_test.sample(2000, random_state=42)

explainer = SHAPExplainer(model)
shap_values = explainer.explain(X_sample)