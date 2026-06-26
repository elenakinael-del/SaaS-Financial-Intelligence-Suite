import pandas as pd
import os

# 1. Setup paths and load the unified metrics layer
script_dir = os.path.dirname(os.path.abspath(__file__))
metrics_path = os.path.join(script_dir, 'SaaS_Executive_Dashboard_Metrics.csv')

if not os.path.exists(metrics_path):
    print("❌ Error: Core metrics file missing. Please run script 3 first!")
    exit()

df = pd.read_csv(metrics_path)
df['Month'] = pd.to_datetime(df['Month'])

def launch_copilot():
    print("=" * 60)
    print("🤖 STRATEGIC FINANCE AI COPILOT ENGINE v1.0")
    print("   Connected directly to: SaaS_Executive_Dashboard_Metrics.csv")
    print("=" * 60)
    print("Available Commands:")
    print("  [1] Get Latest Executive Summary (Most Recent Month)")
    print("  [2] Run Health Check (Unit Economics & Rule of 40)")
    print("  [3] Exit Copilot")
    print("-" * 60)
    
    while True:
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            latest_row = df.iloc[-1]
            date_str = latest_row['Month'].strftime('%B %Y')
            print(f"\n📋 --- EXECUTIVE BRIEFING FOR {date_str.upper()} ---")
            print(f"  • Monthly Recurring Revenue (MRR): €{latest_row['MRR']:,}")
            print(f"  • Annualized Run-Rate (ARR):       €{latest_row['ARR']:,}")
            print(f"  • Active Customer Logo Base:      {int(latest_row['Active_Customers'])} logos")
            print(f"  • Sales & Marketing Spend:        €{latest_row['SM_Spend']:,}")
            
        elif choice == '2':
            latest_row = df.iloc[-1]
            rule_40 = latest_row['Rule_of_40']
            ltv_cac = latest_row['LTV_to_CAC']
            
            print("\n🩺 --- SAAS HEALTH ANALYSIS & GUARDRAILS ---")
            print(f"  • LTV to CAC Ratio: {ltv_cac}x")
            if ltv_cac >= 3.0:
                print("    ✅ Unit economics are highly efficient (above the 3.0x venture benchmark).")
            else:
                print("    ⚠️ Unit economics are tight. Customer acquisition costs are high relative to value.")
                
            print(f"  • Rule of 40 Score: {rule_40:.1f}%")
            if rule_40 >= 40.0:
                print("    ✅ Elite Tier! Growth rates combined with margins exceed the 40% threshold.")
            else:
                print("    ℹ️ Healthy, but running under elite scaling efficiency metrics.")
                
        elif choice == '3':
            print("\n👋 Disconnecting financial data streams. Portfolio engine secure.")
            break
        else:
            print("Invalid input. Please choose option 1, 2, or 3.")

if __name__ == '__main__':
    launch_copilot()