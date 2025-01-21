import pytest
from pytest_playwright.pytest_playwright import browser


def test_login(browser_context_with_trace)-> None:
    page = browser_context_with_trace.new_page()
    page.goto('https://3rd-eye-ed-mate-qa.mpower-social.com/login')

    # Interact with login form
    page.get_by_label("Email Address / Username").fill("3rdeye_admin")
    page.get_by_label("Password", exact=True).fill("Nopass@1234")
    page.get_by_role("button", name="Sign In").click()
    assert "Login Successful!" in page.get_by_role("status").inner_text()
