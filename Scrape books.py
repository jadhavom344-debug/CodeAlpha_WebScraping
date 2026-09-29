"""
CodeAlpha Internship - Task 1
Web Scraping - books.toscrape.com

Scrapes book title, price, rating and stock status from the site
and dumps everything into a csv. Using this instead of a real
ecommerce site since it's built for scraping practice.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# this site has ~50 pages, each with 20 books
base_url = "https://books.toscrape.com/catalogue/page-{}.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ratings on the site are given as word classes like "Three", "Five" etc
# so mapping them to numbers manually
rating_words = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

all_books = []

page = 1
while True:
    url = base_url.format(page)
    res = requests.get(url, headers=headers)

    # once we go past the last page it 404s, so just stop the loop
    if res.status_code != 200:
        print("no more pages, stopping at page", page)
        break

    soup = BeautifulSoup(res.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")

    if len(books) == 0:
        break

    print("scraping page", page, "-", len(books), "books found")

    for b in books:
        title = b.h3.a["title"]

        price_tag = b.find("p", class_="price_color")
        price = price_tag.text.replace("£", "")
        price = float(price)

        # rating class looks like "star-rating Three" so grab the 2nd word
        rating_class = b.p["class"][1]
        rating = rating_words.get(rating_class)

        avail = b.find("p", class_="instock availability")
        avail = avail.text.strip()

        all_books.append({
            "title": title,
            "price": price,
            "rating": rating,
            "availability": avail
        })

    page += 1
    time.sleep(1)  # don't want to hammer the server too fast

df = pd.DataFrame(all_books)
df.to_csv("books_dataset.csv", index=False)

print("done, total books scraped:", len(df))
print(df.head())
