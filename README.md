SaaS Financial Intelligence Suite 

An institutional-grade corporate financial data engineering pipeline and ledger automation ecosystem. This suite models end-to-end financial operations for a subscription-based enterprise, moving raw operational metrics into structured accounting journals and relational databases for strategic analysis.

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

pip install pandas numpy matplotlib openpyxl


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


 Tech Stack

Languages: Python, SQL (SQLite3)

Libraries: Pandas, NumPy, OpenPyXL, Matplotlib

Concepts: Relational Database Design, Common Table Expressions (CTEs), General Ledger Architecture, SaaS Financial Metrics (ARR/MRR/Burn Rate)
