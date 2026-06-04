import pandas as pd

telemetry = pd.read_csv(
    "data/processed/azure_clean/telemetry.csv"
)

failures = pd.read_csv(
    "data/processed/azure_clean/failures.csv"
)

maintenance = pd.read_csv(
    "data/processed/azure_clean/maintenance.csv"
)

# Convert datetime
telemetry["datetime"] = pd.to_datetime(
    telemetry["datetime"]
)

# Aggregate telemetry metrics
machine_features = telemetry.groupby("machineid").agg({
    "volt": "mean",
    "rotate": "mean",
    "pressure": "mean",
    "vibration": "mean"
}).reset_index()

# Rename columns
machine_features.columns = [
    "machineid",
    "avg_volt",
    "avg_rotate",
    "avg_pressure",
    "avg_vibration"
]

# Failure counts
failure_counts = failures.groupby(
    "machineid"
).size().reset_index(name="failure_count")

# Maintenance counts
maintenance_counts = maintenance.groupby(
    "machineid"
).size().reset_index(name="maintenance_count")

# Merge everything
features = machine_features.merge(
    failure_counts,
    on="machineid",
    how="left"
)

features = features.merge(
    maintenance_counts,
    on="machineid",
    how="left"
)

# Fill missing
features = features.fillna(0)

# Create risk score
features["risk_score"] = (
    features["avg_vibration"] * 0.4 +
    features["avg_pressure"] * 0.3 +
    features["failure_count"] * 0.3
)

# Save
features.to_csv(
    "data/processed/machine_features.csv",
    index=False
)

print(features.head())