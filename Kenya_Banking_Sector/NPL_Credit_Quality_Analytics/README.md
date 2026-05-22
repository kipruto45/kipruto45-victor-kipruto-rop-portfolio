# 23. NPL & Credit Quality Trend Analytics

## Difficulty: Advanced | Impact: High

### Overview
Track NPL formation, write-off, and recovery rates across all Kenya banks from CBK quarterly data. Segment by bank tier (Tier 1/2/3), loan category (personal, SME, corporate, mortgage), and economic sector. Build an early warning scorecard for sector stress.

### Tools Required
- Python
- dbt
- DuckDB
- Apache Airflow
- Metabase
- scikit-learn (anomaly detection)

### Kenyan Data Sources
- CBK Credit Survey
- CBK Bank Supervision data
- CRB Africa portfolio data

### Project Structure
```
kenya-npl-analytics/
ingestion/
  cbk_returns.py # CBK NPL + Loan Loss Provision data
  crb_open_api.py # Credit Reference Bureau (CRB) portal
  ncba_parser.py # NCBA quarterly NPL by sector
  stanbic_parser.py # Stanbic quarterly sectoral breakdown
analysis/
  npl_vintage.py # NPL emergence & resolution curves
  sector_analysis.py # Sectoral NPL concentration
  crb_default_tracker.py # Consumer-level defaults
  provision_adequacy.py # LLP/NPL ratio trends
dbt/models/
  marts/mart_npl_by_sector.sql
  marts/mart_npl_by_product.sql
  marts/mart_provision_coverage.sql
notebooks/
  npl_stress_scenario.ipynb
dags/
tests/
docs/
```

### Key Deliverables
- NPL formation tracking
- Write-off and recovery analysis
- Bank tier segmentation
- Loan category breakdown
- Sector stress indicators
- Early warning scorecards
- Anomaly detection
- Metabase dashboards

### Next Steps
1. Access CBK credit survey data
2. Get bank supervision NPL data
3. Integrate CRB sector data
4. Set up DuckDB
5. Build segmentation models
6. Create stress detection
7. Schedule Airflow pipelines
8. Deploy dashboards
