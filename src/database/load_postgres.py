from sqlalchemy import create_engine
from urllib.parse import quote_plus
import pandas as pd

password = quote_plus("password")

engine = create_engine(
    f"postgresql://postgres:{password}@localhost:5433/analytics_db"
)
# Load Superstore data 
superstore = pd.read_csv(
    "data/processed/superstore_clean.csv"
)

superstore.columns = (
    superstore.columns
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

superstore.to_sql(
    "superstore_orders",
    engine,
    if_exists="replace",
    index=False
)

print("Superstore loaded!")

# Load ecommerce data
ecommerce = pd.read_csv(
    "data/processed/ecommerce_clean.csv"
)

ecommerce.to_sql(
    "ecommerce_events",
    engine,
    if_exists="replace",
    index=False
)

print("Ecommerce loaded!")

#Load azure data

azure_tables = {
    "machines": "data/processed/azure_clean/machines.csv",
    "telemetry": "data/processed/azure_clean/telemetry_features.csv",
    "failures": "data/processed/azure_clean/failures.csv",
    "errors": "data/processed/azure_clean/errors.csv",
    "maintenance": "data/processed/azure_clean/maintenance.csv"
}

for table_name, path in azure_tables.items():

    df = pd.read_csv(path)

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"{table_name} loaded!")


machine_features = pd.read_csv(
    "data/processed/machine_features.csv"
)

machine_features.to_sql(
    "machine_features",
    engine,
    if_exists="replace",
    index=False
)
print("Machine features loaded!")