# Day 93: Custom Web Scraper

A collection of Python web scrapers to collect data from various websites.

## 🚀 Features

- **Book Scraper**: Scrapes book data (title, price, rating, availability)
- **Quote Scraper**: Collects inspirational quotes with authors and tags
- **Custom Template**: Reusable template for building your own scrapers

## 📦 Installation

Install required packages:

```bash
pip install -r requirements.txt
```

## 🎯 Usage

### Book Scraper
Scrapes book data from books.toscrape.com:

```bash
python book_scraper.py
```

Output: `books_data.csv` with book information and statistics

### Quote Scraper
Collects quotes from quotes.toscrape.com:

```bash
python quote_scraper.py
```

Output: `quotes_data.csv` with quotes, authors, and tags

### Custom Template
Use the template to build your own scraper:

```python
from custom_scraper_template import CustomScraper

# Create your scraper
scraper = CustomScraper("https://your-target-site.com")

# Customize the extract_data method
# Then run:
scraper.scrape()
scraper.save_to_csv()
```

## 🛠️ Customization

To scrape your own website:

1. Copy `custom_scraper_template.py`
2. Update the `base_url` in `__init__`
3. Implement the `extract_data` method with your CSS selectors
4. Run your scraper!

### Example: Finding Elements

```python
# Find by class
soup.find('div', class_='product')

# Find by id
soup.find('div', id='main-content')

# Find all matching elements
soup.find_all('a', class_='link')

# Get text content
element.text.strip()

# Get attribute value
element['href']
```

## ⚠️ Web Scraping Ethics

- Always check the website's `robots.txt` file
- Add delays between requests (use `time.sleep()`)
- Use appropriate User-Agent headers
- Respect rate limits and terms of service
- Don't overload servers with too many requests

## 📊 Output Examples

### Books Data
```csv
title,price,rating,availability
"A Light in the Attic",51.77,3,"In stock"
"Tipping the Velvet",53.74,1,"In stock"
```

### Quotes Data
```csv
quote,author,tags
"The world as we have created it...",Albert Einstein,"change, deep-thoughts, thinking, world"
```

## 🎓 Learning Resources

- BeautifulSoup Documentation: https://www.crummy.com/software/BeautifulSoup/
- Requests Library: https://requests.readthedocs.io/
- CSS Selectors: https://www.w3schools.com/cssref/css_selectors.php

## 📝 Notes

- These scrapers use practice websites designed for learning
- Modify the code to scrape data you're interested in
- Always be respectful and ethical when scraping websites
