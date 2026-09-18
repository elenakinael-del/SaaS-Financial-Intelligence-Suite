# SaaS Financial Intelligence: Executive KPI Case Study

An end-to-end, **synthetic** SaaS finance case study: operational metrics and general-ledger rows are transformed into an executive KPI mart and queried with SQLite. It demonstrates data modelling, SQL, metric definitions, and decision-ready reporting; it is not a production ERP.

## What a hiring manager can review

- A reproducible KPI data mart: run `2_Data_Engine_Layer/3_SaaS_Dashboard_Engine.py`.
- A relational SQLite build: run `5_SQL_Database_Layer/5_Financial_DB_App.py` from that folder.
- A documented CTE case study in [`5_SQL_Database_Layer/portfolio_case_study.sql`](5_SQL_Database_Layer/portfolio_case_study.sql).
- A data-quality test in `tests/test_dashboard_metrics.py`.

### Metric definitions and assumptions

MRR is the monthly sum in `Historical_SaaS_Metrics`; ARR is `MRR × 12`; active logos are summed from the supplied synthetic source. CAC is reported only where new logos are positive—no artificial floor is applied. The Rule of 40 uses an explicitly labelled 22% EBITDA-margin **assumption**, because the source does not contain observed EBITDA.

 System Architecture & Layers

The repository is modularly structured into core functional layers, isolating data generation, transactional accounting, and analytical reporting:

SaaS-Financial-Intelligence-Suite/
├── 1_Financial_Architecture/  # Core financial planning & forecasting logic
├── 2_Data_Engine_Layer/       # Central data storage & upstream Excel data sources
├── 3_Executive_Reporting/     # Corporate reporting models & KPI outputs
├── 4_ERP_Ledger_Layer/        # Synthetic ledger transaction engine (NetSuite Logic)
└── 5_SQL_Database_Layer/      # Relational storage & advanced SQL query engine


 Prerequisites & Installation

To run the tools in this suite, you must have Python installed along with the required financial and data engineering libraries. Install them all with a single terminal command:

pip install pandas numpy matplotlib openpyxl pytest


 Module Deep Dives

1. ERP & NetSuite Ledger Automator (4_ERP_Ledger_Layer)

SaaS Revenue Engine: Simulates cohort-specific customer behavior (Enterprise, Mid-Market, SMB) leveraging natural business variance, Poisson-distributed customer acquisition, and binomial churn rates.

Journal Audit Automation: Mimics an enterprise ERP controller by automatically aggregating daily ledger transactions into a retrospective Trial Balance Summary, computing structural totals for Revenue, COGS, and OpEx lines.

2. Relational SQL Database Layer (5_SQL_Database_Layer)

Database Modeling: Programmatically structures raw operational outputs into an embedded SQLite3 database schema (corporate_finance.db), creating indexed transactional fact tables and customer dimension tables.

Institutional Analytics: Executes advanced financial analytics directly inside SQL using Common Table Expressions (CTEs) and relational JOIN operations to compute recurring software metrics including Monthly Recurring Revenue (MRR), Annualized Run Rate (ARR), Monthly OpEx Burn, and Net Operating Cash Flow.

 Execution & Deployment

To execute the database compilation pipeline and output the executive-level monthly financial close summary directly to your terminal console, run:

cd 5_SQL_Database_Layer
python3 5_Financial_DB_App.py

# from the repository root
pytest -q


 Tech Stack

Languages: Python, SQL (SQLite3)

Libraries: Pandas, NumPy, OpenPyXL, Matplotlib

Concepts: Relational Database Design, Common Table Expressions (CTEs), General Ledger Architecture, SaaS Financial Metrics (ARR/MRR/Burn Rate)
