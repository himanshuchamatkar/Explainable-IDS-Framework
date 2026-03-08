import os
import pandas as pd


class CICIDSDataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def list_csv_files(self):
        files = [
            os.path.join(self.data_path, file)
            for file in os.listdir(self.data_path)
            if file.endswith(".csv")
        ]
        return files

    def load_all_data(self):
        csv_files = self.list_csv_files()
        dataframes = []

        print(f"Found {len(csv_files)} CSV files.")

        for file in csv_files:
            print(f"Loading: {os.path.basename(file)}")
            df = pd.read_csv(file)
            dataframes.append(df)

        combined_df = pd.concat(dataframes, ignore_index=True)
        # Clean column names (remove leading/trailing spaces)
        combined_df.columns = combined_df.columns.str.strip()

        print("All files loaded and combined successfully.")
        print(f"Final dataset shape: {combined_df.shape}")

        return combined_df