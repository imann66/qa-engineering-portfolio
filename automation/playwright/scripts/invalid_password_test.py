
from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Sauce Demo
    page.goto("https://www.saucedemo.com/")

    # Enter valid username and invalid password
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password")

    # Attempt login
    page.locator("#login-button").click()

    # Verify error message
    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()

    expect(error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

    # Verify user remains on login page
    expect(page).to_have_url("https://www.saucedemo.com/")

    print("TEST PASSED: Invalid password was rejected!")
    print("Error:", error_message.text_content())

    browser.close()
