"""
Custom Web Scraper Template
Modify this template to scrape any website you're interested in!
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


class CustomScraper:
    def __init__(self, base_url: str):
        """
        Initialize your scraper with the target website URL.
        
        Args:
            base_url: The main URL of the website to scrape
        """
        self.base_url = base_url
        self.data = []
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a webpage."""
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_data(self, soup: BeautifulSoup):
        """
        Extract data from the parsed HTML.
        Customize this method based on what you want to scrape!
        
        Example:
            items = soup.find_all('div', class_='item')
            for item in items:
                data = {
                    'title': item.find('h2').text,
                    'description': item.find('p').text,
                    'link': item.find('a')['href']
                }
                self.data.append(data)
        """
        # TODO: Implement your extraction logic here
        pass
    
    def scrape(self):
        """Main scraping method."""
        print(f"Starting to scrape {self.base_url}...")
        
        soup = self.get_page(self.base_url)
        if soup:
            self.extract_data(soup)
            print(f"Scraped {len(self.data)} items")
        
        # Be polite - add delay between requests
        time.sleep(1)
    
    def save_to_csv(self, filename: str = "scraped_data.csv"):
        """Save data to CSV."""
        if not self.data:
            print("No data to save!")
            return
        
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    
    def display_data(self):
        """Display scraped data."""
        if not self.data:
            print("No data available!")
            return
        
        df = pd.DataFrame(self.data)
        print("\n" + "="*50)
        print("SCRAPED DATA")
        print("="*50)
        print(df.head(10))
        print(f"\nTotal items: {len(df)}")
        print("="*50)


def main():
    # TODO: Replace with your target URL
    scraper = CustomScraper("https://example.com")
    
    # Scrape the data
    scraper.scrape()
    
    # Display results
    scraper.display_data()
    
    # Save to file
    scraper.save_to_csv()


if __name__ == "__main__":
    main()
