import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

browser_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
chromedriver_path = "/Users/odoker/Documents/Projects/Python/Python-BootCamp/Week05/Lesson15 - 2025.10.18/chromedriver"

service = Service(chromedriver_path)
options = Options()
options.binary_location = browser_path

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

time.sleep(3)
driver.quit()
