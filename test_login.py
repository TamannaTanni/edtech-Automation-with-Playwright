from playwright.sync_api import sync_playwright, expect
import pytest
from pytest_playwright.pytest_playwright import browser

@pytest.fixture(scope="function")
def browser_context_with_trace():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo = 1000)
        context = browser.new_context()

        # Start tracing
        context.tracing.start(
            screenshots=True,
            snapshots=True,
            sources=True
        )

        yield context

        # Stop tracing and save the trace
        context.tracing.stop(path="traces/trace.zip")
        browser.close()

def test_login(browser_context_with_trace)-> None:
    page = browser_context_with_trace.new_page()
    page.goto('https://3rd-eye-ed-mate-qa.mpower-social.com/login')

    # Interact with login form
    page.get_by_label("Email Address / Username").fill("3rdeye_admin")
    page.get_by_label("Password", exact=True).fill("Nopass@1234")
    page.get_by_role("button", name="Sign In").click()
    assert "Login Successful!" in page.get_by_role("status").inner_text()
