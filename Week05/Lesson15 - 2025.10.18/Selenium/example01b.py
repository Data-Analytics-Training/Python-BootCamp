import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager, ChromeType

browser_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

options = Options()
options.binary_location = browser_path

service = Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")

time.sleep(3)
driver.quit()
