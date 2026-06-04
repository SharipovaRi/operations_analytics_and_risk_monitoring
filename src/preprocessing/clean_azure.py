import pandas as pd
import os

# Paths

BASE = r"data/raw/azure_maintenance"
OUTPUT_BASE = r"data/processed/azure_clean"

# Raw files to process

FILES = {
    "errors": "PdM_errors.csv",
    "failures": "PdM_failures.csv",
    "maintenance": "PdM_maint.csv",
    "machines": "PdM_machines.csv",
    "telemetry": "PdM_telemetry.csv"
}

# Clean datetime

def clean_datetime(df):

    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(
            df["datetime"],
            errors="coerce"
        )

    return df


# Clean and save files
def clean_and_save(name, file):

    path = os.path.join(BASE, file)

    df = pd.read_csv(path)

    # Standardize columns

    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )

    # Convert datetime
    df = clean_datetime(df)

    # Remove duplicates
    df = df.drop_duplicates()

    # Save cleaned CSV
    out_path = os.path.join(
        OUTPUT_BASE,
        f"{name}.csv"
    )

    df.to_csv(out_path, index=False)

    print(f"[OK] {name} -> {df.shape}")


# Build telemetry features

def build_telemetry_features():

    path = os.path.join(
        BASE,
        FILES["telemetry"]
    )

    df = pd.read_csv(path)


    # Standardize columns
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
    )


    # Convert datetime
    df["datetime"] = pd.to_datetime(
        df["datetime"],
        errors="coerce"
    )


    # Machine-level telemetry features
    features = df.groupby("machineid").agg({
        "volt": "mean",
        "rotate": "mean",
        "pressure": "mean",
        "vibration": "mean"
    }).reset_index()


    # Rename columns
    features.columns = [
        "machineid",
        "avg_volt",
        "avg_rotate",
        "avg_pressure",
        "avg_vibration"
    ]


    # Save features table
    out_path = os.path.join(
        OUTPUT_BASE,
        "telemetry_features.csv"
    )

    features.to_csv(out_path, index=False)

    print(f"[OK] telemetry_features -> {features.shape}")



def run():

    # Create output folder
    os.makedirs(
        OUTPUT_BASE,
        exist_ok=True
    )


    # Clean ALL Azure files
    for name, file in FILES.items():
        clean_and_save(name, file)


    # Build engineered features
    build_telemetry_features()



if __name__ == "__main__":
    run()