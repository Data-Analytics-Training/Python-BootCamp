"""
Methods to Find Web Elements
Selenium provides 8 main methods to locate HTML elements

- find_element(By.ID, "id")
- find_element(By.NAME, "name")
- find_element(By.CLASS_NAME, "class")
- find_element(By.TAG_NAME, "div")
- find_element(By.XPATH, "//input[@name='q']")
- find_element(By.CSS_SELECTOR, "input[name='q']")
- find_element(By.LINK_TEXT, "Gmail")
- find_element(By.PARTIAL_LINK_TEXT, "Gma")
"""

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager, ChromeType

browser_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

options = Options()
options.binary_location = browser_path

service = Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://www.google.com")
driver.implicitly_wait(5)  # Upload page

search_box = driver.find_element(By.NAME, "q")
time.sleep(2)

search_box.send_keys("python")
search_box.submit()
time.sleep(2)
driver.implicitly_wait(5)

time.sleep(3)
driver.quit()
