import subprocess
# python src/run_cleaning_all.py - to run this file in terminal. 
scripts = [
    "src/cleaning/clean_superstore.py",
    "src/cleaning/clean_azure.py",
    "src/cleaning/clean_ecommerce.py"
]

for script in scripts:
    print(f"Running {script}")
    subprocess.run(["python", script])