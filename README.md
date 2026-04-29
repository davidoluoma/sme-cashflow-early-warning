# SME Cash Flow Early Warning System
### Built with Python, Prophet, and Power BI

## The Problem This Solves

Small and medium businesses in Nigeria and across Africa fail not because they are unprofitable, 
but because they run out of cash at the wrong time. There is no affordable, visual tool that tells 
a business owner "you are 3 weeks away from not being able to pay salaries." Banks do not help 
them see this. Accountants are reactive. This project fills that gap.

## What This Dashboard Does

- Tracks 12 months of income and expense transactions across 8 categories
- Calculates a running cash balance updated after every transaction
- Automatically flags every transaction as SAFE, WARNING or DANGER based on cash position
- Breaks down the top expense categories draining cash from the business
- Compares income vs expenses side by side for every month
- Forecasts the next 30 days of net cash flow using Facebook Prophet
- Flags specific future dates at OUTFLOW RISK before they happen

## Dashboard Preview

![SME Cash Flow Dashboard](dashboard_preview.png)

## Key Findings from the Data

- Total Income tracked: 328.66M NGN across 12 months
- Total Expenses tracked: 271.76M NGN across 12 months
- Closing Cash Balance: 58.36M NGN
  - The business spent 19.5% of the year in a DANGER cash zone
- Peak income months: March, April, November, December
- Slowest months: January and August
- Top expense drain: Marketing, Staff Salaries, and Rent combined

## Tools and Technologies Used

| Tool | Purpose |
|---|---|
| Python (Pandas) | Data generation, cleaning and transformation |
| Python (Prophet) | 30-day cash flow forecasting model |
| Power BI Desktop | Interactive dashboard and visualizations |
| VS Code | Development environment |

## Project Files

| File | Description |
|---|---|
| `generate_data.py` | Generates 12 months of realistic SME transaction data |
| `forecast.py` | Trains Prophet model and outputs 30-day cash flow forecast |
| `sme_cashflow_data.csv` | Full cleaned transaction dataset (365 days) |
| `cashflow_forecast_30days.csv` | 30-day forecast output with risk flags |
| `SME_CashFlow_Dashboard_DavidOluoma.pdf` | Exported Power BI dashboard |

## How to Run This Project

1. Clone the repository
2. Install dependencies:
pip install pandas prophet
3. Generate the dataset:
python generate_data.py
4. Run the forecast model:
python forecast.py
5. Open Power BI Desktop and load both CSV files to explore the dashboard

## Business Impact

A business owner using this system can:
- See their exact cash position updated in real time
- Know which months historically drain cash fastest
- Identify which expense categories to cut first in a cash crisis
- See 30 days ahead and prepare before a cash shortfall hits

## Author

**David Oluomachukwu Favour**  
Data Analyst and Data Scientist  
Portfolio: https://davidoluoma.github.io/data.html  
Email: david.oluoma.favour@gmail.com
