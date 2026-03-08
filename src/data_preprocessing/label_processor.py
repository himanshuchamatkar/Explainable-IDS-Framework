class LabelProcessor:
    def __init__(self, df):
        self.df = df.copy()

    def convert_to_binary(self):
        self.df["Label"] = self.df["Label"].apply(
            lambda x: 0 if x == "BENIGN" else 1
        )
        print("Converted labels to binary.")
        print(self.df["Label"].value_counts())

    def get_data(self):
        return self.df