from playwright.sync_api import sync_playwright


def run_test():
    with sync_playwright() as p:
        browser = p.webkit.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()
        try:
            page.goto("https://www.hepsiburada.com", wait_until="domcontentloaded")
            page.wait_for_timeout(5000)

            # Accept cookies if the button is present
            accept_div = page.locator("#hb-accept-all").filter(has_text="Kabul Et")

            if accept_div.is_visible(timeout=500):
                try:
                    accept_div.click(timeout=500)
                except:
                    # Fallback to JavaScript evaluation
                    accept_div.evaluate("element=>element.click(timeout=500)")

            print("Cookies are accepted")

            # page.wait_for_load_state("networkidle")

            # * Locate the element by ID and print its text content
            # element = page.locator(
            #     '[id="hepsiburadann-en-cok-tercih-edilen-urun-cesitleri"]'
            # )
            # print(element.all_text_contents())

            # * Locate the element by class name and print its text content
            # element = page.locator('[class="sc-content__block"]')
            # print(element.all_text_contents())

            # * Locate the element by link text and print its href attribute
            element = page.locator("[title='Kuzine Soba']")
            print(element.get_attribute("href"))

        except Exception as error:
            print("There was an error occurred Cookies are not accepted")
            print(f"Error details: {error}")

            # Wait for 5 seconds to ensure the page is fully loaded

        finally:
            browser.close()
            print("Browser closed.")


if __name__ == "__main__":
    run_test()
