# 28. Digital Banking Adoption Tracker

## Difficulty: Beginner | Impact: High

### Overview
Combine CBK mobile and internet banking statistics with bank-by-bank digital channel disclosures. Build a tracker measuring digital transaction share, cost-per-transaction trends, and which banks are winning the digital shift — with monthly automated updates.

### Tools Required
- Python
- dbt
- PostgreSQL
- Apache Airflow
- Grafana

### Kenyan Data Sources
- CBK Annual Report Digital Finance section
- Individual bank annual reports
- CA Kenya

### Project Structure
```
kenya-digital-adoption/
ingestion/
  cbk_mobile_banking.py # CBK monthly mobile banking stats
  cbk_internet_banking.py # CBK internet banking data
  bank_disclosures_scraper.py # Parse annual reports for digital metrics
  ca_telecom_client.py # CA telecom subscriber data
dbt/models/
  staging/stg_cbk_digital.sql
  staging/stg_bank_digital_disclosures.sql
  marts/mart_adoption_metrics.sql
  marts/mart_cost_per_transaction.sql
  marts/mart_digital_shift_leaders.sql
analysis/
  adoption_curve_fitting.py # S-curve adoption models
  cost_analysis.py # Operating cost trends
dags/
  monthly_update_dag.py
notebooks/
  adoption_trends.ipynb
tests/
docs/
```

### Key Deliverables
- Mobile banking adoption tracking
- Internet banking statistics
- Digital transaction share metrics
- Cost-per-transaction analysis
- Bank-by-bank comparisons
- Monthly automated updates
- Grafana dashboards
- Digital shift leadership reports

### Next Steps
1. Collect CBK digital finance data
2. Get bank annual reports
3. Parse digital disclosures
4. Set up PostgreSQL
5. Create dbt models
6. Build tracking metrics
7. Schedule Airflow DAGs
8. Deploy Grafana dashboards
