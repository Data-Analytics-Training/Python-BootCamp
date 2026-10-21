import requests


def crypto_price(crypto_name):
  url = (
    f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_name.lower()}&vs_currencies=usd,try"
  )

  try:
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
      data = response.json()

      if crypto_name.lower() in data:
        usd = data[crypto_name.lower()]["usd"]
        try_price = data[crypto_name.lower()]["try"]
        print(f"✅ {crypto_name.capitalize()}: ${usd:,.2f} | ₺{try_price:,.0f} ")
      else:
        print(f"❌ {crypto_name} not found, please try again later")

    else:
      print(f"⚠️ API request failed, status code: {response.status_code}")

  except requests.exceptions.ConnectionError:
    print("❌ Internet connection error or cannot reach API")
  except requests.exceptions.Timeout:
    print("⏱️ API request timed out")
  except Exception as error:
    print(f"🚨 Unexpected error: {error}")


print("🪙 Wellcome to the Cryptocurrency Price Tracker!")
print("Supported Examples: bitcoin, ethereum, cardano, solana, dogecoin\n")

while True:
  coin = input("Enter the name of the cryptocurrency you would like to use (press 'q' to quit): ")
  if coin.lower() == "q":
    print("Exiting...")
    break
  if not coin:
    print("Please enter a cryptocurrency you would like to use.")
    continue

  crypto_price(coin)
