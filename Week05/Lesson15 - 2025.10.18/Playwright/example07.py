from playwright.sync_api import sync_playwright


def fill_form():

    with sync_playwright() as p:
        browser_path = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        # browser = p.chromium.launch(headless=False, executable_path=browser_path)
        browser = p.webkit.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        try:
            page.goto(
                "https://demoqa.com/automation-practice-form",
                wait_until="domcontentloaded",
            )

            page.wait_for_timeout(3000)

            # * First Name field
            page.locator('[id="firstName"]').fill("John")
            page.wait_for_timeout(1000)

            # * Last Name field
            page.locator('[id="lastName"]').fill("Dow")
            page.wait_for_timeout(1000)

            # * Email field
            # page.locator("userEmail").fill("johndow@mail.com")
            page.locator('[id="userEmail"]').fill("johndow@mail.com")
            page.wait_for_timeout(1000)

            # * Gender radio button
            page.locator("input.form-check-input[value='Male']").click()
            page.wait_for_timeout(1000)

            # * Mobile field
            page.locator('[id="userNumber"]').fill("0987654321")
            page.wait_for_timeout(1000)

            # * Date of Birth field
            # ? Long way to fill the date with birth field using multiple steps
            page.locator('[id="dateOfBirthInput"]').click()
            page.wait_for_timeout(1000)

            page.locator(".react-datepicker__year-select").click()
            page.wait_for_timeout(1000)
            page.locator(".react-datepicker__year-select").select_option("1978")
            page.wait_for_timeout(1000)

            page.locator(".react-datepicker__month-select").click()
            page.wait_for_timeout(1000)
            page.locator(".react-datepicker__month-select").select_option("May")
            page.wait_for_timeout(1000)

            page.locator(
                ".react-datepicker__day--002:not(.react-datepicker__day--outside-month)"
            ).click()

            # ? Short way to fill the date with birth field using multiple steps
            # page.locator('[id="dateOfBirthInput"]').click()
            # page.wait_for_timeout(1000)
            # page.locator(".react-datepicker__year-select").select_option("1978")
            # page.wait_for_timeout(1000)
            # page.locator(".react-datepicker__month-select").select_option("May")
            # page.wait_for_timeout(1000)
            # page.locator(
            #     ".react-datepicker__day--002:not(.react-datepicker__day--outside-month)"
            # ).click()

            # * Subject field
            page.locator('[id="subjectsInput"]').fill("ma")
            page.wait_for_timeout(1000)
            page.locator('[id="react-select-2-option-0"]').click()
            page.wait_for_timeout(1000)

            page.locator('[id="subjectsInput"]').fill("co")
            page.wait_for_timeout(1000)
            page.locator('[id="react-select-2-option-0"]').click()
            page.wait_for_timeout(1000)

            # * Hobbies checkboxes
            page.locator('input.form-check-input[value="3"]').click()
            page.wait_for_timeout(1000)

            # * Picture upload field
            # element = page.locator('[id="uploadPicture"]').click()
            # element.set_input_files("/Users/odoker/Desktop/16377.jpg")

            # * Current Address field
            page.locator('[id="currentAddress"]').fill("123 Main St")
            page.wait_for_timeout(1000)

            # * State and City dropdowns
            page.locator('[id="state"]').click()
            page.wait_for_timeout(1000)
            page.locator('div[id^="react-select-3-option-"]').filter(
                has_text="Haryana"
            ).click()
            page.wait_for_timeout(1000)
            page.locator('[id="city"]').click()
            page.wait_for_timeout(1000)
            page.locator('div[id^="react-select-4-option-"]').filter(
                has_text="Panipat"
            ).click()
            page.wait_for_timeout(1000)

            # * Submit button
            page.locator('[id="submit"]').click()

            page.wait_for_timeout(5000)
            print("All fields are filled successfully. You can submit the form now.")

        except Exception as error:
            print(f"An error occurred: {error}")

        finally:
            browser.close()
            print("Browser closed.")


if __name__ == "__main__":
    fill_form()
