import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))
bva_path = os.path.join(script_dir, 'SaaS_Quarterly_BVA_Analysis.csv')
metrics_path = os.path.join(script_dir, 'SaaS_Executive_Dashboard_Metrics.csv')

# Load the datasets
df_bva = pd.read_csv(bva_path)
df_metrics = pd.read_csv(metrics_path)

# Convert dates for plotting
df_bva['Month'] = pd.to_datetime(df_bva['Month'])
df_metrics['Month'] = pd.to_datetime(df_metrics['Month'])

# Set professional visualization style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Chart 1: ARR Actuals vs Budget Targets (BVA Performance)
ax1.plot(df_bva['Month'], df_bva['ARR'] / 1e6, label='Actual ARR', color='#0F4C81', linewidth=3)
ax1.plot(df_bva['Month'], df_bva['Budgeted_ARR'] / 1e6, label='Budget Target', color='#F5A623', linestyle='--', linewidth=2)
ax1.set_title('ARR Performance vs. Approved Budget Plan', fontsize=14, fontweight='bold', pad=15)
ax1.set_ylabel('Annual Recurring Revenue (€ Millions)', fontsize=12)
ax1.legend(fontsize=11, loc='upper left')
ax1.tick_params(colors='#333333')

# Chart 2: Strategic Unit Economics (LTV to CAC Ratio)
ax2.plot(df_metrics['Month'], df_metrics['LTV_to_CAC'], color='#10B981', linewidth=3, label='LTV:CAC Ratio')
ax2.axhline(3.0, color='#EF4444', linestyle=':', label='SaaS Health Benchmark (3.0x)')
ax2.set_title('SaaS Unit Economics: LTV to CAC Scaling Trend', fontsize=14, fontweight='bold', pad=15)
ax2.set_ylabel('LTV : CAC Ratio (x)', fontsize=12)
ax2.legend(fontsize=11, loc='upper left')

# Optimize layout and save
plt.tight_layout()
chart_output = os.path.join(script_dir, 'Executive_Board_Charts.png')
plt.savefig(chart_output, dpi=300)
plt.close()

print("\n🖼️  Project 4 Visuals Generated!")
print(f"--> Clean Executive Presentation Chart Cards saved to: {chart_output}")