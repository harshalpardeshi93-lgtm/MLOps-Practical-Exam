
import pandas as pd
from pathlib import Path


def preprocess_data():
    input_path = Path("data/wine_raw.csv")
    output_path = Path("data/wine_cleaned.csv")

    # Load raw dataset
    df = pd.read_csv(input_path)

    print("Original dataset shape:", df.shape)

    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    # Standardize column names
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Add unique wine ID
    df.insert(0, "wine_id", range(1, len(df) + 1))

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    print("\nPreprocessing completed successfully!")
    print("Cleaned dataset shape:", df.shape)
    print("Missing values:", df.isnull().sum().sum())
    print("Duplicate records:", df.duplicated().sum())
    print("Saved to:", output_path)


if __name__ == "__main__":
    preprocess_data()
