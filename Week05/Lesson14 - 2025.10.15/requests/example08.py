import requests
from bs4 import BeautifulSoup


def simple_product_scraper():

  url = "https://webscraper.io/test-sites/e-commerce/allinone"
  url = "https://webscraper.io/test-sites/e-commerce/allinone/phones"

  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "tr=TR, tr; q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
  }

  try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select(".thumbnail")

    print("🛒 Product Lists:\n")

    for i, product in enumerate(products[:8], 1):
      try:
        # Product name
        name = product.select_one(".title").text.strip()

        # Price
        price = product.select_one(".price").text.strip()

        # Description
        description = product.select_one(".description").text.strip()

        # Rating
        rating = product.select_one(".ratings p").text.strip()

        print(f"{i:2d}. {name}")
        print(f"    💰 {price}")
        print(f"    📝 {description}")
        print(f"    ⭐ {rating}")
        print("-" * 50)

      except AttributeError:
        continue

  except Exception as e:
    print(f"Hata: {e}")


# Çalıştır
simple_product_scraper()
