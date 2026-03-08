from sklearn.model_selection import train_test_split


class DataSplitter:
    def __init__(self, df):
        self.df = df

    def split(self, test_size=0.2, random_state=42):
        X = self.df.drop("Label", axis=1)
        y = self.df["Label"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state,
            stratify=y
        )

        print("Train shape:", X_train.shape)
        print("Test shape:", X_test.shape)

        return X_train, X_test, y_train, y_test