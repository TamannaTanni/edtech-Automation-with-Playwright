import pytest
from playwright.sync_api import sync_playwright
from add_student_without_batch import add_student_without_batch
from add_admin import add_admin
from add_teacher import add_teacher
from create_batch import create_batch
import json

# File to load the authentication state
auth_file = "auth_state.json"

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
    return page

def testsuite():
    with sync_playwright() as playwright:
        # Login and create a page instance
        page = login_with_saved_state(playwright)

        # Perform test cases sequentially
        #create_batch(page)

        # add_admin(page)
        # add_teacher(page)
        # add_student(page)
        create_batch(page)

        # Keep the browser open for debugging
        input("Press Enter once you're ready to exit...")
        page.context.browser.close()
