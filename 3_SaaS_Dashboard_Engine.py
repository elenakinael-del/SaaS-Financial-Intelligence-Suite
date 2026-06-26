import pandas as pd
import numpy as np
import os

# 1. Automatically find the exact directory where this script lives
script_dir = os.path.dirname(os.path.abspath(__file__))
print(f"🔄 Execution folder detected: {script_dir}")

# Target the actual Excel workbook file directly
excel_path = os.path.join(script_dir, 'FP&A_Model_Data_Source.xlsx')
print(f"✅ Reading data directly from Excel workbook: {excel_path}")

# Read the specific sheets right out of the .xlsx file
df_metrics = pd.read_excel(excel_path, sheet_name='Historical_SaaS_Metrics')
df_gl = pd.read_excel(excel_path, sheet_name='Historical_GL_Dump')

# Clean date column strings to datetime format
df_metrics['Month'] = pd.to_datetime(df_metrics['Month'])
df_gl['Month'] = pd.to_datetime(df_gl['Month'])

# 2. Isolate and roll up Monthly Recurring Revenue (MRR) and S&M Spend
mrr_monthly = df_metrics.groupby('Month')['MRR'].sum().reset_index()
mrr_monthly['ARR'] = mrr_monthly['MRR'] * 12

sm_spend = df_gl[df_gl['Account'] == 'Sales & Marketing Programs'].groupby('Month')['Amount'].sum().reset_index()
sm_spend = sm_spend.rename(columns={'Amount': 'SM_Spend'})

# Merge operational datasets together
df_dash = pd.merge(mrr_monthly, sm_spend, on='Month')

# 3. Track Customer Acquisitions & Movement Variations
customer_counts = df_metrics.groupby('Month')['Active_Customers'].sum().reset_index()
df_dash = pd.merge(df_dash, customer_counts, on='Month')

# Calculate Net New Customer additions month-over-month
df_dash['New_Logos'] = df_dash['Active_Customers'].diff().fillna(0).astype(int)
df_dash['New_Logos'] = df_dash['New_Logos'].apply(lambda x: max(x, 2)) 

# 4. Compute Core SaaS Unit Economics Metrics
df_dash['CAC'] = np.where(df_dash['New_Logos'] > 0, df_dash['SM_Spend'] / df_dash['New_Logos'], 0)
df_dash['ARPU_Mo'] = df_dash['MRR'] / df_dash['Active_Customers']
df_dash['Churn_Rate_Est'] = 0.015 
df_dash['LTV'] = (df_dash['ARPU_Mo'] * 0.80) / df_dash['Churn_Rate_Est'] 
df_dash['LTV_to_CAC'] = df_dash['LTV'] / df_dash['CAC']

# 5. Calculate Elite Executive "Rule of 40" Matrix
df_dash['ARR_Growth_YoY'] = df_dash['ARR'].pct_change(periods=12).fillna(0)
df_dash['EBITDA_Margin'] = 0.22 
df_dash['Rule_of_40'] = (df_dash['ARR_Growth_YoY'] + df_dash['EBITDA_Margin']) * 100

# Format and round outputs cleanly
df_dash = df_dash.round(2)

# Save output right next to the script
output_path = os.path.join(script_dir, 'SaaS_Executive_Dashboard_Metrics.csv')
df_dash.to_csv(output_path, index=False)

print("\n📊 Project 2 Complete!")
print(f"--> Saved metrics data successfully to: {output_path}")