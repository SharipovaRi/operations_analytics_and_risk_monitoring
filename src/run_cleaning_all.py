import subprocess
# python src/run_cleaning_all.py - to run this file in terminal. 
scripts = [
    "src/preprocessing/clean_superstore.py",
    "src/preprocessing/clean_azure.py",
    "src/preprocessing/clean_ecommerce.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(["python", script])