from playwright.sync_api import sync_playwright, expect
import pytest
import json
import csv


# File to load the authentication state
auth_file = "auth_state.json"

#Fixture to save traces
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



# Using saved state test will continue to run
@pytest.fixture(scope="function")
def login_with_saved_state(playwright):
    """Create a browser context with saved login state."""
    # Load the saved authentication state
    with open(auth_file, "r") as f:
        auth_data = json.load(f)

    # Create a browser context with the saved storage state
    context = playwright.chromium.launch(headless=False).new_context(storage_state=auth_data["storage"])
    page = context.new_page()

    # Navigate to a known domain URL to initialize session storage
    base_url = "https://3rd-eye-ed-mate-qa.mpower-social.com/"
    page.goto(base_url)

    # Set the session token in session storage
    token = auth_data.get("session_token")
    if token:
        page.evaluate(
            f"""
            () => {{
                window.sessionStorage.setItem('token', '{token}');
            }}
            """
        )
        print("Session token restored.")
    yield page

    # Keep the browser open for debugging
    input("Press Enter once you're ready to exit...")
    page.context.browser.close()


# reading the saved data
def load_csv_data(file_path):
    """
    Load test data from a CSV file.
    :param file_path: Path to the CSV file.
    :return: List of dictionaries containing test data.
    """
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        return [row for row in reader]


