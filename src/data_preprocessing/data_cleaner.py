import numpy as np


class DataCleaner:
    def __init__(self, df):
        self.df = df.copy()

    def remove_duplicates(self):
        initial_shape = self.df.shape
        self.df = self.df.drop_duplicates()
        print(f"Removed duplicates: {initial_shape[0] - self.df.shape[0]}")

    def handle_infinite_values(self):
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        self.df[numeric_cols] = self.df[numeric_cols].replace([np.inf, -np.inf], np.nan)
        print("Infinite values replaced with NaN.")

    def handle_missing_values(self):
        missing_before = self.df.isnull().sum().sum()
        print(f"Total missing before handling: {missing_before}")

        # Drop rows with any NaN
        self.df = self.df.dropna()

        missing_after = self.df.isnull().sum().sum()
        print(f"Total missing after handling: {missing_after}")

    def get_clean_data(self):
        return self.df