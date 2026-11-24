# Power BI dashboard build guide

## 1. Import data
1. Open Power BI Desktop.
2. Select **Get data -> Text/CSV**.
3. Select `data/sales_campaigns.csv`.
4. Confirm `order_date` is Date, quantity is Whole number, and monetary columns are Decimal number.
5. Select **Load**.

## 2. Create measures (Modeling -> New measure)
```DAX
Total Revenue = SUM(sales_campaigns[revenue])

Estimated Gross Profit = SUM(sales_campaigns[gross_profit])

Total Orders = DISTINCTCOUNT(sales_campaigns[order_id])

Unique Customers = DISTINCTCOUNT(sales_campaigns[customer_id])

Units Sold = SUM(sales_campaigns[quantity])

Average Order Value = DIVIDE([Total Revenue], [Total Orders])

Gross Profit Margin % = DIVIDE([Estimated Gross Profit], [Total Revenue])
```

## 3. Suggested one-page report
- KPI cards: Total Revenue, Estimated Gross Profit, Total Orders, Unique Customers, Average Order Value.
- Line chart: `order_date` by month on the X-axis and Total Revenue on the Y-axis.
- Bar chart: category by Total Revenue.
- Bar/column chart: campaign by Estimated Gross Profit.
- Table: product name, units sold, revenue, gross profit.
- Slicers: date, category, campaign.

## 4. Customer segment page
Import `outputs/customer_rfm_segments.csv` after running the Python script. Build:
- Bar chart: count of customers by segment.
- Table: customer ID, recency days, frequency, monetary, segment.
- Cards: customer count and monetary value by segment.

## 5. Forecast page
Use `outputs/forecast_holdout_evaluation.csv` to plot actual vs forecast revenue for the holdout months. Show the MAE from `outputs/forecast_mae.txt`. Clearly label this as a simple 3-month moving-average baseline.

## 6. Campaign ROI: important data limitation
The starter dataset has no campaign spend. Therefore, do not label campaign revenue or profit as ROI. To calculate ROI, add a separate, clearly documented synthetic campaign spend table and define the formula:
`Campaign ROI % = DIVIDE([Incremental Profit] - [Campaign Spend], [Campaign Spend])`
A defensible incremental profit requires a baseline/control comparison; if you only use total profit, call the result a **profit-to-spend proxy**, not causal campaign ROI.

## 7. Save evidence for GitHub
Save the report as `commercial_marketing_analytics.pbix` locally. Export screenshots or images of the report to `screenshots/` and reference them in the README.
