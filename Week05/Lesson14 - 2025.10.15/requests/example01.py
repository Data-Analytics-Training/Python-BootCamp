"""
Web Scraping:

Web scraping is process of automatically extracting data from web pages.

What can be done with web scraping:
- Track product prices on e-commerce or news websites
- Find top-rated movie or series from film databases
- Analyze trending topics on social media

✅ Allowed
- Scrape publicly accessible data
- Follow robots.txt rules
- Add delays between requests to avoid overloading the server

❌ Not Allowed
- Hack pages that required login.
- Copy copyrighted content without permission
- Send continuous requests that overload the server (DoS-like behavior)
"""

import requests

url = "https://www.google.com"

response = requests.get(url)

if response.status_code == 200:
  print("Success!")
  print("Status Code: ", response.status_code)

  # Print the HTML content of the page.
  print(response.text)
else:
  print("Failed to receive data")
