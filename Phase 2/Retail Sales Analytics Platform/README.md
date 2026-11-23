# Retail Sales Analytics Platform

## Project Overview
This project focuses on building a Retail Sales Analytics Platform using **Databricks Lakeflow Spark Declarative Pipelines** and the **Medallion Architecture**.

The goal is to transform raw retail sales data into clean, structured, and analytics-ready datasets for business insights.

## Technologies Used
- Databricks
- SQL
- Lakeflow Spark Declarative Pipelines
- Unity Catalog
- Medallion Architecture

## Project Architecture

The project follows the three-layer Medallion Architecture:

### 1. Bronze Layer
- Ingests raw retail sales data from CSV files.
- Uses `read_files()` for data ingestion.
- Adds source file information and ingestion timestamps.
- Applies basic data quality expectations.

### 2. Silver Layer
- Cleans and standardizes the raw data.
- Trims unnecessary spaces.
- Converts data into appropriate data types.
- Handles missing and invalid records.

### 3. Gold Layer
Creates analytical tables for business reporting:

| Table | Description |
|---|---|
| `gold_monthly_sales` | Monthly sales and profit analysis |
| `gold_category_sales` | Category-wise sales performance |
| `gold_region_sales` | Region-wise sales analysis |
| `gold_segment_kpis` | Customer segment performance |
| `gold_product_sales` | Product and subcategory analysis |

## Dataset
The project uses retail sales transaction data containing information about:
- Orders and customers
- Products and categories
- Sales and profit
- Regions and customer segments
- Quantity and pricing

## Repository Structure

```text
Retail-Sales-Analytics/
│
├── Bronze_Layer.sql
├── Silver_Layer.sql
├── Gold_Layer.sql
└── README.md
```

## Key Learning Outcomes
- Understanding Medallion Architecture.
- Building data pipelines in Databricks.
- Working with Bronze, Silver, and Gold layers.
- Writing SQL transformations.
- Creating analytical datasets for business reporting.

## Author
Nikita Mandharne

**Project:** Retail Sales Analytics Platform