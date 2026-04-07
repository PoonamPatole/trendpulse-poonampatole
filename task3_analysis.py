import pandas as pd
import numpy as np

# Load your CSV
df = pd.read_csv("data/trends_clean.csv")

# --- Basic Exploration ---
print(df.shape, "\n")
print(df.head())
print(df.info())
print("\nSummary stats:\n", df.describe())

# --- Patterns / Insights ---
print("\nAverage score:", np.mean(df["score"]))
print("Max score:", np.max(df["score"]))
print("Min score:", np.min(df["score"]))

# --- Save new CSV (Task 4 output) ---
df.to_csv("data/trends_anaylised.csv", index=False)

print("\nNew file created: data/trends_anaylised.csv")
