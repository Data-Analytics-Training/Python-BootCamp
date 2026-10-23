import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"

response = requests.get(url)

if response.status_code == 200:
  print("Success!")
  print("Status Code: ", response.status_code)

  soup = BeautifulSoup(response.text, "html.parser")

  # Print the title of the web page
  print("Title ot the web page: ", soup.title.text)
  # Title ot the web page:  Google

else:
  print("Failed to receive data")
