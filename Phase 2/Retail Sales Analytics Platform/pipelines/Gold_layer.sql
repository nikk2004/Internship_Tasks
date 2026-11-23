CREATE OR REFRESH MATERIALIZED VIEW gold_monthly_sales
COMMENT "Gold layer: Monthly sales and profit analysis"
AS
SELECT
    date_format(order_date, 'yyyy-MM') AS sales_month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity,
    COUNT(DISTINCT order_id) AS total_orders
FROM silver_sales_clean
GROUP BY date_format(order_date, 'yyyy-MM');

CREATE OR REFRESH MATERIALIZED VIEW gold_category_sales
COMMENT "Gold layer: Category-wise sales and profit"
AS
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM silver_sales_clean
GROUP BY category;
CREATE OR REFRESH MATERIALIZED VIEW gold_region_sales
COMMENT "Gold layer: Region-wise sales and profit"
AS
SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(DISTINCT order_id) AS total_orders
FROM silver_sales_clean
GROUP BY region;
CREATE OR REFRESH MATERIALIZED VIEW gold_segment_kpis
COMMENT "Gold layer: Customer segment performance"
AS
SELECT
    segment,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    COUNT(DISTINCT customer_id) AS total_customers,
    COUNT(DISTINCT order_id) AS total_orders
FROM silver_sales_clean
GROUP BY segment;
CREATE OR REFRESH MATERIALIZED VIEW gold_product_sales
COMMENT "Gold layer: Product-wise sales and profit"
AS
SELECT
    category,
    sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    SUM(quantity) AS total_quantity
FROM silver_sales_clean
GROUP BY category, sub_category;