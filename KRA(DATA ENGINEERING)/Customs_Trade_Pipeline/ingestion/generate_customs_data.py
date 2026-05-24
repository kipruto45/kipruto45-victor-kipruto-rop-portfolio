import pandas as pd
import numpy as np
import os
from datetime import datetime

def generate_customs_data(output_dir="KRA(DATA ENGINEERING)/Customs_Trade_Pipeline/ingestion"):
    os.makedirs(output_dir, exist_ok=True)
    
    hs_codes = {
        "2701": "Coal; briquettes",
        "7108": "Gold, unwrought",
        "0901": "Coffee",
        "0902": "Tea",
        "0603": "Cut flowers",
        "8471": "Computers/Processors",
        "8703": "Motor cars"
    }
    
    countries = ["China", "India", "UAE", "USA", "Netherlands", "Pakistan", "UK", "Tanzania", "Uganda"]
    years = range(2020, 2026)
    
    data = []
    
    for year in years:
        for code, desc in hs_codes.items():
            for country in countries:
                volume = np.random.uniform(10, 1000)
                declared_value = volume * np.random.uniform(500, 2000)
                duty_collected = declared_value * np.random.uniform(0.1, 0.35)
                
                # Injected anomaly for risk scoring
                risk_score = np.random.uniform(0, 100)
                if country == "UAE" and code == "7108": # Gold from UAE - high risk profile
                    risk_score = np.random.uniform(70, 95)
                    declared_value *= 0.6 # Under-valuation
                
                data.append({
                    "hs_code": code,
                    "commodity": desc,
                    "origin_country": country,
                    "year": year,
                    "volume_tons": round(volume, 2),
                    "declared_value_m_kes": round(declared_value, 2),
                    "duty_collected_m_kes": round(duty_collected, 2),
                    "risk_score": round(risk_score, 2)
                })
                
    df = pd.DataFrame(data)
    df.to_csv(f"{output_dir}/customs_declarations.csv", index=False)
    print(f"Generated Customs data in {output_dir}")

if __name__ == "__main__":
    generate_customs_data()
