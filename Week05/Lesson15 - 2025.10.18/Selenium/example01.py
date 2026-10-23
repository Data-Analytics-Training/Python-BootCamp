"""
Web Automation:

Understanding what web automation is and why it is used
Installing and using Selenium WebDriver
Finding and interacting with elements on web pages
Filling out forms, clicking buttons, and navigating pages
Developing automation projects with real-life examples


Use Cases:
- Test Automation (QA)
- Data Collection (alternative of Web Scraping)
- Automatically Form Filled
- Bot development (e.g., price tracking)


What is Selenium?
It is an open-source web automation tool
It programmatically controls browsers (Chrome, Firefox, Edge, etc.)
Selenium WebDriver: Communicates directly with the browser


Reasons to Use Selenium:
- To fetch pages loaded with JavaScript
- For actions like filling out forms or clicking buttons
- For automate browser-based tests


BeautifulSoup vs Selenium:
BeautifulSoup
- Only an HTML parser
- Ideal for static pages
- Fast and lightweight

Selenium
- Controls a real browser
- Can execute JavaScript
- Ideal for dynamic pages
- Slower but more powerful
"""

"""
Webdrivers:
ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
https://googlechromelabs.github.io/chrome-for-testing/index.html

GeckoDriver (Firefox): https://github.com/mozilla/geckodriver/releases

EdgeDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

SafariDriver: Built-in with Safari on macOS

"""

# For Safari
import time

from selenium import webdriver

driver = webdriver.Safari()

try:
    driver.get("https://www.google.com")
    time.sleep(3)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
