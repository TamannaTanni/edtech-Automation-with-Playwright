import pytest
from playwright.sync_api import sync_playwright
from studentadd_kf import add_student
from add_admin import add_admin
from add_teacher import add_teacher
from create_batch import create_batch
from conftest import load_csv_data



# def testsuite(login_with_saved_state):
#         # Login and create a page instance
#         page = login_with_saved_state
#
#         # Perform test cases sequentially
#         # add_admin(page)
#         # add_teacher(page)
#         add_student(page)
#         # create_batch(page)



@pytest.mark.parametrize("test_data", load_csv_data("new_batch_data.csv"))
def test_create_batch_with_csv_data( login_with_saved_state, test_data):
    """
        Test batch creation using data from CSV.
    """
    try:
        # Login and create a page instance
        page = login_with_saved_state

        # Perform test cases sequentially
        create_batch(page, test_data)

        # Additional validation can be added here if applicable
        assert True, f"Service recorded successfully for {test_data['name']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['name']}: {e}")

# def test_logout(login_with_saved_state):
#         # Login and create a page instance
#         page = login_with_saved_state
#
#         # wait for appear all batch list
#         page.wait_for_load_state("domcontentloaded")
#
#
#         page.wait_for_selector("//div[@role='button' and @aria-label='user-account']", timeout=10000)
#
#         # Code to logout
#
#         ##Click on profile
#         page.locator("//div[@role='button' and @aria-label='user-account']").click()
#
#         ##Click on logout button
#         page.locator("//div[@role='button']//p[text()='Logout']").click()
#
#         # Assert that the button is available
#         assert page.locator("button:has-text('Sign In')").is_visible(), "Sign In button is not visible"
#
#         print("Logout is succesfull")

