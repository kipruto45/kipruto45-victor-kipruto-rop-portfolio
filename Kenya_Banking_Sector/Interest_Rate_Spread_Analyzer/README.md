# 29. Kenya Interest Rate Spread Analyser

## Difficulty: Intermediate | Impact: High

### Overview
Model the spread between average lending rates and deposit rates across all banks using CBK Interest Rate Survey data. Decompose spreads into risk premium, operating cost, and profit margin components. Benchmark Kenya against EAC peers.

### Tools Required
- Python
- dbt
- PostgreSQL
- Apache Airflow
- Plotly
- Superset

### Kenyan Data Sources
- CBK Interest Rate Survey (monthly)
- World Bank FinStats
- IMF Financial Access Survey

### Project Structure
```
kenya-interest-rates/
ingestion/
  cbk_rate_survey.py # CBK monthly interest rate survey
  world_bank_finstats.py # World Bank FinStats data
  imf_financial_access.py # IMF Financial Access Survey
dbt/models/
  staging/stg_cbk_rates.sql
  staging/stg_world_bank.sql
  marts/mart_lending_deposit_spread.sql
  marts/mart_spread_components.sql
  marts/mart_eac_benchmarks.sql
analysis/
  spread_decomposition.py # Isolate risk, cost, margin components
  eac_comparison.py # Tanzania, Uganda, Rwanda benchmarks
  clustering_analysis.py # Bank peer clustering by spread profile
notebooks/
  spread_analysis.ipynb
  eac_benchmarking.ipynb
dags/
tests/
docs/
```

### Key Deliverables
- Lending/deposit rate tracking
- Spread calculation and analysis
- Spread decomposition (risk/cost/margin)
- Risk premium estimation
- Operating cost analysis
- EAC regional benchmarking
- Comparative analysis reports
- Superset dashboards

### Next Steps
1. Access CBK Interest Rate Survey
2. Get World Bank FinStats data
3. Download IMF Financial Access data
4. Set up PostgreSQL
5. Build spread models
6. Create decomposition logic
7. Schedule Airflow DAGs
8. Deploy dashboards
