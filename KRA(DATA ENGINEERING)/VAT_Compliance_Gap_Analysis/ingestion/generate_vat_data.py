import pandas as pd
import numpy as np
import os

def generate_vat_gap_data(output_dir="KRA(DATA ENGINEERING)/VAT_Compliance_Gap_Analysis/ingestion"):
    os.makedirs(output_dir, exist_ok=True)
    
    sectors = ["Agriculture", "Manufacturing", "Construction", "Retail Trade", "Telecommunications", "Finance", "Real Estate"]
    years = range(2018, 2026)
    
    data = []
    
    for year in years:
        for sector in sectors:
            # Theoretical VAT based on sector GDP
            sector_gdp = np.random.uniform(100000, 500000)
            theoretical_vat = sector_gdp * 0.16 # Standard 16% VAT
            
            # Compliance varies by sector
            compliance_rate = np.random.uniform(0.6, 0.95)
            if sector in ["Retail Trade", "Agriculture"]:
                compliance_rate = np.random.uniform(0.4, 0.7) # Harder to collect
                
            actual_vat = theoretical_vat * compliance_rate
            vat_gap = theoretical_vat - actual_vat
            
            data.append({
                "sector": sector,
                "year": year,
                "sector_gdp_m_kes": round(sector_gdp, 2),
                "theoretical_vat_m_kes": round(theoretical_vat, 2),
                "actual_vat_m_kes": round(actual_vat, 2),
                "vat_gap_m_kes": round(vat_gap, 2),
                "c_efficiency_ratio": round(actual_vat / theoretical_vat, 4)
            })
            
    df = pd.DataFrame(data)
    df.to_csv(f"{output_dir}/vat_compliance_data.csv", index=False)
    print(f"Generated VAT Gap data in {output_dir}")

if __name__ == "__main__":
    generate_vat_gap_data()
