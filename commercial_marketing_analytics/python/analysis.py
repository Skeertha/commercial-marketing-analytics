from pathlib import Path
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "sales_campaigns.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA)
df["order_date"] = pd.to_datetime(df["order_date"], format="%d-%m-%Y", errors="raise")

# 1) Data quality checks
checks = {
    "row_count": len(df),
    "duplicate_order_ids": int(df["order_id"].duplicated().sum()),
    "missing_cells": int(df.isna().sum().sum()),
    "non_positive_quantity": int((df["quantity"] <= 0).sum()),
    "negative_revenue": int((df["revenue"] < 0).sum()),
}
pd.DataFrame([checks]).to_csv(OUT / "data_quality_checks.csv", index=False)
print("Data quality checks:", checks)

# 2) Monthly and category analysis
df["month"] = df["order_date"].dt.to_period("M").astype(str)
monthly = df.groupby("month", as_index=False).agg(
    revenue=("revenue", "sum"),
    gross_profit=("gross_profit", "sum"),
    orders=("order_id", "nunique")
)
monthly.to_csv(OUT / "monthly_kpis.csv", index=False)

category = df.groupby("category", as_index=False).agg(
    revenue=("revenue", "sum"),
    gross_profit=("gross_profit", "sum"),
    units_sold=("quantity", "sum")
).sort_values("revenue", ascending=False)
category.to_csv(OUT / "category_performance.csv", index=False)

# 3) Campaign performance
df["campaign"] = df["campaign"].fillna("No Campaign").replace("None", "No Campaign")

campaign = df.groupby("campaign", as_index=False).agg(
    revenue=("revenue", "sum"),
    gross_profit=("gross_profit", "sum"),
    orders=("order_id", "nunique"),
    average_discount=("discount_pct", "mean")
).sort_values("revenue", ascending=False)

campaign.to_csv(OUT / "campaign_performance.csv", index=False)

# 3) RFM customer segmentation
snapshot_date = df["order_date"].max() + pd.Timedelta(days=1)
rfm = df.groupby("customer_id").agg(
    last_purchase=("order_date", "max"),
    frequency=("order_id", "nunique"),
    monetary=("revenue", "sum")
).reset_index()
rfm["recency_days"] = (snapshot_date - rfm["last_purchase"]).dt.days
rfm["R_score"] = pd.qcut(rfm["recency_days"].rank(method="first"), 4, labels=[4,3,2,1]).astype(int)
rfm["F_score"] = pd.qcut(rfm["frequency"].rank(method="first"), 4, labels=[1,2,3,4]).astype(int)
rfm["M_score"] = pd.qcut(rfm["monetary"].rank(method="first"), 4, labels=[1,2,3,4]).astype(int)
def segment(row):
    if row.R_score >= 3 and row.F_score >= 3 and row.M_score >= 3:
        return "Champions"
    if row.F_score >= 3 and row.M_score >= 3:
        return "Loyal / High Value"
    if row.R_score >= 3:
        return "Recent Customers"
    if row.R_score <= 2 and row.F_score <= 2:
        return "At Risk"
    return "Potential Growth"
rfm["segment"] = rfm.apply(segment, axis=1)
rfm.to_csv(OUT / "customer_rfm_segments.csv", index=False)

# 4) Simple forecast: 3-month moving average, evaluated on last 3 months
monthly["month_date"] = pd.to_datetime(monthly["month"] + "-01")
series = monthly.set_index("month_date")["revenue"].asfreq("MS")
if len(series) >= 6:
    train, test = series.iloc[:-3], series.iloc[-3:]
    history = list(train.values)
    preds = []
    for actual in test.values:
        preds.append(sum(history[-3:]) / min(3, len(history)))
        history.append(actual)
    mae = mean_absolute_error(test.values, preds)
    forecast_eval = pd.DataFrame({
        "month": test.index.strftime("%Y-%m"),
        "actual_revenue": test.values,
        "forecast_revenue": preds,
        "absolute_error": [abs(a-p) for a,p in zip(test.values, preds)]
    })
    forecast_eval.to_csv(OUT / "forecast_holdout_evaluation.csv", index=False)
    (OUT / "forecast_mae.txt").write_text(f"3-month moving-average holdout MAE: {mae:.2f}\n", encoding="utf-8")
    future_forecast = sum(series.iloc[-3:].values) / 3
    (OUT / "next_month_baseline_forecast.txt").write_text(
        f"Baseline next-month revenue forecast: {future_forecast:.2f}\nMethod: average of the latest 3 monthly revenue values.\n",
        encoding="utf-8"
    )

# 5) Store raw data in SQLite for SQL practice
db_path = OUT / "commercial_analytics.sqlite"
with sqlite3.connect(db_path) as conn:
    df.to_sql("sales_campaigns", conn, if_exists="replace", index=False)

# 6) Simple chart
plt.figure(figsize=(10, 5))
plt.plot(monthly["month"], monthly["revenue"], marker="o")
plt.title("Monthly Revenue (Synthetic Data)")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=60, ha="right")
plt.tight_layout()
plt.savefig(OUT / "monthly_revenue.png", dpi=150)
plt.close()

print(f"Done. Outputs saved in: {OUT}")
