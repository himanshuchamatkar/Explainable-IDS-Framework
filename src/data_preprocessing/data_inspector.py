import numpy as np


class DataInspector:
    def __init__(self, df):
        self.df = df

    def basic_info(self):
        print("Dataset Shape:", self.df.shape)
        print("\nColumn Types:")
        print(self.df.dtypes)

    def check_missing_values(self):
        missing = self.df.isnull().sum()
        missing = missing[missing > 0]
        print("\nMissing Values:")
        print(missing)

    def check_infinite_values(self):
        numeric_df = self.df.select_dtypes(include=[np.number])
        inf_count = np.isinf(numeric_df).sum().sum()
        print(f"\nTotal Infinite Values: {inf_count}")

    def label_distribution(self):
        print("\nLabel Distribution:")
        print(self.df["Label"].value_counts())

    def check_duplicates(self):
        dup_count = self.df.duplicated().sum()
        print(f"\nDuplicate Rows: {dup_count}")