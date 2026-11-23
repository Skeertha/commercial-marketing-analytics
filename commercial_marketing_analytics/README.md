\# Commercial \& Marketing Analytics: Customer Segmentation, Sales Forecasting \& Promotional ROI



\## Project Overview



This portfolio project uses a \*\*synthetic retail sales dataset\*\* to demonstrate a commercial analytics workflow, including data validation, exploratory analysis, customer segmentation, campaign performance analysis, baseline sales forecasting, and dashboard reporting.



> \*\*Data Note:\*\* The dataset is artificially generated for learning and portfolio demonstration. It does not represent a real company or real customers.



\## Business Questions



1\. Which product categories and products contribute the most revenue and gross profit?

2\. Which customer groups are most valuable based on Recency, Frequency, and Monetary value (RFM)?

3\. How do promotional campaigns compare on revenue and estimated profit?

4\. What is a simple baseline forecast for monthly revenue, and how accurate is it?

5\. What business actions should a commercial or marketing team consider?



\## Tools and Technologies



\- \*\*Python:\*\* pandas, matplotlib, scikit-learn

\- \*\*SQL:\*\* SQLite

\- \*\*Excel:\*\* PivotTables and independent validation

\- \*\*Power BI:\*\* Interactive dashboard and KPI reporting

\- \*\*Selenium WebDriver:\*\* Browser automation

\- \*\*Pytest:\*\* Automated test execution and assertions

\- \*\*pytest-html:\*\* HTML test reporting

\- \*\*Git and GitHub:\*\* Version control and documentation



\## Repository Structure



```text

commercial-marketing-analytics/

│

├── data/

│   └── sales\_campaigns.csv

│

├── python/

│   └── analysis.py

│

├── sql/

│   └── analysis\_queries.sql

│

├── powerbi/

│   └── dashboard\_build\_guide.md

│

├── selenium\_tests/

│   ├── test\_browser.py

│   ├── test\_dashboard.html

│   ├── requirements.txt

│   └── artifacts/

│       ├── dashboard\_screenshot.png

│       └── test\_report.html

│

├── screenshots/

├── requirements.txt

└── README.md

```



\## Python Data Analysis



The Python analysis demonstrates:



\- Data loading and validation

\- Exploratory data analysis

\- Customer segmentation

\- Campaign performance analysis

\- Baseline sales forecasting



\### How to Run



1\. Install Python 3.10 or later.

2\. Open a terminal in the project folder.

3\. Install dependencies:



```bash

pip install -r requirements.txt

```



4\. Run the analysis:



```bash

python python/analysis.py

```



5\. The script writes summary CSV files to `outputs/`.



\## SQL Analysis



The SQL file contains SQLite-compatible queries for analysing sales, revenue, product categories, and campaign performance.



Queries can be executed using DB Browser for SQLite or through a Python SQLite connection.



\## Excel Validation



Open `data/sales\_campaigns.csv` in Excel and validate:



\- Unique `order\_id` values

\- Positive quantities

\- Revenue calculations

\- Required fields and missing values



Create PivotTables for revenue by month, category, and campaign to independently validate analysis results.



\## Power BI Dashboard



The interactive dashboard includes:



\- Total Revenue

\- Total Orders

\- Average Order Value

\- Total Units Sold

\- Unique Customers

\- Total Gross Profit

\- Gross Profit Margin

\- Revenue by Category

\- Campaign Performance

\- Monthly Revenue Trend

\- Campaign, Category, and Date slicers



The dashboard was validated against independent Excel calculations.



\## Selenium Browser Automation



A local browser-based dashboard test page was created to practise and demonstrate Selenium WebDriver automation with Python and Pytest.



\### Automation Coverage



The test suite includes six automated test cases:



| Test Case | Validation |

|---|---|

| Dashboard title | Verifies dashboard heading |

| KPI values | Checks expected KPI values |

| Campaign filter | Verifies campaign selection |

| Campaign filter reset | Checks restoration of original values |

| KPI visibility | Checks that KPI values are visible and non-empty |

| Screenshot capture | Saves a browser screenshot as test evidence |



\### Technologies



\- Selenium WebDriver 4.54.0

\- Pytest 9.2.0

\- pytest-html 4.2.0

\- Google Chrome



\### Installation



Create and activate a virtual environment, then install the test dependencies:



```bash

python -m venv .venv

```



Windows PowerShell:



```powershell

.\\.venv\\Scripts\\Activate.ps1

```



Install the packages:



```bash

pip install -r selenium\_tests/requirements.txt

```



\### Execute Automation Tests



From the project root, run:



```bash

python -m pytest selenium\_tests/test\_browser.py -v

```



\### Generate HTML Test Report



```bash

python -m pytest selenium\_tests/test\_browser.py -v --html=selenium\_tests/artifacts/test\_report.html --self-contained-html

```



\### Test Results



\*\*Latest verified local execution: 6 passed, 0 failed.\*\*



The test suite validates the local HTML test fixture. It does not directly automate or interact with Power BI Desktop.



\### Test Evidence



\- `selenium\_tests/artifacts/dashboard\_screenshot.png` – Browser screenshot captured through Selenium.

\- `selenium\_tests/artifacts/test\_report.html` – HTML test execution report.



\## KPI Definitions



\- \*\*Revenue:\*\* Sum of net sales revenue after row-level discounts.

\- \*\*Estimated Gross Profit:\*\* Revenue minus estimated cost. Cost values are synthetic estimates.

\- \*\*Campaign ROI:\*\* Cannot be calculated as actual ROI without marketing spend data.

\- \*\*Forecast Baseline:\*\* A simple seasonal-naive or moving-average forecast for learning and comparison.



\## Limitations



\- The dataset is synthetic and does not represent actual market performance.

\- Campaign performance does not prove incremental sales or causation.

\- Actual campaign spending is not included.

\- Forecasting uses a baseline approach rather than a production-grade model.

\- Selenium tests run against a local HTML test fixture, not the Power BI Desktop application.



\## Future Improvements



\- Expand Selenium coverage with additional filter and negative test scenarios.

\- Add documented synthetic campaign budget assumptions.

\- Compare forecasting approaches using a time-based holdout.

\- Add customer segment profiles and business recommendations.

\- Add Power BI screenshots and a project walkthrough video.



