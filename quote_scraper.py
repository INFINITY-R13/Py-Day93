"""
Quote Scraper - Collects inspirational quotes from quotes.toscrape.com
Extracts quotes, authors, and tags.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


class QuoteScraper:
    def __init__(self):
        self.base_url = "http://quotes.toscrape.com"
        self.quotes_data = []
    
    def get_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a webpage."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error: {e}")
            return None
    
    def scrape_quotes(self, page_num: int = 1):
        """Scrape quotes from a page."""
        url = f"{self.base_url}/page/{page_num}/"
        print(f"Scraping page {page_num}...")
        
        soup = self.get_page(url)
        if not soup:
            return 0
        
        quotes = soup.find_all('div', class_='quote')
        
        for quote in quotes:
            text = quote.find('span', class_='text').text.strip('"')
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            self.quotes_data.append({
                'quote': text,
                'author': author,
                'tags': ', '.join(tags)
            })
        
        return len(quotes)
    
    def scrape_all(self, max_pages: int = 10):
        """Scrape multiple pages."""
        print(f"Scraping quotes...\n")
        
        for page in range(1, max_pages + 1):
            found = self.scrape_quotes(page)
            if found == 0:
                break
            time.sleep(1)
        
        print(f"\nCollected {len(self.quotes_data)} quotes!")
    
    def save_to_csv(self, filename: str = "quotes_data.csv"):
        """Save to CSV."""
        if self.quotes_data:
            df = pd.DataFrame(self.quotes_data)
            df.to_csv(filename, index=False)
            print(f"Saved to {filename}")
    
    def display_random_quotes(self, n: int = 5):
        """Display random quotes."""
        if not self.quotes_data:
            return
        
        df = pd.DataFrame(self.quotes_data)
        print("\n" + "="*60)
        print(f"RANDOM QUOTES (showing {min(n, len(df))})")
        print("="*60)
        
        for _, row in df.sample(min(n, len(df))).iterrows():
            print(f"\n\"{row['quote']}\"")
            print(f"  - {row['author']}")
            print(f"  Tags: {row['tags']}")
        
        print("="*60)


def main():
    scraper = QuoteScraper()
    scraper.scrape_all(max_pages=10)
    scraper.display_random_quotes(5)
    scraper.save_to_csv()


if __name__ == "__main__":
    main()
