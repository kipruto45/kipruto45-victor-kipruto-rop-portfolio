# 26. Kenya Mortgage & Housing Finance Data Platform

## Difficulty: Intermediate | Impact: High

### Overview
Aggregate mortgage portfolio data from HFC, Stanbic, KCB, Equity, Absa, and CBK housing finance statistics. Track average loan sizes, LTV ratios, interest rate trends, and build a county-level housing affordability index using KNBS income data.

### Tools Required
- Python
- dbt
- PostgreSQL
- Apache Airflow
- Kepler.gl
- Superset

### Kenyan Data Sources
- CBK Housing Finance Report
- Kenya Mortgage Refinance Company data
- KNBS

### Project Structure
```
kenya-mortgage-platform/
ingestion/
  cbk_mortgage_stats.py # CBK housing finance statistics
  kes_scraper.py # Kenya Economic Survey housing data
  nbs_web_scraper.py # National Bureau of Statistics housing price index
  land_registrar_parser.py # Land Registry plot values (if available)
analysis/
  affordability_calculator.py # Mortgage payment % of median income by county
  mortgage_demand.py # Regional mortgage demand forecasting
  default_probability.py # Household debt-to-income stress testing
  esg_scorer.py # Green mortgage origination tracking
dbt/models/
  staging/stg_mortgages_by_county.sql
  marts/mart_affordability_ratio.sql
  marts/mart_mortgage_default_risk.sql
seeds/
  kenya_counties.csv
  income_statistics.csv # By county
notebooks/
  affordability_regional.ipynb
dags/
tests/
docs/
```

### Key Deliverables
- Multi-bank mortgage portfolio data
- Average loan size tracking
- LTV ratio analysis
- Interest rate trend tracking
- County-level affordability index
- Geographic heat maps
- Kepler.gl visualizations
- Superset dashboards

### Next Steps
1. Access HFC portfolio data
2. Get bank mortgage disclosures
3. Collect CBK housing stats
4. Integrate KNBS income data
5. Set up PostgreSQL + PostGIS
6. Build county-level indices
7. Create Kepler.gl maps
8. Deploy dashboards
