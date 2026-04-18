# Quotes Scraper — Scrape 100 quotes from quotes.toscrape.com into Excel
import pandas as pd
import requests
from bs4 import BeautifulSoup

data = []

for page in range(1, 11):
    url = f"https://quotes.toscrape.com/page/{page}/"
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("div", class_="quote")

    for q in quotes:
        text_tag = q.find("span", class_="text")
        author_tag = q.find("small", class_="author")
        if text_tag and author_tag:
            data.append((text_tag.text, author_tag.text))

df = pd.DataFrame(data, columns=["Quote", "Author"])
df.to_excel("quotes.xlsx", index=False)
print("Done. quotes.xlsx created.")