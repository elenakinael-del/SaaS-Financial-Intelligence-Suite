# SaaS Financial Intelligence Suite 

An institutional-grade, automated corporate finance engineering suite that bridges dynamic financial planning and analysis (FP&A) with programmatic data pipelines, automated management variance commentary, and an interactive executive command-line copilot.

---

##  Architecture Ecosystem

This suite functions as a unified corporate financial data pipeline, moving from raw workbook modeling into structured algorithmic analysis and executive-ready reporting outputs:

1. **Strategic Planning Layer (`/1_Financial_Architecture`)**
   * `B2B_SaaS_Strategic_Financial_Model_v1.0.xlsx`: A dynamic 5-year integrated financial model tracking Revenue Forecasts, Cost Projections, Opex, Hiring Schedules, and 3-Statement financial integrations (Income Statement, Balance Sheet, Cash Flow).

2. **Data Processing & Analytics Engine (`/2_Data_Engine_Layer`)**
   * `3_SaaS_Dashboard_Engine.py`: Processes operational raw data streams to programmatically calculate advanced SaaS unit economics including ARR, MRR, active customer logos, and customer lifetime metrics.
   * `4_BVA_Variance_Analysis.py`: Evaluates actual results against budget plans line-by-line, computing variance percentages and auto-generating text narrative commentary for management briefings.

3. **Executive Presentation Layer (`/3_Executive_Reporting`)**
   * `5_Executive_Board_Pack.py`: Programmatically generates production-ready chart cards (`Executive_Board_Charts.png`) tracking ARR against budget alongside LTV:CAC scaling trend guardrails.
   * `6_AI_Finance_Copilot.py`: A live interactive terminal interface allowing C-suite executives to query the financial stack, running instant health diagnostics or briefings.

---

##  Core Financial Engine Highlights

### Real-Time Financial Diagnostics (December 2025 Run)
* **Annualized Run-Rate (ARR):** €8,448,008.76
* **Monthly Recurring Revenue (MRR):** €704,000.73
* **LTV to CAC Ratio:** 7.18x *(Exceeds the standard 3.0x venture health benchmark)*
* **Rule of 40 Efficiency Score:** 39.9% *(Highly efficient operational scaling trend)*

---

##  Getting Started & Execution

Ensure your environment contains the required dependencies:
```bash
pip install pandas numpy matplotlib openpyxl
