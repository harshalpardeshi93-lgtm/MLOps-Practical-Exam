
import pandas as pd
from pathlib import Path


def engineer_features():
    input_path = Path("data/wine_cleaned.csv")
    output_path = Path("data/wine_features.csv")

    df = pd.read_csv(input_path)

    # Create new features
    df["alcohol_to_malic_ratio"] = (
        df["alcohol"] / (df["malic_acid"] + 1e-8)
    )

    df["total_phenols_flavonoids"] = (
        df["total_phenols"] + df["flavanoids"]
    )

    df["color_hue_interaction"] = (
        df["color_intensity"] * df["hue"]
    )

    # Save engineered dataset
    df.to_csv(output_path, index=False)

    print("Feature engineering completed!")
    print("Dataset shape:", df.shape)
    print("New features created:")
    print("- alcohol_to_malic_ratio")
    print("- total_phenols_flavonoids")
    print("- color_hue_interaction")
    print("Saved to:", output_path)


if __name__ == "__main__":
    engineer_features()
