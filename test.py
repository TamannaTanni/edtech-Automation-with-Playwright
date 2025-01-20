import pytest
from playwright.sync_api import sync_playwright
from studentadd_kf import add_student
from add_admin import add_admin
from add_teacher import add_teacher
from create_batch import create_batch



# def testsuite(login_with_saved_state):
#         # Login and create a page instance
#         page = login_with_saved_state
#
#         # Perform test cases sequentially
#         # add_admin(page)
#         # add_teacher(page)
#         add_student(page)
#         # create_batch(page)

def test_logout(login_with_saved_state):
        # Login and create a page instance
        page = login_with_saved_state

        # wait for appear all batch list
        page.wait_for_load_state("domcontentloaded")


        page.wait_for_selector("//div[@role='button' and @aria-label='user-account']", timeout=10000)

        # Code to logout

        ##Click on profile
        page.locator("//div[@role='button' and @aria-label='user-account']").click()

        ##Click on logout button
        page.locator("//div[@role='button']//p[text()='Logout']").click()

        # Assert that the button is available
        assert page.locator("button:has-text('Sign In')").is_visible(), "Sign In button is not visible"

        print("Logout is succesfull")
