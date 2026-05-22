# 27. SACCOs vs Banks Competitive Landscape Pipeline

## Difficulty: Intermediate | Impact: High

### Overview
Ingest SASRA (SACCO Societies Regulatory Authority) annual supervision data alongside CBK bank data. Build a comparative financial product analysing deposit mobilisation, lending rates, NPLs, and member growth — enabling policy-grade analysis of cooperative vs commercial banking.

### Tools Required
- Python
- dbt
- DuckDB
- Apache Airflow
- Superset

### Kenyan Data Sources
- SASRA Supervision Reports (sasra.go.ke)
- CBK data
- Kenya Union of Savings & Credit Co-operatives

### Project Structure
```
saccos-vs-banks-analysis/
ingestion/
  sasra_parser.py # SASRA supervision reports
  sacco_portfolio_scraper.py # Individual SACCO data
  cbk_bank_data.py # CBK bank supervision data
  kuscc_client.py # Kenya Union of SACCOs
analysis/
  deposit_mobilization.py # Deposits per member/customer
  lending_rate_comparison.py # SACCO vs Bank rates
  npl_benchmarking.py # Non-performing loans
  member_growth.py # Member vs customer growth rates
dbt/models/
  staging/stg_sasra_data.sql
  staging/stg_cbk_banks.sql
  marts/mart_sacco_bank_comparison.sql
  marts/mart_competitive_positioning.sql
seeds/
  sacco_list.csv
  bank_registry.csv
notebooks/
  policy_analysis.ipynb
dags/
tests/
docs/
```

### Key Deliverables
- SASRA supervision data ingestion
- SACCO vs Bank comparison metrics
- Deposit mobilization analysis
- Lending rate benchmarking
- NPL comparison by institution type
- Member/customer growth tracking
- Policy-grade analysis reports
- Superset dashboards

### Next Steps
1. Access SASRA supervision reports
2. Get SACCO portfolio data
3. Collect CBK banking data
4. Set up DuckDB for analysis
5. Build comparative metrics
6. Create policy frameworks
7. Schedule Airflow DAGs
8. Deploy dashboards
