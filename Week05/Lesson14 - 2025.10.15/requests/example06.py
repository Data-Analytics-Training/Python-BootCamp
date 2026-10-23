import requests
from bs4 import BeautifulSoup


def basic_scraping_example():
  url = "https://books.toscrape.com"

  try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.select("h3 a")

    print("Books List:")
    for i, book in enumerate(books[:10], 1):  # first 10 books listed
      print(f"{i:2d}. {book.text.strip()}")

  except Exception as error:
    print("Error: ", error)


basic_scraping_example()
