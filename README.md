# CodeAlpha_WebScraping

Task 1 of my CodeAlpha Data Analytics internship - web scraping with Python.

## What this does
Scrapes book info (title, price, rating, stock status) from [books.toscrape.com](https://books.toscrape.com) - it's a demo site made specifically for practicing scraping, so no issues with terms of service or anything like that.

The script goes through every page on the site, pulls the data with BeautifulSoup, and saves it all into a csv using pandas.

## Files
- `scrape_books.py` - the actual scraper
- `books_dataset.csv` - output data
- `requirements.txt` - libraries needed
- `README.md` - this file

## Libraries used
- requests (to get the page HTML)
- beautifulsoup4 (to parse it)
- pandas (to save as csv)

## How to run it
```
pip install -r requirements.txt
python scrape_books.py
```

It'll print progress for each page as it scrapes, and save everything to `books_dataset.csv` when done.

## Notes
- Ratings on the site are shown as word classes (like "Three" instead of 3), so I mapped them to numbers in the script.
- Added a 1 second delay between requests so it's not hammering the server.
- Data in the repo right now is just a small sample - running the script pulls the full ~1000 book dataset.

## About
Done as part of my CodeAlpha internship (Data Analytics track).

GitHub: [jadhavom344-debug](https://github.com/jadhavom344-debug)
