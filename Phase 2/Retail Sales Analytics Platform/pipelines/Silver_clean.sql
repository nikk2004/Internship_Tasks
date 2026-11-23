
CREATE OR REFRESH MATERIALIZED VIEW silver_sales_clean
COMMENT "Silver layer: cleaned and standardized retail sales data"
AS
SELECT
    TRIM(OrderID) AS order_id,
    TRY_CAST(OrderDate AS DATE) AS order_date,
    TRIM(CustomerID) AS customer_id,
    TRIM(CustomerSegment) AS segment,
    TRIM(Region) AS region,
    TRIM(ProductCategory) AS category,
    TRIM(ProductSubCategory) AS sub_category,
    TRY_CAST(Quantity AS INT) AS quantity,
    TRY_CAST(Sales AS DOUBLE) AS sales,
    TRY_CAST(Profit AS DOUBLE) AS profit
FROM cs_bronze_sales
WHERE OrderID IS NOT NULL
  AND OrderDate IS NOT NULL;
