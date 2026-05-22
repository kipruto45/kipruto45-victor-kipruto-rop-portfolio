# 4. M-Pesa Merchant Intelligence Platform

## Difficulty: Intermediate | Impact: High

### Overview
Aggregate paybill and till numbers from public directories and business registration data. Track merchant activity trends, sector concentration, weekend vs weekday patterns, and average transaction values. Expose a merchant scorecard API for lending decisions.

### Tools Required
- Python
- PostgreSQL
- dbt
- Apache Airflow
- FastAPI (serving)
- Metabase

### Kenyan Data Sources
- Safaricom Daraja Business APIs
- Registrar of Companies (eCitizen)
- KNBS sector data

### Project Structure
```
mpesa-merchant-intelligence/
ingestion/
  merchant_scraper.py # Scrape public paybill directories
  brs_client.py # Business registration lookup
  daraja_activity.py # Pull merchant transaction summaries
dbt/models/
  staging/stg_merchants.sql
  staging/stg_transactions.sql
  marts/mart_merchant_scorecard.sql
  marts/mart_sector_concentration.sql
api/
  main.py # FastAPI: GET /merchant/{till_number}
  schemas.py # Pydantic response models
  auth.py # API key authentication
dags/
  merchant_refresh_dag.py # Daily merchant data refresh
tests/
notebooks/
docs/
```

### Key Deliverables
- Merchant database (paybill/till mappings)
- Activity trend analysis
- Merchant scorecard API
- Sector concentration reports
- Metabase dashboards
- Lending risk scores

### Next Steps
1. Scrape merchant directories
2. Integrate Registrar of Companies data
3. Set up PostgreSQL schema
4. Build dbt transformations
5. Create FastAPI endpoints
6. Generate merchant scorecards
7. Deploy dashboards
