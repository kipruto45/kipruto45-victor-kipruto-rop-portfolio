# 25. NCBA Group (CBA + NIC) Post-Merger Analytics

## Difficulty: Intermediate | Impact: Medium

### Overview
Model the NCBA merger (2019) impact: extract pre- and post-merger financials, reconcile NIC and CBA historical series, track merger synergy realisation (cost savings, cross-sell) and compare against management guidance over 5 years.

### Tools Required
- Python (pdfplumber)
- dbt
- PostgreSQL
- Apache Airflow
- Jupyter
- Metabase

### Kenyan Data Sources
- NCBA Investor Relations
- NSE filings
- CMA merger documents

### Project Structure
```
ncba-merger-analytics/
ingestion/
  ncba_pre_merger.py # Equity Bank pre-merger financials 2013-2018
  cfc_stanbic_pre.py # CFC Stanbic pre-merger data
  post_merger_parser.py # Consolidated NCBA 2019-present
  fx_normalizer.py # Convert all prior periods to combined entity basis
dbt/models/
  staging/stg_equity_pre_merger.sql
  staging/stg_cfc_stanbic_pre_merger.sql
  staging/stg_ncba_post_merger.sql
  marts/mart_merger_synergies.sql # Cost saves realized
  marts/mart_revenue_retention.sql # Customer attrition/cross-sell
  marts/mart_ebitda_bridge.sql # Pre+pre vs post EBITDA
seeds/
  merger_timeline.csv # Key dates: announcement, close, integration phases
notebooks/
  synergy_realization.ipynb
  customer_consolidation.ipynb
dags/
tests/
docs/
```

### Key Deliverables
- Pre/post-merger financial series
- NIC-CBA reconciliation
- Merger synergy tracking
- Cost savings analysis
- Cross-sell impact measurement
- Guidance variance analysis
- 5-year trend reports
- Metabase dashboards

### Next Steps
1. Collect NIC historical data
2. Gather CBA historical data
3. Get NCBA merged results
4. Access merger guidance docs
5. Reconcile financial series
6. Build impact models
7. Create Jupyter analysis
8. Deploy dashboards
