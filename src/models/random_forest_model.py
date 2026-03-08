from sklearn.ensemble import RandomForestClassifier


class RandomForestModel:
    def __init__(self):
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=42,
            n_jobs=-1
        )

    def train(self, X_train, y_train):
        print("Training Random Forest...")
        self.model.fit(X_train, y_train)
        print("Training completed.")

    def predict(self, X_test):
        return self.model.predict(X_test)

    def get_model(self):
        return self.model