import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

failures = pd.read_csv(
    "data/processed/azure_clean/failures.csv"
)

failures["datetime"] = pd.to_datetime(
    failures["datetime"]
)

# Daily failures
daily_failures = failures.groupby(
    failures["datetime"].dt.date
).size().reset_index()

daily_failures.columns = ["ds", "y"]

daily_failures["ds"] = pd.to_datetime(
    daily_failures["ds"]
)

# Train model
model = Prophet()

model.fit(daily_failures)

# Future dates
future = model.make_future_dataframe(
    periods=30
)

forecast = model.predict(future)

# Save forecast
forecast.to_csv(
    "reports/failure_forecast.csv",
    index=False
)

# Plot
fig = model.plot(forecast)

plt.savefig(
    "reports/failure_forecast.png"
)

print("Forecast complete")