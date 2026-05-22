# 22. Interbank Lending Rate & Liquidity Monitor

## Difficulty: Intermediate | Impact: High

### Overview
Ingest daily CBK interbank rate, repo, and reverse repo volumes. Build a real-time liquidity dashboard tracking system-wide excess reserves, CBK open market operations, and early warning indicators for liquidity stress events.

### Tools Required
- Python
- TimescaleDB
- dbt
- Apache Airflow
- Grafana

### Kenyan Data Sources
- CBK Daily Interbank Rate (cbk.go.ke/data)
- CBK Money Market Operations

### Project Structure
```
kenya-liquidity-monitor/
ingestion/
  cbk_core_liabilities.py # CBK T-bills, bonds auction data
  central_bank_rate.py # CBK repo rate, reverse repo
  interbank_rates.py # Nairobi Interbank Offered Rate
  forex_scanner.py # USD/KES cross rates, volatility
features/
  liquidity_coverage_ratio.py # LCR calculator per bank
  stability_funding_ratio.py # NSFR metric
  funding_concentration.py # Liquidity risk by source
dbt/models/
  staging/stg_cbk_rates.sql
  marts/mart_lcr_by_bank.sql
  marts/mart_funding_concentration.sql
  marts/mart_fx_pressure.sql
notebooks/
  stress_testing.ipynb
dags/
tests/
docs/
```

### Key Deliverables
- Daily interbank rate tracking
- Repo/reverse repo monitoring
- Excess reserves calculation
- CBK OMO tracking
- Liquidity stress indicators
- Early warning system
- Grafana dashboards
- Alert notifications

### Next Steps
1. Access CBK daily rates
2. Set up TimescaleDB
3. Build data ingestion pipeline
4. Create liquidity metrics
5. Develop stress detection model
6. Schedule Airflow DAGs
7. Deploy Grafana dashboards
8. Configure alerts
