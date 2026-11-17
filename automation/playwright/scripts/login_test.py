
from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:

    # Launch browser
    browser = playwright.chromium.launch(headless=False)

    # Create page
    page = browser.new_page()

    # Open Sauce Demo
    page.goto("https://www.saucedemo.com/")

    # Enter valid credentials
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    # Click login
    page.locator("#login-button").click()

    # Verify successful login
    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()

    print("TEST PASSED: Login successful!")
    print("Current URL:", page.url)

    # Close browser
    browser.close()
