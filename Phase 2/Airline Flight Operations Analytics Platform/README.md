# Airline Flight Operations Analytics Platform

End-to-end data engineering project on **Databricks** using the **Medallion Architecture**
(Bronze → Silver → Gold), built with **Lakeflow Spark Declarative Pipelines (SQL)**,
with a **Databricks AI/BI dashboard** on top of the Gold tables.

## Business problem

An airline operations team exports every domestic flight to a CSV file. The file has common
quality problems: extra spaces, inconsistent capitalisation, blank values, duplicate flights,
flights with more passengers than seats, and negative fares. On-time % and load factor were
calculated by hand, so different teams reported different numbers.

This project builds a repeatable pipeline that keeps the raw file, cleans it step by step,
creates business-ready summary tables, proves that no row was lost, and shows the results in
a dashboard.

## Architecture

```
CSV (Unity Catalog Volume)
        │
        ▼
   Bronze  ──►  Silver (clean + rejected)  ──►  Gold (5 tables)  ──►  AI/BI Dashboard
 1,365 rows         1,321 + 19 rejected            reconciliation          3 pages
```

| Layer | Table | Purpose |
|---|---|---|
| Bronze | `bronze_airline_flights` | Raw CSV as-is, plus source file name and load time |
| Silver | `silver_flights_stage` | Helper view: dedupe, cleaning and `delay_category` in one place |
| Silver | `silver_flights_clean` | Valid, deduplicated, standardised flights |
| Silver | `silver_flights_rejected` | Invalid flights saved with a `reject_reason` |
| Gold | `gold_monthly_flights` | Monthly flights, passengers, seats, load factor, revenue, fuel cost, delays |
| Gold | `gold_airline_summary` | Airline-level on-time %, load factor, average delay |
| Gold | `gold_route_summary` | Route-level flights, passengers, revenue, load factor |
| Gold | `gold_delay_summary` | Flights and average delay by delay category and reason |
| Gold | `gold_data_quality` | Problem counts and the reconciliation check |

## Data cleaning rules

| Problem | Fix | Why |
|---|---|---|
| Duplicate flights | Keep one row per `flight_id` using `ROW_NUMBER()` | `flight_id` is unique; `flight_number` repeats on many days |
| Extra spaces / mixed case | `INITCAP(TRIM(col))` | Consistent grouping in reports |
| Blank airline or delay reason | Replace with `Unknown` | Keep the row, avoid NULL groups |
| Blank delay minutes | `TIMESTAMPDIFF(MINUTE, scheduled_departure, actual_departure)` | Can be derived from the two times |
| Blank ticket revenue | `passengers * avg_fare` | Can be derived |
| Blank aircraft ID | Row kept unchanged | Revenue is still valid |
| Passengers > seats, negative fare | Moved to the rejected table | Impossible values |
| Negative delay minutes | Kept, counted as On Time | The flight left early, so it is not bad data |

### Delay category

| delay_minutes | delay_category |
|---|---|
| 15 or less (including negative) | On Time |
| 16 to 60 | Minor Delay |
| More than 60 | Major Delay |

## Key formulas

```
delay_minutes   = TIMESTAMPDIFF(MINUTE, scheduled_departure, actual_departure)
ticket_revenue  = passengers × avg_fare
load_factor_pct = SUM(passengers) × 100.0 ÷ SUM(seat_capacity)
on_time_pct     = On Time flights × 100.0 ÷ all flights
```

Load factor is calculated as total passengers ÷ total seats, not as an average of each
flight's load factor, so large and small aircraft are weighted correctly.

## Results

| Metric | Value |
|---|---|
| Bronze rows | 1,365 |
| Duplicates removed | 25 |
| Rejected rows | 19 (11 overbooked, 8 negative fare) |
| Clean rows | 1,321 |
| Reconciliation | **PASSED** (1,365 = 1,321 + 19 + 25) |

Delay split on clean flights: On Time **902**, Minor Delay **284**, Major Delay **135**
(total 1,321).

## Dashboard

Built in Databricks AI/BI on the Gold tables, 3 pages:

| Page | Visuals |
|---|---|
| Overview | KPI counters (flights, passengers, revenue, delayed flights), monthly revenue line chart, on-time % by airline |
| Airlines, Routes & Delays | Airline table, top 10 routes by revenue, flights by delay category, delayed flights by reason |
| Data Quality | Bronze / clean / rejected / duplicate counters, reconciliation result, problem counts |

![Overview](screenshots/04_dashboard_overview.png)
![Airlines, Routes and Delays](screenshots/05_dashboard_airlines_routes_delays.png)
![Data Quality](screenshots/06_dashboard_data_quality.png)

## Pipeline screenshots

![Pipeline graph](screenshots/01_pipeline_graph.png)
![Gold tables](screenshots/02_gold_tables.png)
![Reconciliation](screenshots/03_data_quality_reconciliation.png)

## Repository structure

```
├── README.md
├── data/
│   └── airline_flights_raw.csv
├── pipeline/
│   ├── bronze_airline_flights.sql
│   ├── silver_flights_clean.sql
│   ├── silver_flights_rejected.sql
│   └── gold_layer.sql
└── screenshots/
```

## How to run

1. Create the catalog `aviation_catalog`, schema `flights` and volume `raw_files`.
2. Upload `data/airline_flights_raw.csv` into `/Volumes/aviation_catalog/flights/raw_files/`.
3. Create an ETL pipeline with default catalog `aviation_catalog` and default schema `flights`.
4. Add the 4 SQL files from `pipeline/` as pipeline source files.
5. Click **Run pipeline** (the whole pipeline, not a single file).
6. Verify: `SELECT * FROM aviation_catalog.flights.gold_data_quality` should show
   `reconciliation_passed = true`.
7. Create an AI/BI dashboard on the 5 Gold tables.

## Tech stack

Databricks (Free Edition), Lakeflow Spark Declarative Pipelines, SQL, Unity Catalog Volumes,
Databricks AI/BI Dashboards

## Dataset

Synthetic dataset created for learning (not real airline data): 1,365 rows, 20 columns,
domestic flights in 2025, five airline brands across ten Indian cities.

## Author

Nikita Mandharne
[LinkedIn](https://www.linkedin.com/in/nikita-mandharne-10a2542b7) · [GitHub](https://github.com/nikk2004)