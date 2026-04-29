import pandas as pd
from prophet import Prophet
import json

# Load the dataset we already created
df = pd.read_csv("sme_cashflow_data.csv")

# Prophet needs exactly two columns: ds (date) and y (value)
# We will forecast the daily net cash flow (income minus expenses)
daily = df.groupby("Date")["Signed_Amount"].sum().reset_index()
daily.columns = ["ds", "y"]
daily["ds"] = pd.to_datetime(daily["ds"])

# Build and train the model
model = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    daily_seasonality=False,
    changepoint_prior_scale=0.05
)
model.fit(daily)

# Forecast 30 days into the future
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Pull out just the next 30 days
next_30 = forecast[forecast["ds"] > daily["ds"].max()][
    ["ds", "yhat", "yhat_lower", "yhat_upper"]
].copy()

next_30.columns = ["Date", "Predicted_NetCashFlow", "Lower_Bound", "Upper_Bound"]
next_30["Date"] = next_30["Date"].dt.strftime("%Y-%m-%d")
next_30["Predicted_NetCashFlow"] = next_30["Predicted_NetCashFlow"].round(2)
next_30["Lower_Bound"] = next_30["Lower_Bound"].round(2)
next_30["Upper_Bound"] = next_30["Upper_Bound"].round(2)

# Add a risk flag based on predicted cash flow
next_30["Risk_Flag"] = next_30["Predicted_NetCashFlow"].apply(
    lambda x: "OUTFLOW RISK" if x < 0 else "STABLE"
)

# Save to CSV for Power BI
next_30.to_csv("cashflow_forecast_30days.csv", index=False)

print("30-day forecast complete")
print(f"Days with OUTFLOW RISK: {(next_30['Risk_Flag'] == 'OUTFLOW RISK').sum()}")
print(f"Days STABLE: {(next_30['Risk_Flag'] == 'STABLE').sum()}")
print()
print(next_30.to_string(index=False))