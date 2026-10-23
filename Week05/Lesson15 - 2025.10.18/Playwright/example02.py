from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto("https://www.google.com", wait_until="domcontentloaded")

        search_box = page.locator('[name="q"]')
        search_box.wait_for(state="visible", timeout=5000)
        search_box.fill("python")
        search_box.press("Enter")

        # Wait for results to load
        page.wait_for_load_state("domcontentloaded")
        page.wait_for_selector("#search", timeout=5000)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        browser.close()
