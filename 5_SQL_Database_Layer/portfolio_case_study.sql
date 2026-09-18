-- Executive KPI case study: run after 5_Financial_DB_App.py builds corporate_finance.db.
-- Assumption: amounts use the sign convention present in the synthetic workbook.
WITH monthly_revenue AS (
  SELECT Month, SUM(MRR) AS mrr, SUM(Active_Customers) AS active_logos
  FROM dim_saas_subscriptions GROUP BY Month
), monthly_opex AS (
  SELECT Month, SUM(Amount) AS opex
  FROM fact_general_ledger WHERE Category = 'OpEx' GROUP BY Month
), metrics AS (
  SELECT r.Month, r.mrr, r.mrr * 12 AS arr, r.active_logos,
         COALESCE(o.opex, 0) AS opex,
         LAG(r.mrr, 12) OVER (ORDER BY r.Month) AS mrr_prior_year
  FROM monthly_revenue r LEFT JOIN monthly_opex o USING (Month)
)
SELECT Month, ROUND(mrr, 2) AS mrr, ROUND(arr, 2) AS arr, active_logos,
       ROUND(opex, 2) AS opex_burn,
       ROUND(mrr - opex, 2) AS operating_cash_flow,
       ROUND(100.0 * (mrr / NULLIF(mrr_prior_year, 0) - 1), 1) AS mrr_yoy_pct
FROM metrics ORDER BY Month;
