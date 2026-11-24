# Commercial & Marketing Analytics



**Customer Segmentation | Sales Analysis | Campaign Performance | Revenue Forecasting**



## Project Overview



This portfolio project uses a **synthetic retail sales dataset** to demonstrate an end-to-end commercial analytics workflow. It covers data validation, exploratory data analysis, customer segmentation, campaign performance analysis, baseline sales forecasting, SQL analysis, dashboard reporting, and browser automation testing.



> **Data Note:** The dataset is artificially generated for learning and portfolio demonstration. It does not represent a real company or real customers.



## Verified Project Results



- Processed 1,800 synthetic sales orders across 24 months.

- Validated order IDs, quantities, revenue, and missing values.

- Generated monthly revenue, gross profit, and order KPIs.

- Segmented 250 customers using Recency, Frequency, and Monetary (RFM) analysis into five groups.

- Analysed campaign performance, including 768 orders without campaign attribution.

- Evaluated a three-month moving-average forecast using a three-month holdout.

- Executed six Selenium browser automation tests: **6 passed, 0 failed**.



## Business Questions



1. Which product categories contribute the most revenue and gross profit?

2. Which customer groups are most valuable based on RFM analysis?

3. How do promotional campaigns compare in revenue and estimated profit?

4. How accurately does a simple baseline forecast predict monthly revenue?

5. What business actions could a commercial or marketing team consider?



## Tools and Technologies



| Area | Tools |

|---|---|

| Programming | Python |

| Data Analysis | pandas, NumPy |

| Visualization | Matplotlib, Power BI |

| Forecast Evaluation | scikit-learn |

| Database | SQLite |

| Querying | SQL |

| Spreadsheet Analysis | Microsoft Excel, PivotTables |

| Browser Automation | Selenium WebDriver |

| Testing | Pytest, pytest-html |

| Version Control | Git and GitHub |



## Repository Structure



```text

commercial-marketing-analytics/

|

|-- data/

|   |-- sales_campaigns.csv

|   |-- sales_campaigns_backup.csv

|

|-- python/

|   |-- analysis.py

|

|-- sql/

|   |-- analysis_queries.sql

|

|-- powerbi/

|   |-- dashboard_build_guide.md

|

|-- selenium_tests/

|   |-- test_browser.py

|   |-- test_dashboard.html

|   |-- requirements.txt

|   |-- artifacts/

|       |-- dashboard_screenshot.png

|       |-- test_report.html

|

|-- outputs/


|-- requirements.txt

|-- README.md

```



*Note: The structure above describes the main project components. Generated output files and optional folders may vary.*



## Python Data Analysis



The Python pipeline performs:



- Data loading and validation.

- Missing-value and duplicate checks.

- Monthly revenue and gross profit analysis.

- Product category performance analysis.

- Campaign performance analysis.

- Customer RFM segmentation.

- Baseline revenue forecasting.

- Forecast error evaluation.

- SQLite database generation.

- Monthly revenue visualization.



### How to Run



1. Install Python 3.10 or later.

2. Open a terminal in the project root directory.

3. Install dependencies:



```bash

pip install -r requirements.txt

```



4. Execute the analysis:



```bash

python python/analysis.py

```



5. Generated reports and charts are saved in the `outputs/` directory.



### Generated Outputs



| File | Description |

|---|---|

| `data_quality_checks.csv` | Data validation summary |

| `monthly_kpis.csv` | Monthly revenue, gross profit, and orders |

| `category_performance.csv` | Product category analysis |

| `campaign_performance.csv` | Campaign revenue and discount analysis |

| `customer_rfm_segments.csv` | Customer segmentation results |

| `forecast_holdout_evaluation.csv` | Actual versus forecast revenue |

| `forecast_mae.txt` | Mean Absolute Error |

| `next_month_baseline_forecast.txt` | Baseline next-month forecast |

| `commercial_analytics.sqlite` | SQLite database |

| `monthly_revenue.png` | Monthly revenue chart |



