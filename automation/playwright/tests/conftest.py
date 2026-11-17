
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():

    print("\n[SESSION] Launching Chromium")

    with sync_playwright() as playwright:

        browser = playwright.chromium.launch(headless=False)

        yield browser

        print("\n[SESSION] Closing Chromium")
        browser.close()


@pytest.fixture
def context(browser):

    print("\n[TEST] Creating browser context")

    context = browser.new_context()

    yield context

    print("\n[TEST] Closing browser context")
    context.close()


@pytest.fixture
def page(context):

    print("\n[TEST] Creating browser page")

    page = context.new_page()

    yield page

    print("\n[TEST] Closing browser page")
    page.close()
