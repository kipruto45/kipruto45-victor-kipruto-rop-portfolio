import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_subsidiary_data(output_dir="/opt/airflow/projects/pan_africa/ingestion"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    subsidiaries = [
        {"name": "Kenya", "currency": "KES", "base_profit": 15000000000},
        {"name": "DRC", "currency": "CDF", "base_profit": 8000000000},
        {"name": "Uganda", "currency": "UGX", "base_profit": 2000000000},
        {"name": "Tanzania", "currency": "TZS", "base_profit": 1500000000},
        {"name": "Rwanda", "currency": "RWF", "base_profit": 1000000000},
        {"name": "South_Sudan", "currency": "SSP", "base_profit": 500000000},
        {"name": "Ethiopia", "currency": "ETB", "base_profit": 200000000}
    ]

    periods = ["2023-FY", "2024-Q1", "2024-Q2", "2024-Q3"]
    
    data = []
    for sub in subsidiaries:
        for period in periods:
            growth = 1 + np.random.normal(0.05, 0.02)
            profit = sub["base_profit"] * growth
            data.append({
                "subsidiary": sub["name"],
                "period": period,
                "currency": sub["currency"],
                "net_profit": round(profit, 2),
                "total_assets": round(profit * 8, 2)
            })
    
    pd.DataFrame(data).to_csv(f"{output_dir}/subsidiary_financials.csv", index=False)
    print(f"Generated Pan-Africa financial data in {output_dir}")

if __name__ == "__main__":
    generate_subsidiary_data()
