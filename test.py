import pytest
from playwright.sync_api import sync_playwright
from conftest import load_csv_data
from dotenv import load_dotenv
import os
from studentadd_kf import add_student
from add_admin import add_admin
from add_teacher import add_teacher
from create_batch import create_batch
from login_logout import login, logout



# Load environment variables from .env file
load_dotenv()

# def testsuite(login_with_saved_state):
#         # Login and create a page instance
#         page = login_with_saved_state
#
#         # Perform test cases sequentially
#         # add_admin(page)
#         # add_teacher(page)
#         add_student(page)
#         # create_batch(page)



def test_login_with_superadmin(browser):

    # Use super admin credentials directly from environment variables
    superadmin_username = os.getenv("admin_username")
    superadmin_password = os.getenv("admin_password")

    login(browser,superadmin_username,superadmin_password)



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
        pytest.fail(f"Test failed for {test_data['batch_name']}: {e}")


