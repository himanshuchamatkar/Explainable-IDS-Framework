import pandas as pd
import numpy as np

print("Loading dataset...")

df = pd.read_csv("data/processed/cicids2017_binary.csv")

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nLabel distribution:")
print(df["Label"].value_counts())

print("\nChecking for missing values...")
print(df.isnull().sum().sum(), "missing values")

print("\nChecking for infinite values...")
print(np.isinf(df.select_dtypes(include=[float, int])).sum().sum(), "infinite values")

print("\nDone.")