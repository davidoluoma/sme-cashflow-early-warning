import pandas as pd
import random
from datetime import date, timedelta

random.seed(42)

categories_income = [
    "Product Sales", "Bulk Order Payment", "Advance Payment", "Loan Received"
]

categories_expense = [
    "Supplier Payment", "Staff Salaries", "Rent", "Logistics / Delivery",
    "Utilities", "Marketing", "Loan Repayment", "Miscellaneous"
]

records = []
start_date = date(2024, 1, 1)

for i in range(365):
    current_date = start_date + timedelta(days=i)
    month = current_date.month

    if month in [1, 8]:
        income_multiplier = 0.6
    elif month in [3, 4, 11, 12]:
        income_multiplier = 1.4
    else:
        income_multiplier = 1.0

    num_income = random.randint(1, 3)
    for _ in range(num_income):
        amount = round(random.uniform(50000, 800000) * income_multiplier, 2)
        records.append({
            "Date": current_date,
            "Transaction_Type": "Income",
            "Category": random.choice(categories_income),
            "Amount_NGN": amount,
            "Description": "Customer payment received",
            "Month": current_date.strftime("%B"),
            "Week": current_date.isocalendar()[1]
        })

    num_expense = random.randint(1, 4)
    for _ in range(num_expense):
        if current_date.day >= 25:
            expense_multiplier = 1.8
        else:
            expense_multiplier = 1.0
        amount = round(random.uniform(20000, 500000) * expense_multiplier, 2)
        records.append({
            "Date": current_date,
            "Transaction_Type": "Expense",
            "Category": random.choice(categories_expense),
            "Amount_NGN": amount,
            "Description": "Business expense paid",
            "Month": current_date.strftime("%B"),
            "Week": current_date.isocalendar()[1]
        })

df = pd.DataFrame(records)
df = df.sort_values("Date").reset_index(drop=True)

df["Signed_Amount"] = df.apply(
    lambda row: row["Amount_NGN"] if row["Transaction_Type"] == "Income" else -row["Amount_NGN"],
    axis=1
)
df["Running_Balance_NGN"] = df["Signed_Amount"].cumsum()

df["Cash_Alert"] = df["Running_Balance_NGN"].apply(
    lambda x: "DANGER" if x < 500000 else ("WARNING" if x < 1500000 else "SAFE")
)

df.to_csv("sme_cashflow_data.csv", index=False)
print(f"Dataset created: {len(df)} transactions across 12 months")
print(df[["Date", "Transaction_Type", "Category", "Amount_NGN", "Running_Balance_NGN", "Cash_Alert"]].head(10))