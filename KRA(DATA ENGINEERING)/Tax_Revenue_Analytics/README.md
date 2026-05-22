# 11. KRA Tax Revenue Analytics Warehouse

## Difficulty: Beginner | Impact: High

### Overview
Ingest KRA monthly and annual revenue performance reports (PDF and press releases). Extract collections by tax head (Income Tax, VAT, Excise, Customs), build a data warehouse tracking revenue vs target, year-on-year growth, and GDP tax ratio trends over 15+ years.

### Tools Required
- Python (pdfplumber)
- dbt
- PostgreSQL
- Apache Airflow
- Apache Superset

### Kenyan Data Sources
- KRA Revenue Performance Reports (kra.go.ke)
- National Treasury budget outturn
- IMF AFRITAC

### Project Structure
```
kra-revenue-warehouse/
ingestion/
  kra_pdf_downloader.py # Download KRA press releases & reports
  pdf_extractor.py # pdfplumber: extract revenue tables
  press_release_parser.py # Parse monthly revenue announcements
  normalizer.py # Standardise tax head names 2009-2024
dbt/models/
  staging/stg_revenue_monthly.sql
  staging/stg_revenue_annual.sql
  marts/mart_revenue_by_tax_head.sql
  marts/mart_target_vs_actual.sql
  marts/mart_gdp_tax_ratio.sql
seeds/
  tax_heads.csv # Canonical tax category reference
  kenya_gdp.csv # KNBS GDP data for ratio calc
dags/
  kra_monthly_ingest_dag.py
tests/
notebooks/
docs/
```

### Key Deliverables
- KRA report PDF parsing
- Tax collection data warehouse
- 15+ year historical trends
- Revenue vs target tracking
- Tax head breakdown (Income, VAT, Excise, Customs)
- GDP tax ratio analysis
- Superset dashboards

### Next Steps
1. Collect KRA reports (15+ years)
2. Build PDF parser
3. Extract tax collections by head
4. Set up PostgreSQL schema
5. Create dbt models
6. Schedule Airflow ingestion
7. Build Superset dashboards
