import requests
import json
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com"


quotes = []
authors = {}
page = 1

while True:
    response = requests.get(f"{BASE_URL}/page/{page}/")
    if response.status_code != 200:
        break

    soup = BeautifulSoup(response.text, "html.parser")
    quotes_block = soup.find_all("div", class_="quote")

    if not quotes_block:
        break

    for q in quotes_block:
        quote_text = q.find("span", class_="text").text
        author_name = q.find("small", class_="author").text
        tags = [tag.text for tag in q.find_all("a", class_="tag")]

        quotes.append({
            "quote": quote_text,
            "author": author_name,
            "tags": tags
        })

        if author_name not in authors:
            author_url = BASE_URL + q.find("a")["href"]
            author_page = requests.get(author_url)
            author_soup = BeautifulSoup(author_page.text, "html.parser")

            authors[author_name] = {
                "fullname": author_name,
                "born_date": author_soup.find("span", class_="author-born-date").text,
                "born_location": author_soup.find("span", class_="author-born-location").text,
                "description": author_soup.find("div", class_="author-description").text.strip()
            }

    page += 1


with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(quotes, f, ensure_ascii=False, indent=2)

with open("authors.json", "w", encoding="utf-8") as f:
    json.dump(list(authors.values()), f, ensure_ascii=False, indent=2)