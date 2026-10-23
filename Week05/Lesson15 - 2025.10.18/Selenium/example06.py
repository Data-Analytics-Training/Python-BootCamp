import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
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
    driver.get("https://www.hepsiburada.com")

    try:
      print("Cookies are accepted")

      accept_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(By.ID, "onetrust-accept-btn-handler")
      )

      # accept_button = driver.find_element(
      #     By.XPATH, '// *[ @ id = "onetrust-accept-btn-handler"]'
      # )

      accept_button.click()
      print("Cookies are accepted")

    except:
      print("There was an error occurred Cookies are not accepted")
    driver.implicitly_wait(5)

    # * Using ID
    # element = driver.find_element(By.ID, "seo-root")
    # print(element.text)

    # * Using Class_name
    # element = driver.find_element(By.CLASS_NAME, "b4LLXnK8oFgCSaa4Ni13")
    # print(element.text)

    # * Using link
    element = driver.find_element(By.LINK_TEXT, "Hakkımızda")
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.LINK_TEXT, "Hakkımızda"))
    # )

    print(element.get_attribute("href"))
    element.click()

    time.sleep(15)
    driver.implicitly_wait(5)

  except Exception as error:
    print(f"An error occurred: {error}")
  finally:
    print("Browser closed")
    # driver.quit()


selenium_test()
