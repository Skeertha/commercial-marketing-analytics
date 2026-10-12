# Commercial & Marketing Analytics: Customer Segmentation, Sales Forecasting & Promotional ROI

## Project overview
This portfolio project uses a **synthetic retail sales dataset** to demonstrate a commercial analytics workflow: data validation, exploratory analysis, customer segmentation, campaign ROI, baseline sales forecasting, and dashboard reporting.

> **Data note:** The dataset is artificially generated for learning and portfolio demonstration. It does not represent a real company or real customers.

## Business questions
1. Which product categories and products contribute the most revenue and gross profit?
2. Which customer groups are most valuable based on Recency, Frequency, and Monetary value (RFM)?
3. How do promotional campaigns compare on revenue, estimated profit, and ROI?
4. What is a simple baseline forecast for monthly revenue, and how accurate is it?
5. What business actions should a commercial or marketing team consider?

## Tools
- Python: pandas, matplotlib, scikit-learn
- SQL: SQLite (works locally without installing a database server)
- Excel: pivot tables and independent validation checks
- Power BI: interactive dashboard
- GitHub: version control and project documentation

## Repository structure
```text
commercial-marketing-analytics/
├── data/
│   └── sales_campaigns.csv
├── python/
│   └── analysis.py
├── sql/
│   └── analysis_queries.sql
├── powerbi/
│   └── dashboard_build_guide.md
├── screenshots/
├── requirements.txt
└── README.md
```

## How to run the Python analysis
1. Install Python 3.10+.
2. Open a terminal in the project folder.
3. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run:
   ```bash
   python python/analysis.py
   ```
5. The script writes summary CSV files to `outputs/`.

## SQL analysis
The SQL file contains SQLite-compatible queries. You can run them in DB Browser for SQLite or use the Python script to load the CSV into a local SQLite database.

## Excel validation
Open `data/sales_campaigns.csv` in Excel. Check:
- `order_id` is unique.
- `quantity` is positive.
- `revenue` matches quantity × unit price × (1 − discount).
- No required fields are blank.
Create PivotTables for revenue by month, category, and campaign. Use these as independent checks against Python results.

## Power BI dashboard
Follow `powerbi/dashboard_build_guide.md` to import the CSV, create measures, and build the report. Save your `.pbix` file locally and add screenshots to `screenshots/`. Only commit the `.pbix` file if its size is reasonable and you want it public.

## KPI definitions
- **Revenue:** sum of net sales revenue after the row-level discount.
- **Estimated gross profit:** revenue minus estimated cost. Cost values are synthetic estimates.
- **Campaign ROI (proxy):** (campaign gross profit − estimated campaign spend) / estimated campaign spend. This starter dataset does **not** contain actual marketing spend, so the starter analysis compares revenue/profit and explicitly avoids presenting a made-up ROI as real. Add a clearly documented synthetic `campaign_spend` assumption only if you want to demonstrate the ROI formula.
- **Forecast baseline:** next-month revenue forecast using a simple seasonal-naive / moving-average baseline. It is a learning baseline, not a production forecast.

## Limitations
- Synthetic data; results are not real market evidence.
- No causal experiment or control group is included, so campaign performance does not prove that a campaign caused incremental sales.
- Campaign spend is not included in the initial data, so true promotional ROI cannot be calculated until a documented spend field is added.
- The forecast is a baseline and should be compared with stronger models before business use.

## Next improvements
- Add a documented synthetic campaign budget table.
- Compare a moving-average forecast with seasonal-naive forecasts using a time-based holdout.
- Add customer segment profiles and actionable recommendations.
- Add Power BI screenshots and a short project walkthrough video.
