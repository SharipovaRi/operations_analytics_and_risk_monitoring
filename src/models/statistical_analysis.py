import os
import pandas as pd
from scipy.stats import ttest_ind

df = pd.read_csv("reports/anomaly_results.csv")

normal = df[df["anomaly"] == 1]
abnormal = df[df["anomaly"] == -1]

stat, p = ttest_ind(
    normal["avg_vibration"],
    abnormal["avg_vibration"],
    equal_var=False
)

if p < 0.05:
    interpretation = (
        "Result: Significant difference detected.\n"
        "Anomalous machines show statistically different vibration levels."
    )
else:
    interpretation = (
        "Result: No statistically significant difference detected.\n"
        "Anomalous machines do not show statistically different vibration levels."
    )

output = f"""
Statistical Analysis: Normal vs Anomalous Machines

Test:
Independent two-sample t-test

Metric:
Average vibration

T-statistic:
{stat:.4f}

P-value:
{p:.6f}

Interpretation:
{interpretation}
"""

os.makedirs("reports", exist_ok=True)

with open("reports/statistical_analysis_results.txt", "w") as f:
    f.write(output)

print(output)
print("Statistical analysis saved to reports/statistical_analysis_results.txt")