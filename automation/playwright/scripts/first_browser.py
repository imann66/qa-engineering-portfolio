
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    # Launch Chromium browser
    browser = playwright.chromium.launch(headless=False)

    # Create a new browser page
    page = browser.new_page()

    # Navigate to Sauce Demo
    page.goto(
        "https://www.saucedemo.com/",
        wait_until="domcontentloaded"
    )

    # Inspect the page
    print("Page title:", page.title())
    print("Current URL:", page.url)

    # Inspect login page elements
    print("Username input:", page.locator("#user-name").count())
    print("Password input:", page.locator("#password").count())
    print("Login button:", page.locator("#login-button").count())

    # Close browser
    browser.close()
