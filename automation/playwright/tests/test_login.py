
import pytest
from playwright.sync_api import expect


BASE_URL = "https://www.saucedemo.com/"


def test_successful_login(page):

    page.goto(BASE_URL)

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click()

    expect(page).to_have_url(BASE_URL + "inventory.html")

    expect(
        page.get_by_text("Products", exact=True)
    ).to_be_visible()


def test_locked_out_user(page):

    page.goto(BASE_URL)

    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce")

    page.locator("#login-button").click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()

    expect(error_message).to_have_text(
        "Epic sadface: Sorry, this user has been locked out."
    )

    expect(page).to_have_url(BASE_URL)


@pytest.mark.parametrize(
    "password",
    [
        "wrong_password",
        "123456",
        "incorrect123",
    ]
)
def test_invalid_password(page, password):

    page.goto(BASE_URL)

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill(password)

    page.locator("#login-button").click()

    error_message = page.locator('[data-test="error"]')

    expect(error_message).to_be_visible()

    expect(error_message).to_have_text(
        "Epic sadface: Username and password do not match any user in this service"
    )

    expect(page).to_have_url(BASE_URL)

