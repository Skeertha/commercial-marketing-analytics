-- SQLite queries for the sales_campaigns table
-- Run python/analysis.py once to create outputs/commercial_analytics.sqlite.

-- 1. Overall KPIs
SELECT
  COUNT(DISTINCT order_id) AS total_orders,
  COUNT(DISTINCT customer_id) AS unique_customers,
  ROUND(SUM(revenue), 2) AS total_revenue,
  ROUND(SUM(gross_profit), 2) AS estimated_gross_profit
FROM sales_campaigns;

-- 2. Monthly trend
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(SUM(gross_profit), 2) AS gross_profit,
       COUNT(DISTINCT order_id) AS orders
FROM sales_campaigns
GROUP BY month
ORDER BY month;

-- 3. Category performance
SELECT category,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(SUM(gross_profit), 2) AS estimated_gross_profit,
       SUM(quantity) AS units_sold
FROM sales_campaigns
GROUP BY category
ORDER BY revenue DESC;

-- 4. Campaign comparison (not ROI: spend is not present in the starter data)
SELECT campaign,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(SUM(gross_profit), 2) AS estimated_gross_profit,
       ROUND(AVG(discount_pct) * 100, 1) AS average_discount_pct,
       COUNT(DISTINCT order_id) AS orders
FROM sales_campaigns
GROUP BY campaign
ORDER BY estimated_gross_profit DESC;

-- 5. Customers with highest lifetime revenue
SELECT customer_id,
       COUNT(DISTINCT order_id) AS order_count,
       ROUND(SUM(revenue), 2) AS lifetime_revenue
FROM sales_campaigns
GROUP BY customer_id
ORDER BY lifetime_revenue DESC
LIMIT 20;

-- 6. Data quality: duplicate order IDs (should return no rows)
SELECT order_id, COUNT(*) AS record_count
FROM sales_campaigns
GROUP BY order_id
HAVING COUNT(*) > 1;
