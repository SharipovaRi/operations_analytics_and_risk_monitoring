import pandas as pd
import os

INPUT_FILES = [
    r"data/raw/ecommerce_behavior/2019_Oct.csv",
    r"data/raw/ecommerce_behavior/2019_Nov.csv"
]

OUTPUT_PATH = r"data/processed/ecommerce_clean.csv"

def clean_ecommerce():
    dfs = []

    for file in INPUT_FILES:
        print("Loading:", file)

        df = pd.read_csv(file)

        # Sample 
        df = df.sample(500000, random_state=42)

        # Datetime conversion
        df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")

        dfs.append(df)

    full_df = pd.concat(dfs)

    # Cleanup
    full_df = full_df.drop_duplicates()
    full_df = full_df.dropna(subset=["event_time", "event_type"])

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    full_df.to_csv(OUTPUT_PATH, index=False)

    print("Ecommerce cleaned:", full_df.shape)

if __name__ == "__main__":
    clean_ecommerce()