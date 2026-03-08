from xgboost import XGBClassifier


class XGBoostModel:

    def __init__(self):

        self.model = XGBClassifier(
            n_estimators=200,
            max_depth=8,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            tree_method="hist",
            n_jobs=-1
        )

    def train(self, X_train, y_train):

        print("Training XGBoost...")
        self.model.fit(X_train, y_train)
        print("XGBoost training completed.")

    def predict(self, X_test):

        return self.model.predict(X_test)

    def get_model(self):

        return self.model