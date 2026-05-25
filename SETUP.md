# 🛠️ Installation & Setup Guide

This guide will help you get the portfolio projects running on your local machine.

## 1. Prerequisites
Ensure you have the following installed:
- **Docker & Docker Compose** (Required)
- **Python 3.11+**
- **Git**

## 2. Global Installation
Clone the repository and install the shared dependencies:
```bash
git clone https://github.com/kipruto45/kipruto45-victor-kipruto-rop-portfolio.git
cd DATA_ENGINEERING
pip install -r requirements.txt
```

## 3. Running a Project (e.g., mpesa_safaricom)
Each project is designed to be self-contained.
```bash
cd mpesa_safaricom
cp .env.example .env
# Edit .env with your local settings if necessary
docker-compose up -d
```

## 4. Triggering Transformations (dbt)
Once the databases are up:
```bash
cd dbt
dbt run
dbt test
```

## 5. Visualizing Data
Launch the project-specific dashboard:
```bash
streamlit run dashboards/main_dashboard.py
```

## 6. Troubleshooting
- **Port Conflicts**: If a port (e.g., 5432) is in use, modify the mapping in the `docker-compose.yml` file.
- **Docker Health**: Ensure the Docker daemon is running and has sufficient memory (at least 4GB recommended for Airflow + Kafka).
