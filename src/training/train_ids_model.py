import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

print("Loading dataset...")

df = pd.read_csv("data/processed/cicids2017_binary.csv")

print("Dataset shape:", df.shape)

# -------- Feature Engineering -------- #

df["flow_duration"] = df["Flow Duration"]

df["total_packets"] = df["Total Fwd Packets"] + df["Total Backward Packets"]

df["total_bytes"] = df["Total Length of Fwd Packets"] + df["Total Length of Bwd Packets"]

df["packet_length_mean"] = df["Packet Length Mean"]

df["packet_length_std"] = df["Packet Length Std"]

df["packets_per_sec"] = df["Flow Packets/s"]

df["bytes_per_sec"] = df["Flow Bytes/s"]

features = [
    "flow_duration",
    "total_packets",
    "total_bytes",
    "packet_length_mean",
    "packet_length_std",
    "packets_per_sec",
    "bytes_per_sec"
]

X = df[features]

y = df["Label"]

print("\nLabel distribution:")
print(y.value_counts())

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining XGBoost multi-class model...")

model = XGBClassifier(
    n_estimators=120,
    max_depth=6,
    learning_rate=0.1,
    objective="multi:softprob",
    eval_metric="mlogloss"
)

model.fit(X_train, y_train)

print("\nEvaluating model...\n")

preds = model.predict(X_test)

print(classification_report(y_test, preds))

print("Saving model...")

joblib.dump(model, "trained_models/xgboost_ids_model.pkl")

print("Model saved.")