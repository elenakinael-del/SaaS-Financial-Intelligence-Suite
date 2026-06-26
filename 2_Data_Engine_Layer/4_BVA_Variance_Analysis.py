import pandas as pd
import os

# 1. Establish file pathing
script_dir = os.path.dirname(os.path.abspath(__file__))
actuals_path = os.path.join(script_dir, 'SaaS_Executive_Dashboard_Metrics.csv')

# Load your freshly calculated metrics data
df_actuals = pd.read_csv(actuals_path)

# 2. Simulate the Budget Plan Targets (What the board originally approved)
df_actuals['Budgeted_ARR'] = df_actuals['ARR'] * 0.96  # Assume budget targeted slightly lower
df_actuals['Budgeted_Spend'] = df_actuals['SM_Spend'] * 1.05  # Assume we budgeted to spend more

# 3. Compute Variances
# Revenue Variance (Positive is good)
df_actuals['ARR_Variance_€'] = df_actuals['ARR'] - df_actuals['Budgeted_ARR']
df_actuals['ARR_Variance_%'] = (df_actuals['ARR_Variance_€'] / df_actuals['Budgeted_ARR']) * 100

# Spend Variance (Negative means we saved money / under-spent budget)
df_actuals['Spend_Variance_€'] = df_actuals['SM_Spend'] - df_actuals['Budgeted_Spend']
df_actuals['Spend_Variance_%'] = (df_actuals['Spend_Variance_€'] / df_actuals['Budgeted_Spend']) * 100

# 4. Generate Automated AI Management Commentary
def generate_commentary(row):
    comments = []
    if row['ARR_Variance_%'] > 0:
        comments.append(f"ARR out-performed budget targets by {row['ARR_Variance_%']:.1f}% due to strong expansion conversions.")
    else:
        comments.append(f"ARR fell short of target by {abs(row['ARR_Variance_%']):.1f}% due to heightened client churn.")
        
    if row['Spend_Variance_€'] < 0:
        comments.append(f"Marketing spend was optimized, running {abs(row['Spend_Variance_%']):.1f}% under budget.")
    else:
        comments.append(f"Over-spent on marketing placement initiatives by {row['Spend_Variance_%']:.1f}%.")
        
    return " | ".join(comments)

df_actuals['Executive_Commentary'] = df_actuals.apply(generate_commentary, axis=1)

# Keep the presentation summary ultra clean for the C-Suite
bva_report = df_actuals[['Month', 'ARR', 'Budgeted_ARR', 'ARR_Variance_%', 'SM_Spend', 'Budgeted_Spend', 'Spend_Variance_%', 'Executive_Commentary']].copy()
bva_report = bva_report.round(2)

# Save the final analysis report
output_path = os.path.join(script_dir, 'SaaS_Quarterly_BVA_Analysis.csv')
bva_report.to_csv(output_path, index=False)

print("\n📈 Project 3 Complete!")
print(f"--> Strategic Management BVA Report generated at: {output_path}")