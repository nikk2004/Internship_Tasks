CREATE OR REFRESH STREAMING TABLE cs_bronze_sales
(
    CONSTRAINT data_loaded
    EXPECT (orderid IS NOT NULL)
)
COMMENT 'Bronze_layer: Retail sales Data Ingestion'
AS
SELECT *,
       _metadata.file_path AS source_file,
       current_timestamp() AS ingested_at
FROM STREAM read_files(
    '/Volumes/retail_sales_sdp/default/sales_volume',
    format => 'CSV',
    header => true
);