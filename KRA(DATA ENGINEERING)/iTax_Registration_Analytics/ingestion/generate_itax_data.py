import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def generate_itax_data(output_dir="KRA(DATA ENGINEERING)/iTax_Registration_Analytics/ingestion"):
    os.makedirs(output_dir, exist_ok=True)
    
    counties = [
        "Nairobi", "Mombasa", "Kiambu", "Nakuru", "Machakos", "Kisumu", 
        "Uasin Gishu", "Kilifi", "Kajiado", "Nyeri"
    ]
    
    sectors = ["Financial Services", "Retail", "Manufacturing", "ICT", "Construction", "Hospitality"]
    
    data = []
    start_date = datetime(2020, 1, 1)
    
    # Generate 1000 "New Registrations"
    for i in range(2000):
        reg_date = start_date + timedelta(days=np.random.randint(0, 365*5))
        county = random.choices(counties, weights=[40, 10, 8, 7, 7, 7, 6, 5, 5, 5])[0]
        sector = np.random.choice(sectors)
        
        data.append({
            "pin": f"P{np.random.randint(100000000, 999999999)}A",
            "registration_date": reg_date.strftime("%Y-%m-%d"),
            "county": county,
            "sector": sector,
            "is_active": np.random.choice([True, False], p=[0.85, 0.15])
        })
        
    df = pd.DataFrame(data)
    df.to_csv(f"{output_dir}/itax_registrations.csv", index=False)
    print(f"Generated iTax data in {output_dir}")

import random
if __name__ == "__main__":
    generate_itax_data()
