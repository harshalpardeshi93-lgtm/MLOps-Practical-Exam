import pandas as pd
from sklearn.datasets import load_wine

data = load_wine()

df = pd.DataFrame(data.data, columns=data.feature_names)
df["target"] = data.target

df.to_csv("data/dataset.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
print("Shape:", df.shape)
