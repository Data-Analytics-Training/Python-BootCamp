"""
This is a sample Python script to demonstrate how to interact with a web form using Selenium WebDriver.
The script will open the DemoQA Automation Practice Form page, fill in some fields, and submit the form.

You can customize this script according to your specific needs and test cases.
https://demoqa.com/automation-practice-form
"""

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


def filling_form():
  driver = setup_driver()

  try:
    driver.get("https://demoqa.com/automation-practice-form")
    driver.implicitly_wait(5)
    time.sleep(1)

    first_name = driver.find_element(By.ID, "firstName")
    first_name.send_keys("Jone")
    time.sleep(1)

    last_name = driver.find_element(By.ID, "lastName")
    last_name.send_keys("Dow")
    time.sleep(1)

    email = driver.find_element(By.ID, "userEmail")
    email.send_keys("jonedoe@mail.com")
    time.sleep(1)

    # Using CSS selector via filling radio buttons
    gender = driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]')
    gender.click()

    # Using XPath via filling radio buttons
    # gender = driver.find_element(By.XPATH, '//label[@for="gender-radio-1"]')
    # gender.click()

    # Using JS script to filling radio button
    # driver.execute_script("document.getElementById('gender-radio-1').click()")
    time.sleep(1)

    mobile = driver.find_element(By.ID, "userNumber")
    mobile.send_keys("0123456789")
    time.sleep(1)

    # Entering birthday section
    date_input = driver.find_element(By.ID, "dateOfBirthInput")
    date_input.click()

    driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select").click()
    driver.find_element(By.XPATH, "//option[text()='1990']").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select").click()
    driver.find_element(By.XPATH, "//option[text()='January']").click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//div[text()='15']").click()
    # driver.find_element(By.XPATH, "//option[text()='1990']")
    time.sleep(1)

    # Entering subject section
    subjects_input = driver.find_element(By.ID, "subjectsInput")

    # first subject
    subjects_input.send_keys("Comp")
    # subjects_input.send_keys(Keys.ENTER)

    subjects_input.send_keys("Mathematics")
    # subjects_input.send_keys(Keys.ENTER)

    submit_button = driver.find_element(By.ID, "submit")
    submit_button.click()

    time.sleep(5)

  except Exception as error:
    print(f"An error occurred: {error}")

  finally:
    print("Browser closed")
    driver.quit()


filling_form()
