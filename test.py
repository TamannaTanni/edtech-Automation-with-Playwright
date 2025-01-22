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

# Global variables to store new admin credentials
new_admin_credentials = {}

# Global variables to store new teacher credentials
new_teacher_credentials = {}

# Global variables to store new student credentials
new_student_credentials = {}

# Global variables to store new batch information
new_batch_information = {}

def test_login_with_superadmin(browser):

    # Use super admin credentials directly from environment variables
    superadmin_username = os.getenv("admin_username")
    superadmin_password = os.getenv("admin_password")

    login(browser,superadmin_username,superadmin_password)

@pytest.mark.parametrize("test_data", load_csv_data("new_admin_data.csv"))
def test_add_admin_with_csv_data(login_with_saved_state, test_data):
    """
        Test admin creation using data from CSV.
    """
    global new_admin_credentials
    try:
        # Login and create a page instance
        page = login_with_saved_state

        # Perform test cases sequentially
        add_admin(page, test_data)

        # Save the credentials in a global variable
        new_admin_credentials['username'] = test_data["username"]
        new_admin_credentials['password'] = test_data["password"]

        # Additional validation can be added here if applicable
        assert True, f"Admin created successfully for {test_data['admin_name']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['admin_name']}: {e}")

def test_login_with_newadmin(browser):
    """
        Test login with the new admin credentials.
    """
    global new_admin_credentials
    if not new_admin_credentials:
        pytest.fail("No admin credentials found from the previous test.")

    admin_username = new_admin_credentials.get('username')
    admin_password = new_admin_credentials.get('password')

    # Use the stored credentials to log in
    login(browser, admin_username, admin_password)


@pytest.mark.parametrize("test_data", load_csv_data("new_teacher_data.csv"))
def test_add_teacher_with_csv_data(login_with_saved_state, test_data):
    """
        Test teacher creation using data from CSV.
    """
    global new_teacher_credentials
    try:
        # Login and create a page instance
        page = login_with_saved_state

        # Perform test cases sequentially
        add_teacher(page, test_data)

        # Save the credentials in a global variable
        new_teacher_credentials['name'] = test_data["name"]
        new_teacher_credentials['username'] = test_data["username"]
        new_teacher_credentials['password'] = test_data["password"]

        # Additional validation can be added here if applicable
        assert True, f"Teacher created successfully for {test_data['teacher_name']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['teacher_name']}: {e}")


@pytest.mark.parametrize("test_data", load_csv_data("new_student_data.csv"))
def test_add_student_with_csv_data(login_with_saved_state, test_data):
    """
        Test student creation using data from CSV.
    """
    global new_student_credentials
    try:
        # Login and create a page instance
        page = login_with_saved_state

        # Perform test cases sequentially
        add_student(page, test_data)

        # Save the credentials in a global variable
        new_student_credentials['name'] = test_data["name"]

        # Additional validation can be added here if applicable
        assert True, f"Student created successfully for {test_data['student_name']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['student_name']}: {e}")



@pytest.mark.parametrize("test_data", load_csv_data("new_batch_data.csv"))
def test_create_batch_with_csv_data( login_with_saved_state, test_data):
    """
        Test batch creation using data from CSV.
    """

    global new_batch_information

    try:
        # Login and create a page instance
        page = login_with_saved_state

        # Perform test cases sequentially
        batch_name, teacher_name = create_batch(page, test_data)

        # Save the credentials in a global variable
        new_batch_information['batch_name'] = test_data["batch_name"]
        new_batch_information['teacher_name'] = test_data["teacher_name"]

        # Additional validation can be added here if applicable
        assert True, f"Service recorded successfully for {test_data['batch_name']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['batch_name']}: {e}")


