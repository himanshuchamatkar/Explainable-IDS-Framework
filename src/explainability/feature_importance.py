import pandas as pd


class FeatureImportanceAnalyzer:
    def __init__(self, model, feature_names):
        self.model = model
        self.feature_names = feature_names

    def get_importance(self):
        importances = self.model.feature_importances_

        importance_df = pd.DataFrame({
            "Feature": self.feature_names,
            "Importance": importances
        })

        importance_df = importance_df.sort_values(
            by="Importance",
            ascending=False
        )

        print("\nTop 15 Important Features:")
        print(importance_df.head(15))

        return importance_df