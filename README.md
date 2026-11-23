# 🎓 Internship Tasks

**Innomatics Research Labs: Data Analytics and Data Engineering Internship**

This repository contains my work from the internship, organised by phase.

---

## 📘 Phase 1: Foundation of Python

Python fundamentals and practice tasks.

---

## 🏗️ Phase 2: Building ETL Pipelines using Databricks and SQL

Medallion Architecture (Bronze, Silver, Gold) projects built with **Lakeflow Spark Declarative Pipelines** on Databricks. Each project takes a raw CSV with real-world data problems, cleans it, builds business-ready Gold tables and checks that no row was lost.

| # | Project | What it does | Link |
|---|---|---|---|
| 1 | **Online Learning Enrollment Analytics** | Cleans a raw course enrollments CSV (1,283 rows) into Gold tables and a 3-page AI/BI dashboard. Found 47 learners double-counted because of messy emails | [View project](https://github.com/nikk2004/Internship_Tasks/tree/main/Phase%202/Online%20Learning%20Enrollment%20Analytics%20Platform) |
| 2 | **Airline Flight Operations Analytics** | Cleans a raw airline flights CSV (1,365 rows), adds delay categories and builds Gold tables for airline, route and delay analysis | [View project](https://github.com/nikk2004/Internship_Tasks/tree/main/Phase%202/Airline%20Flight%20Operations%20Analytics%20Platform) |
| 3 | **Retail Sales Analytics** | Cleans a raw retail sales CSV (1,506 rows, 33 columns) into trusted Gold tables for sales and profit analysis | [View project](https://github.com/nikk2004/Internship_Tasks/tree/main/Phase%202/Retail%20Sales%20Analytics%20Platform) |

### 🧰 Tech Stack

| Area | Tools |
|---|---|
| Platform | Databricks |
| Pipelines | Lakeflow Spark Declarative Pipelines (SQL) |
| Storage | Unity Catalog Volumes |
| Architecture | Medallion (Bronze, Silver, Gold) |
| Dashboards | Databricks AI/BI |
| Language | SQL, Python |

### 🔑 What these projects demonstrate

- Raw data is preserved in **Bronze** so every cleaning decision can be traced
- **Silver** removes duplicates, fixes text and types, and saves invalid rows with a reason
- **Gold** answers business questions with summary tables
- **Reconciliation checks** prove that every input row is accounted for

---

## 👩‍💻 Author

**Nikita Mandharne**
[LinkedIn](https://linkedin.com/in/nikita-mandharne-10a2542b7) | [GitHub](https://github.com/nikk2004)
