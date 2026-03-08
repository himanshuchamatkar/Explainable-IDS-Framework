from src.data_preprocessing.data_loader import CICIDSDataLoader
from src.data_preprocessing.data_cleaner import DataCleaner
from src.data_preprocessing.label_processor import LabelProcessor

DATA_PATH = "data/raw"
OUTPUT_PATH = "data/processed/cicids2017_binary.csv"

# Load
loader = CICIDSDataLoader(DATA_PATH)
df = loader.load_all_data()

# Clean
cleaner = DataCleaner(df)
cleaner.remove_duplicates()
cleaner.handle_infinite_values()
cleaner.handle_missing_values()
cleaned_df = cleaner.get_clean_data()

# Label processing
processor = LabelProcessor(cleaned_df)
processor.convert_to_binary()
final_df = processor.get_data()

# Save processed dataset
final_df.to_csv(OUTPUT_PATH, index=False)

print(f"Processed dataset saved to {OUTPUT_PATH}")
print("Final shape:", final_df.shape)