from requests_html import HTMLSession
import pandas as pd
import os
import logging

class PublicTradeScraper:
    """
    Scrapes public trade data from accessible portals (e.g. ITC TradeMap search results).
    Provides an alternative to the paid UN Comtrade API.
    """
    
    def __init__(self):
        self.session = HTMLSession()
        
    def scrape_itc_benchmarks(self, url="https://www.trademap.org/Country_SelProduct_TS.aspx?nvpm=1|404||||TOTAL|||2|1|1|1|2|1|1|1|1"):
        """
        Example scraper for ITC TradeMap (Kenya's Trade Profile).
        This method demonstrates how to extract table data without an API key.
        """
        try:
            # Note: In a real environment, you'd need to handle cookies/sessions
            r = self.session.get(url)
            # Find the main data table
            table = r.html.find('#ctl00_PageContent_GridView_SelectedCountry', first=True)
            
            if not table:
                logging.warning("Trade data table not found on page.")
                return pd.DataFrame()
                
            # Extract rows
            rows = table.find('tr')
            data = []
            for row in rows[1:]: # Skip header
                cols = row.find('td')
                if len(cols) >= 5:
                    data.append({
                        "hs_code": cols[0].text,
                        "commodity": cols[1].text,
                        "value_usd": cols[2].text.replace(',', ''),
                        "year": 2024
                    })
            
            return pd.DataFrame(data)
        except Exception as e:
            logging.error(f"Scraping error: {e}")
            return pd.DataFrame()

    def run_ingestion(self):
        df = self.scrape_itc_benchmarks()
        if not df.empty:
            output_path = "KRA(DATA ENGINEERING)/Customs_Trade_Pipeline/ingestion/scraped_trade_benchmarks.csv"
            df.to_csv(output_path, index=False)
            print(f"Successfully scraped {len(df)} trade benchmarks to {output_path}")
        else:
            # Fallback to local files if scraping fails (e.g. no internet in sandbox)
            print("Scraping failed or returned no data. Using existing benchmarks.")

if __name__ == "__main__":
    scraper = PublicTradeScraper()
    scraper.run_ingestion()
