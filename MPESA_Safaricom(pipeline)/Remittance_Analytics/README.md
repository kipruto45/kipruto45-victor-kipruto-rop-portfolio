# 6. M-Pesa Send-Money Remittance Analytics

## Difficulty: Intermediate | Impact: Medium

### Overview
Track domestic and international M-Pesa remittance flows using CBK remittance data and Daraja International API. Build corridor-level analytics (Kenya-Tanzania, Kenya-Uganda), model seasonality, and benchmark against formal bank wire fees.

### Tools Required
- Python
- dbt
- Snowflake
- Apache Airflow
- Superset

### Kenyan Data Sources
- CBK Cross-Border Remittance data
- Daraja International API
- World Bank Remittance Prices

### Project Structure
```
mpesa-remittance-analytics/
ingestion/
  cbk_remittance.py # CBK cross-border remittance tables
  worldbank_client.py # World Bank Remittance Prices API
  daraja_intl.py # Daraja International API
dbt/models/
  staging/stg_remittances.sql
  marts/mart_corridors.sql # Kenya-TZ, KE-UG, KE-UK, etc.
  marts/mart_fee_benchmark.sql # M-Pesa vs SWIFT vs Wise
  marts/mart_seasonality.sql
notebooks/
  corridor_analysis.ipynb
  fee_comparison.ipynb
dags/
tests/
docs/
```

### Key Deliverables
- Remittance flow database (Snowflake)
- Corridor-level analytics (KE-TZ, KE-UG, etc.)
- Seasonality modeling
- Fee benchmarking reports
- Superset visualization dashboards

### Next Steps
1. Access CBK remittance datasets
2. Set up Daraja International API
3. Download World Bank data
4. Build Snowflake warehouse
5. Create dbt models
6. Develop Airflow pipelines
7. Deploy Superset dashboards
