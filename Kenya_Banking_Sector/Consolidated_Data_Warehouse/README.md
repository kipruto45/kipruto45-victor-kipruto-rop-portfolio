# 21. Kenya Banking Sector Consolidated Data Warehouse

## Difficulty: Intermediate | Impact: High

### Overview
Ingest CBK Bank Supervision Annual Report tables for all 38+ licensed banks. Build a star-schema DWH with bank-level time-series on: total assets, loans, deposits, NPL ratios, capital adequacy, NIM, ROE, and branch/ATM/agent network. Enable peer benchmarking queries.

### Tools Required
- Python (pdfplumber, tabula)
- dbt
- PostgreSQL
- Apache Airflow
- Apache Superset

### Kenyan Data Sources
- CBK Bank Supervision Reports 2010-2024 (cbk.go.ke)
- CMA annual reports

### Project Structure
```
kenya-banking-dwh/
ingestion/
  cbk_prudential.py # CBK prudential returns (FR)
  cbk_statistics.py # CBK banking statistics
  nse_scrappers/
    kcb_scraper.py
    equity_scraper.py
    stanbic_scraper.py
    absa_scraper.py
  subsidiary_ingest.py # DTB, I&M, National Bank etc.
reconciliation/
  npl_bridge.py # CBK NPL vs bank-reported NPL
  deposit_bridge.py # CBK deposits vs bank deposits
  capital_audit.py # CBK CAR vs Tier 1 ratios
dbt/models/
  staging/stg_cbk_returns.sql
  staging/stg_bank_filings.sql
  marts/mart_system_npl.sql
  marts/mart_sector_deposits.sql
  marts/mart_sector_capital.sql
seeds/
  bank_registry.csv # Full list of CBK-licensed banks
  cbk_return_codes.csv
dags/
tests/
notebooks/
docs/
```
│   ├── staging/
│   ├── marts/
│   └── star_schema.sql
├── schemas/
├── airflow_dags/
└── dashboards/
```

### Key Deliverables
- CBK supervision data extraction
- Star-schema dimensional model
- Bank-level metric tables
- 14+ year time-series
- Peer benchmarking queries
- PostgreSQL warehouse
- Superset dashboards

### Next Steps
1. Collect CBK reports (2010-2024)
2. Build table extraction (tabula/camelot)
3. Parse bank metrics
4. Design star schema
5. Set up PostgreSQL
6. Create dbt models
7. Schedule Airflow DAGs
8. Deploy benchmarking dashboards
