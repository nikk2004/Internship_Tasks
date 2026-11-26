# 🎓 Internship Tasks
Innomatics Research Labs: Data Analytics and Data Engineering Internship

This repository contains my work from the internship, organised by phase.

## 📘 Phase 1: Foundation of Python
Python fundamentals and practice tasks.

## 🏗️ Phase 2: Building ETL Pipelines using Databricks and SQL
Medallion Architecture (Bronze, Silver, Gold) projects built with Lakeflow Spark Declarative Pipelines on Databricks. Each project takes a raw CSV with real-world data problems, cleans it, builds business-ready Gold tables and checks that no row was lost.

| # | Project | What it does | Link |
|---|---------|--------------|------|
| 1 | Online Learning Enrollment Analytics | Cleans a raw course enrollments CSV (1,283 rows) into Gold tables and a 3-page AI/BI dashboard. Found 47 learners double-counted because of messy emails | [View project](https://github.com/nikk2004/Internship_Tasks/tree/main/Phase%202/Online%20Learning%20Enrollment%20Analytics%20Platform) |
| 2 | Airline Flight Operations Analytics | Cleans a raw airline flights CSV (1,365 rows), adds delay categories and builds Gold tables for airline, route and delay analysis | [View project](https://github.com/nikk2004/Internship_Tasks/tree/main/Phase%202/Airline%20Flight%20Operations%20Analytics%20Platform) |
| 3 | Retail Sales Analytics | Cleans a raw retail sales CSV (1,506 rows, 33 columns) into trusted Gold tables for sales and profit analysis | [View project](https://github.com/nikk2004/Internship_Tasks/tree/main/Phase%202/Retail%20Sales%20Analytics%20Platform) |

## 🌐 Phase 3: Real-Time Industry Use Cases & Projects
End-to-end business intelligence projects built the way a BI Analyst works on the job: raw transactional data → cleaning → data model → KPIs → dashboards → insights and recommendations.

| # | Project | What it does | Link |
|---|---------|--------------|------|
| 1 | E-Commerce Sales, Customer & Product Analytics | Takes raw e-commerce data (Customers, Products, Orders, Order Items) through Power Query cleaning, a star-schema data model with a Date table, and DAX KPIs. Delivers 6 Power BI dashboards (Sales, Customer, Product & Category, Orders & Payment, Customer Value & Retention, Executive Summary) with business insights and recommendations | [View project](https://github.com/nikk2004/Internship_Tasks/tree/main/Phase%203/E-Commerce%20Sales%20Data%20Engineering%20Pipeline%20project) |

## 🧰 Tech Stack
| Area | Tools |
|------|-------|
| Platform | Databricks, Power BI Desktop |
| Pipelines | Lakeflow Spark Declarative Pipelines (SQL) |
| Storage | Unity Catalog Volumes |
| Architecture | Medallion (Bronze, Silver, Gold) |
| Data Preparation | Power Query |
| Data Modeling & Measures | Star schema, DAX |
| Dashboards | Databricks AI/BI, Power BI |
| Language | SQL, Python, DAX |

## 🔑 What these projects demonstrate
- Raw data is preserved in Bronze so every cleaning decision can be traced
- Silver removes duplicates, fixes text and types, and saves invalid rows with a reason
- Gold answers business questions with summary tables
- Reconciliation checks prove that every input row is accounted for
- Raw business data can be profiled, cleaned in Power Query and modeled into relationships that don't inflate totals
- KPIs (revenue, AOV, repeat rate, cancellation rate) are defined with DAX and turned into objective-based dashboards
- Dashboards answer *what happened → why → what should the business do*, ending in actionable recommendations

## 👩‍💻 Author
Nikita Mandharne
[LinkedIn](https://linkedin.com/in/nikita-mandharne-10a2542b7) | [GitHub](https://github.com/nikk2004)
