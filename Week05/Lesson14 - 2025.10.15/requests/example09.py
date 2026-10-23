import requests
from bs4 import BeautifulSoup


def product_scraper_with_images():

  url = "https://webscraper.io/test-sites/e-commerce/allinone"

  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "tr=TR, tr; q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
  }

  try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    products = soup.select(".thumbnail")

    print("📸 PRODUCTS VE IMAGES:\n")

    for i, product in enumerate(products[:5], 1):
      try:
        name = product.select_one(".title").text.strip()
        price = product.select_one(".price").text.strip()

        img = product.select_one("img")
        if img and img.get("src"):
          image_url = "https://webscraper.io" + img["src"]
        else:
          image_url = "There is no image available for this product."

        print(f"{i}. {name}")
        print(f"   💰 {price}")
        print(f"   🖼️  {image_url}")
        print("-" * 60)

      except AttributeError:
        continue

  except Exception as e:
    print(f"Error: {e}")


# Çalıştır
product_scraper_with_images()
