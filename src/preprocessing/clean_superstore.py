import pandas as pd
import os

INPUT_PATH = r"data/raw/superstore/sample_superstore.csv"
OUTPUT_PATH = r"data/processed/superstore_clean.csv"

def clean_superstore():
    df = pd.read_csv(INPUT_PATH, encoding="latin1")

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Convert dates
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["ship_date"] = pd.to_datetime(df["ship_date"])

    # Feature engineering
    df["delivery_days"] = (df["ship_date"] - df["order_date"]).dt.days
    df["profit_margin"] = df["profit"] / df["sales"]

    # Remove nulls / duplicates
    df = df.drop_duplicates()
    df = df.dropna()

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)

    print("Superstore cleaned:", df.shape)

if __name__ == "__main__":
    clean_superstore()