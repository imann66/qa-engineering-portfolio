
from playwright.sync_api import sync_playwright


with sync_playwright() as playwright:

    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.saucedemo.com/")

    # Locate username using different strategies
    print("ID:", page.locator("#user-name").count())

    print(
        "Name attribute:",
        page.locator('[name="user-name"]').count()
    )

    print(
        "Placeholder:",
        page.get_by_placeholder("Username").count()
    )

    # Locate login button using accessible role
    print(
        "Login button:",
        page.get_by_role("button", name="Login").count()
    )

    browser.close()