## SQL Analysis



The project includes SQLite-compatible queries for analysing:



- Sales and revenue.

- Monthly business performance.

- Product category performance.

- Campaign performance.

- Customer purchasing patterns.



Queries can be executed using DB Browser for SQLite or a Python SQLite connection.



## Excel Validation



Excel is used for independent validation of the dataset and analytical outputs.



Validation activities include:



- Checking unique order IDs.

- Checking positive quantities.

- Reviewing revenue calculations.

- Identifying missing values.

- Creating PivotTables for monthly, category, and campaign analysis.



## Power BI Dashboard



The dashboard build guide documents an interactive commercial analytics dashboard with the following planned KPI and analysis areas:



- Total Revenue.

- Total Orders.

- Average Order Value.

- Total Units Sold.

- Unique Customers.

- Total Gross Profit.

- Gross Profit Margin.

- Revenue by Category.

- Campaign Performance.

- Monthly Revenue Trend.

- Campaign, Category, and Date slicers.



Refer to `powerbi/dashboard_build_guide.md` for dashboard implementation details.



## Selenium Browser Automation



A local HTML dashboard test page is used to practise and demonstrate Selenium WebDriver automation with Python and Pytest.



### Automation Coverage



The test suite contains six automated test cases:



| Test Case | Validation |

|---|---|

| Dashboard title | Verifies dashboard heading |

| KPI values | Checks expected KPI values |

| Campaign filter | Verifies campaign selection |

| Campaign filter reset | Checks restoration of original values |

| KPI visibility | Checks KPI values are visible and non-empty |

| Screenshot capture | Saves a browser screenshot as test evidence |



### Technologies



- Selenium WebDriver

- Pytest

- pytest-html

- Google Chrome



### Installation



Create a virtual environment:



```bash

python -m venv .venv

```



Activate it in Windows PowerShell:



```powershell

.\.venv-automation\Scripts\Activate.ps1

```



Install Selenium test dependencies:



```bash

pip install -r selenium_tests/requirements.txt

```



### Execute Automation Tests



From the project root:



```bash

python -m pytest selenium_tests/test_browser.py -v

```



### Generate HTML Test Report



```bash

python -m pytest selenium_tests/test_browser.py -v --html=selenium_tests/artifacts/test_report.html --self-contained-html

```



### Latest Verified Test Results



**6 passed, 0 failed**



Execution time: 38.25 seconds.



The tests validate the local HTML dashboard fixture. They do not directly automate or interact with Power BI Desktop.



### Test Evidence



- `selenium_tests/artifacts/dashboard_screenshot.png` — Browser screenshot captured through Selenium.

- `selenium_tests/artifacts/test_report.html` — HTML test execution report.



## KPI Definitions



- **Revenue:** Sum of net sales revenue after row-level discounts.

- **Estimated Gross Profit:** Revenue minus estimated cost. Cost values are synthetic estimates.

- **Campaign ROI:** Actual ROI cannot be calculated because marketing spend data is unavailable.

- **Forecast Baseline:** Three-month moving-average forecasting approach evaluated on a time-based holdout.



## Limitations



- The dataset is synthetic and does not represent actual market performance.

- Campaign performance does not establish incremental sales or causation.

- Actual campaign spending is not included.

- Orders without campaign attribution are grouped under `No Campaign`.

- Forecasting uses a simple baseline approach rather than a production-grade predictive model.

- Selenium tests run against a local HTML test fixture, not the actual Power BI dashboard.



## Future Improvements



- Expand Selenium coverage with negative and boundary test scenarios.

- Add documented synthetic campaign budget assumptions.

- Compare multiple forecasting approaches using time-based validation.

- Develop customer segment profiles and business recommendations.

- Add verified Power BI dashboard screenshots.

- Add a project walkthrough video.



## Disclaimer



This project is developed for educational and portfolio demonstration purposes using synthetic data. All generated results are illustrative and should not be interpreted as actual business performance.
