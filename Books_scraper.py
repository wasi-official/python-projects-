# Books Scraper — Scrape 1000 books from books.toscrape.com into Excel
import pandas as pd
import requests
from bs4 import BeautifulSoup

data = []

with open("books.txt", "w") as f:
    for page in range(1, 51):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.find_all("h3")
        prices = soup.find_all("p", class_="price_color")

        for price, book in zip(prices, books):
            title = book.find("a")["title"]
            clean_price = float(price.text[1:])
            data.append((title, clean_price))

df = pd.DataFrame(data, columns=["Title", "Price"])
df.to_excel("books.xlsx", index=False)
print("Done. books.xlsx created.")