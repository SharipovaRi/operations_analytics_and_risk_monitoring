import subprocess
import sys

scripts = [
    "src/preprocessing/clean_superstore.py",
    "src/preprocessing/clean_azure.py",
    "src/preprocessing/clean_ecommerce.py",
    "src/features/build_features.py",
    "src/database/load_postgres.py",
    "src/models/forecasting.py",
    "src/models/anomaly_detection.py",
    "src/models/statistical_analysis.py",
]

for script in scripts:
    print("\n" + "=" * 80)
    print(f"Running: {script}")
    print("=" * 80)

    subprocess.run(
        [sys.executable, script],
        check=True
    )

print("\nFull analytics pipeline completed successfully.")