"""
Book Scraper - Collects data about books from books.toscrape.com
This scraper extracts book titles, prices, ratings, and availability.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from typing import List, Dict


class BookScraper:
    def __init__(self, base_url: str = "http://books.toscrape.com"):
        self.base_url = base_url
        self.books_data = []
        
    def get_page(self, url: str) -> BeautifulSoup:
        """Fetch and parse a webpage."""
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'html.parser')
        except requests.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return None
    
    def extract_rating(self, rating_class: str) -> int:
        """Convert word rating to number."""
        ratings = {
            'One': 1, 'Two': 2, 'Three': 3, 
            'Four': 4, 'Five': 5
        }
        for word, num in ratings.items():
            if word in rating_class:
                return num
        return 0
    
    def scrape_book_details(self, book_element) -> Dict:
        """Extract details from a single book element."""
        try:
            # Title
            title = book_element.find('h3').find('a')['title']
            
            # Price
            price_text = book_element.find('p', class_='price_color').text
            price = float(price_text.replace('£', ''))
            
            # Rating
            rating_class = book_element.find('p', class_='star-rating')['class']
            rating = self.extract_rating(' '.join(rating_class))
            
            # Availability
            availability = book_element.find('p', class_='instock availability').text.strip()
            
            return {
                'title': title,
                'price': price,
                'rating': rating,
                'availability': availability
            }
        except Exception as e:
            print(f"Error extracting book details: {e}")
            return None
    
    def scrape_page(self, page_num: int = 1) -> int:
        """Scrape a single page and return count of books found."""
        if page_num == 1:
            url = f"{self.base_url}/index.html"
        else:
            url = f"{self.base_url}/catalogue/page-{page_num}.html"
        
        print(f"Scraping page {page_num}...")
        soup = self.get_page(url)
        
        if not soup:
            return 0
        
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            book_data = self.scrape_book_details(book)
            if book_data:
                self.books_data.append(book_data)
        
        return len(books)
    
    def scrape_all_pages(self, max_pages: int = 5):
        """Scrape multiple pages."""
        print(f"Starting to scrape up to {max_pages} pages...\n")
        
        for page_num in range(1, max_pages + 1):
            books_found = self.scrape_page(page_num)
            
            if books_found == 0:
                print(f"No more books found. Stopping at page {page_num - 1}")
                break
            
            # Be polite - add delay between requests
            time.sleep(1)
        
        print(f"\nScraping complete! Collected {len(self.books_data)} books.")
    
    def save_to_csv(self, filename: str = "books_data.csv"):
        """Save scraped data to CSV file."""
        if not self.books_data:
            print("No data to save!")
            return
        
        df = pd.DataFrame(self.books_data)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    
    def get_statistics(self):
        """Display statistics about scraped data."""
        if not self.books_data:
            print("No data available!")
            return
        
        df = pd.DataFrame(self.books_data)
        
        print("\n" + "="*50)
        print("BOOK SCRAPING STATISTICS")
        print("="*50)
        print(f"Total books scraped: {len(df)}")
        print(f"\nPrice Statistics:")
        print(f"  Average price: £{df['price'].mean():.2f}")
        print(f"  Minimum price: £{df['price'].min():.2f}")
        print(f"  Maximum price: £{df['price'].max():.2f}")
        print(f"\nRating Distribution:")
        print(df['rating'].value_counts().sort_index(ascending=False))
        print(f"\nMost expensive book: {df.loc[df['price'].idxmax(), 'title']}")
        print(f"Price: £{df['price'].max():.2f}")
        print("="*50)


def main():
    # Create scraper instance
    scraper = BookScraper()
    
    # Scrape 5 pages (100 books)
    scraper.scrape_all_pages(max_pages=5)
    
    # Display statistics
    scraper.get_statistics()
    
    # Save to CSV
    scraper.save_to_csv("books_data.csv")


if __name__ == "__main__":
    main()
