import pandas as pd
import sqlite3
import os

# Define file paths safely across our directory structure
DATA_SOURCE = "../2_Data_Engine_Layer/FP&A_Model_Data_Source.xlsx"
DB_NAME = "corporate_finance.db"

print("============================================================")
print("🗄️ INITIALIZING FINANCIAL RELATIONAL DATABASE ENGINE (SQLITE3)")
print("============================================================")

if not os.path.exists(DATA_SOURCE):
    print(f"❌ Error: Could not find the source data at {DATA_SOURCE}")
    print("Please make sure your Module 1 script has run successfully.")
    exit()

# 1. Extract raw transactional streams from our Excel Architecture
df_rev = pd.read_excel(DATA_SOURCE, sheet_name='Historical_SaaS_Metrics')
df_gl = pd.read_excel(DATA_SOURCE, sheet_name='Historical_GL_Dump')

# Ensure date strings are formatted properly for SQL indexing
df_rev['Month'] = pd.to_datetime(df_rev['Month']).dt.strftime('%Y-%m-%d')
df_gl['Month'] = pd.to_datetime(df_gl['Month']).dt.strftime('%Y-%m-%d')

# 2. Establish local embedded SQLite Database connection
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# 3. Formulate Database Schemas and push pandas dataframes into SQL Tables
df_rev.to_sql('dim_saas_subscriptions', conn, if_exists='replace', index=True, index_label='subscription_id')
df_gl.to_sql('fact_general_ledger', conn, if_exists='replace', index=True, index_label='transaction_id')

print("✅ Data pipeline populated successfully into relational tables.")
print("   • Table [dim_saas_subscriptions] -> Structured")
print("   • Table [fact_general_ledger]    -> Structured")
print("------------------------------------------------------------")

# 4. Execute a high-end SQL analytical query using Common Table Expressions (CTEs)
# This query calculates standard corporate run rates and cross-references Opex costs live in SQL
sql_query = """
WITH MonthlySaaSSummary AS (
    SELECT 
        Month,
        SUM(MRR) AS Total_MRR,
        SUM(ARR) AS Total_ARR,
        SUM(Active_Customers) AS Total_Active_Logos
    FROM dim_saas_subscriptions
    GROUP BY Month
),
MonthlyOpexSummary AS (
    SELECT 
        Month,
        SUM(Amount) AS Total_Opex_Spend
    FROM fact_general_ledger
    WHERE Category = 'OpEx'
    GROUP BY Month
)
SELECT 
    s.Month,
    ROUND(s.Total_MRR, 2) AS [Monthly MRR],
    ROUND(s.Total_ARR, 2) AS [Annualized Run Rate],
    s.Total_Active_Logos AS [Active Logos],
    ROUND(o.Total_Opex_Spend, 2) AS [OpEx Burn],
    ROUND(s.Total_MRR - o.Total_Opex_Spend, 2) AS [Net Operating Cash Flow]
FROM MonthlySaaSSummary s
JOIN MonthlyOpexSummary o ON s.Month = o.Month
ORDER BY s.Month DESC
LIMIT 5;
"""

print("🔍 RUNNING INSTITUTIONAL ANALYTICAL SQL FINANCIAL CLOSE QUERY:")
df_result = pd.read_sql_query(sql_query, conn)
print(df_result.to_string(index=False))
print("============================================================")

# Close database connections safely
conn.close()