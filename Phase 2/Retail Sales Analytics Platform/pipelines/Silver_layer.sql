CREATE OR REFRESH MATERIALIZED VIEW cs_silver_sales
(
    CONSTRAINT valid_order_id
    EXPECT (order_id IS NOT NULL)
)
COMMENT 'Silver Layer: Data Transformation'
AS
SELECT
    TRIM(OrderID) AS order_id,
    OrderDate AS order_date,
    ShipDate AS ship_date,
    TRIM(ShipMode) AS ship_mode,
    source_file,
    ingested_at
FROM cs_bronze_sales;