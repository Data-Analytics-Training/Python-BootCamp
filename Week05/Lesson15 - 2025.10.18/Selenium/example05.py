import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager, ChromeType


def setup_driver():
  browser_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"

  options = webdriver.ChromeOptions()
  options.binary_location = browser_path

  # options.add_argument("--start-maximized")
  options.add_argument("--diable-extensions")
  options.add_argument("--disable-notifications")

  service = Service(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install())

  driver = webdriver.Chrome(service=service, options=options)
  driver.implicitly_wait(5)

  return driver


def selenium_test():
  driver = setup_driver()

  try:
    driver.get("https://www.google.com.tr")
    driver.implicitly_wait(5)

    search_box = driver.find_element(By.NAME, "q")
    time.sleep(3)

    search_box.send_keys("python")
    search_box.submit()
    time.sleep(3)

    driver.save_screenshot("test.png")
    driver.implicitly_wait(3)

  except Exception as error:
    print("Error: ", error)

  finally:
    time.sleep(3)
    driver.quit()


selenium_test()
