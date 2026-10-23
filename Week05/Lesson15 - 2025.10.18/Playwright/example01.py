from playwright.sync_api import sync_playwright

# Don't forget to install the necessary browsers using: playwright install webkit

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)  # WebKit engine is used for Safari
    page = browser.new_page()

    try:
        page.goto("https://www.google.com")
        page.wait_for_timeout(3000)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        browser.close()
