
import pandas as pd
from pathlib import Path


def validate_data():
    file_path = Path("data/wine_features.csv")
    report_path = Path("data/validation_report.txt")

    df = pd.read_csv(file_path)

    print("Starting data validation...")

    assert not df.empty, "Dataset is empty!"
    assert df.isnull().sum().sum() == 0, "Missing values found!"
    assert df.duplicated().sum() == 0, "Duplicate records found!"
    assert "target" in df.columns, "Target column missing!"
    assert df["target"].nunique() == 3, "Expected 3 target classes!"

    required_features = [
        "alcohol_to_malic_ratio",
        "total_phenols_flavonoids",
        "color_hue_interaction"
    ]

    for feature in required_features:
        assert feature in df.columns, f"{feature} missing!"

    report = (
        "Data validation completed successfully!\n"
        f"Total records: {len(df)}\n"
        f"Total columns: {len(df.columns)}\n"
        f"Missing values: {df.isnull().sum().sum()}\n"
        f"Duplicate records: {df.duplicated().sum()}\n"
        f"Target classes: {sorted(df['target'].unique())}\n"
    )

    report_path.write_text(report, encoding="utf-8")

    print(report)
    print("Validation report saved:", report_path)


if __name__ == "__main__":
    validate_data()

