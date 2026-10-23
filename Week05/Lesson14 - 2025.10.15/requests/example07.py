import requests
from bs4 import BeautifulSoup


def bbc_news_scraping():

  url = "https://www.bbc.com/news"

  headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
    "Accept-Language": "tr=TR, tr; q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8",
  }

  try:
    print("Connecting to BBC News...")
    response = requests.get(url, headers=headers, timeout=15)

    if response.status_code != 200:
      print("Failed to connect! Status code: ", response.status_code)

    print("Page successfuly loaded!")

    soup = BeautifulSoup(response.text, "html.parser")

    selectors = [
      "h2[data-testid='card-headline']",  # BBC selector
      "a[data-testid='internal-link'] h2",  # Alternative selector
      "h3[class*='promo-heading']",  # Old selector
      "h2",  # All h2 tags (not recommended but last chance)
    ]

    headlines = []

    for selector in selectors:
      headlines = soup.select(selector)

      if headlines:
        print(f"✅ '{selector}' selector found {len(headlines)} items!")
        break
      else:
        print(f"❌ '{selector}' selector not found! Try another selector ")
        return

    if not headlines:
      print("❌ No headlines found! Please check selectors or website structure.")
      return

    print(f"\nBBC News Headlines: totally ({len(headlines)}) items found!")
    print("=" * 90)

    count = 0

    for i, headline in enumerate(headlines, 1):
      title = headline.get_text(strip=True)

      if title and len(title) > 10 and count < 15:
        count += 1
        print(f"{count:2d}. {title}")

    print("=" * 90)

  except requests.exceptions.Timeout:
    print("\nRequest timed out! Please try again later.")

  except requests.exceptions.RequestException as error:
    print(f"❌ Connection fail, Error: {error}")

  except Exception as error:
    print(f" ❌ An unexpected error occurred: {error}")


bbc_news_scraping()
