import pandas as pd
from scipy.stats import ttest_ind

# Load anomaly results
df = pd.read_csv(
    "reports/anomaly_results.csv"
)

# Separate groups
normal = df[df["anomaly"] == 1]

abnormal = df[df["anomaly"] == -1]

# Perform t-test
stat, p = ttest_ind(
    normal["avg_vibration"],
    abnormal["avg_vibration"]
)

# Print results
print("T-statistic:", stat)
print("P-value:", p)

# Business interpretation
if p < 0.05:
    print(
        "\nResult: Significant difference detected."
    )

    print(
        "Anomalous machines show statistically different vibration levels."
    )

else:
    print(
        "\nResult: No statistically significant difference detected."
    )