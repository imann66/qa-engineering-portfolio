
from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Sauce Demo
    page.goto("https://www.saucedemo.com/")

    # Enter locked-out user credentials
    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce")

    # Attempt login
    page.locator("#login-button").click()

    # Verify login is rejected
    error_message = page.locator(
        '[data-test="error"]'
    )

    expect(error_message).to_be_visible()

    expect(error_message).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )

    # Verify user remains on login page
    expect(page).to_have_url("https://www.saucedemo.com/")

    print("TEST PASSED: Locked-out user was rejected!")
    print("Error:", error_message.text_content())

    browser.close()
