import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Load engineered features
df = pd.read_csv(
    "data/processed/machine_features.csv"
)

# Select telemetry features
X = df[[
    "avg_volt",
    "avg_rotate",
    "avg_pressure",
    "avg_vibration"
]]

# Initialize model
model = IsolationForest(
    contamination=0.05,
    random_state=42
)

# Train and predict
df["anomaly"] = model.fit_predict(X)

# Create readable labels
df["anomaly_label"] = df["anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

# Save results
df.to_csv(
    "reports/anomaly_results.csv",
    index=False
)

# Create visualization
plt.figure(figsize=(12,6))

colors = df["anomaly"].map({
    1: "blue",
    -1: "red"
})

plt.scatter(
    df["machineid"],
    df["risk_score"],
    c=colors
)

plt.xlabel("Machine ID")
plt.ylabel("Risk Score")
plt.title("Machine Risk Anomaly Detection")

# Save chart
plt.savefig(
    "reports/anomaly_plot.png"
)

print(df.head())

print("\nAnomaly counts:")
print(df["anomaly_label"].value_counts())