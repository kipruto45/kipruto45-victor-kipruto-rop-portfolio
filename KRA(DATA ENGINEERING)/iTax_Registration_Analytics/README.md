# 13. iTax Business Registration Analytics

## Difficulty: Intermediate | Impact: Medium

### Overview
Scrape the KRA iTax public PIN checker and business registration gazette notices to build a database of registered taxpayers by county, sector, and registration date. Track new business formation rates as an economic leading indicator.

### Tools Required
- Python (Playwright)
- PostgreSQL + PostGIS
- dbt
- Apache Airflow
- Superset

### Kenyan Data Sources
- KRA iTax public portal
- Kenya Gazette (kenyalaw.org)
- Registrar of Companies eCitizen

### Project Structure
```
kra-business-registration/
ingestion/
  itax_scraper.py # Playwright: KRA iTax PIN checker
  gazette_parser.py # Kenya Gazette registration notices
  ecitizen_scraper.py # Registrar of Companies eCitizen
  rate_limiter.py # Polite scraping with backoff
dbt/models/
  staging/stg_registrations.sql
  marts/mart_new_businesses_by_county.sql
  marts/mart_sector_formation_rate.sql
  marts/mart_economic_leading_indicator.sql
spatial/
  county_mapping.py # Map business addresses to counties
seeds/
  kenya_counties.csv
  sector_sic_codes.csv # SIC code to sector mapping
dags/
tests/
notebooks/
docs/
```

### Key Deliverables
- iTax PIN scraping pipeline
- Business registration database
- Gazette notice parsing
- Taxpayer registration by county/sector
- Business formation rate tracking
- Economic leading indicators
- Superset dashboards

### Next Steps
1. Set up Playwright for web scraping
2. Build iTax PIN checker scraper
3. Parse Kenya Gazette notices
4. Integrate Registrar of Companies data
5. Set up PostgreSQL + PostGIS
6. Create dbt models
7. Schedule Airflow DAGs
8. Deploy dashboards
