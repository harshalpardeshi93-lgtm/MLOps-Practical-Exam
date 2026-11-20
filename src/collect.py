
import pandas as pd
from sklearn.datasets import load_wine
from pathlib import Path


def collect_data():
    wine = load_wine()

    df = pd.DataFrame(
        wine.data,
        columns=wine.feature_names
    )

    df["target"] = wine.target

    output_dir = Path("data")
    output_dir.mkdir(exist_ok=True)

    output_path = output_dir / "wine_raw.csv"
    df.to_csv(output_path, index=False)

    print("Wine dataset collected successfully!")
    print("Dataset shape:", df.shape)
    print("Target classes:", df["target"].nunique())
    print("Saved to:", output_path)


if __name__ == "__main__":
    collect_data()
