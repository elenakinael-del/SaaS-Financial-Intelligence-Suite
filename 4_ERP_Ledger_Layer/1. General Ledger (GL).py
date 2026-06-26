import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
months = pd.date_range(start="2024-01-01", end="2025-12-01", freq="MS")

# 1. Generate SaaS Customer Subscriptions (The Revenue Engine)
segments = {
    'Enterprise': {'count': 12, 'arr': 150000, 'churn': 0.01, 'expansion': 0.04},
    'Mid-Market': {'count': 45, 'arr': 45000, 'churn': 0.03, 'expansion': 0.03},
    'SMB': {'count': 210, 'arr': 8500, 'churn': 0.06, 'expansion': 0.01}
}

revenue_records = []
for m in months:
    for seg, traits in segments.items():
        # Account for natural business variance
        churned = int(np.random.binomial(traits['count'], traits['churn']))
        new_logos = int(np.random.poisson(traits['count'] * 0.04))
        traits['count'] = max(5, traits['count'] - churned + new_logos)
        
        mrr = (traits['count'] * (traits['arr'] / 12)) * np.random.uniform(0.98, 1.02)
        revenue_records.append([m, seg, traits['count'], round(mrr, 2), round(mrr * 12, 2)])

df_rev = pd.DataFrame(revenue_records, columns=['Month', 'Segment', 'Active_Customers', 'MRR', 'ARR'])

# 2. Generate General Ledger Ledger (Expenses & Balance Sheet Items)
gl_records = []
for m in months:
    # OpEx Rollforward (Seasonality & Growth)
    idx = (m.year - 2024) * 12 + m.month
    base_salaries = 180000 * (1 + 0.015 ** idx)
    marketing_spend = 45000 * np.random.uniform(0.9, 1.1) + (15000 if m.month in [9, 11] else 0) # Q3/Q4 marketing push
    hosting_cogs = (df_rev[df_rev['Month'] == m]['MRR'].sum() * 0.12) # 12% hosting COGS
    
    gl_records.extend([
        [m, 'COGS', 'Hosting & Infrastructure', round(hosting_cogs, 2)],
        [m, 'OpEx', 'Salaries & Wages', round(base_salaries, 2)],
        [m, 'OpEx', 'Sales & Marketing Programs', round(marketing_spend, 2)],
        [m, 'OpEx', 'G&A Software & Tools', round(12000 * np.random.uniform(0.95, 1.05), 2)],
    ])

df_gl = pd.DataFrame(gl_records, columns=['Month', 'Category', 'Account', 'Amount'])

# Export to Excel to serve as our data source inputs
with pd.ExcelWriter('FP&A_Model_Data_Source.xlsx', engine='openpyxl') as writer:
    df_rev.to_excel(writer, sheet_name='Historical_SaaS_Metrics', index=False)
    df_gl.to_excel(writer, sheet_name='Historical_GL_Dump', index=False)

print("🚀 Module 1 Complete: High-fidelity historical datasets exported to FP&A_Model_Data_Source.xlsx.")