# 24. Stanbic / Standard Chartered / DTB Peer Analysis

## Difficulty: Intermediate | Impact: Medium

### Overview
Build automated ingestion of quarterly results for mid-tier Kenya banks: Stanbic, Standard Chartered Kenya, Diamond Trust Bank, I&M Bank, and Prime Bank. Create a peer benchmarking dashboard with z-score normalised KPIs and automated commentary generation.

### Tools Required
- Python
- dbt
- PostgreSQL
- Apache Airflow
- OpenAI API (commentary)
- Superset

### Kenyan Data Sources
- NSE Filings Portal
- Individual bank investor pages
- CBK peer data

### Project Structure
```
kenya-peer-analysis/
ingestion/
  nse_scrapers/ # Get all 10 listed banks quarterly filings
    kcb_scraper.py
    equity_scraper.py
    stanbic_scraper.py
    absa_scraper.py
    co_op_scraper.py
    i&m_scraper.py
    diamond_scraper.py
    housing_scraper.py
    national_bank_scraper.py
    ecobank_scraper.py
metrics/
  profitability_ratios.py # ROE, ROA, NIM comparisons
  efficiency_ratios.py # Cost-to-income, NPL ratios
  growth_metrics.py # YoY asset/deposit growth
  positioning_matrix.py # Scale vs profitability scatter
dbt/models/
  marts/mart_peer_comparison.sql
notebooks/
  peer_positioning.ipynb
  efficiency_frontier.ipynb
dags/
tests/
docs/
```

### Key Deliverables
- Quarterly results ingestion
- Multi-bank KPI database
- Z-score normalization
- Peer benchmarking analytics
- Automated commentary generation
- Superset dashboards
- Comparative analysis reports

### Next Steps
1. Identify all 5 bank data sources
2. Set up web scrapers
3. Build KPI extraction
4. Create z-score normalizer
5. Integrate OpenAI API
6. Set up PostgreSQL schema
7. Schedule Airflow DAGs
8. Deploy dashboards
