import pytest
from playwright.sync_api import sync_playwright
from conftest import load_csv_data
from dotenv import load_dotenv
import os
from add_student_without_batch import add_student_without_batch
from add_admin import add_admin
from add_teacher import add_teacher
from create_batch import create_batch
from login_logout import login, logout



# Load environment variables from .env file
load_dotenv()

# Global variables to store credentials and information
new_admin_credentials = {}
new_teacher_credentials = {}
new_student_credentials = []
new_batch_information = {}

# @pytest.mark.skip(reason="already logged")
def test_login_with_superadmin(browser):

    # Use super admin credentials directly from environment variables
    superadmin_username = os.getenv("admin_username")
    superadmin_password = os.getenv("admin_password")

    login(browser,superadmin_username,superadmin_password)


# @pytest.mark.skip(reason="admin already added")
@pytest.mark.dependency(name="add_admin")
@pytest.mark.parametrize("test_data", load_csv_data("new_admin_data.csv"))
def test_add_admin_with_csv_data(login_with_saved_state, test_data):
    """
        Test admin creation using data from CSV.
    """
    global new_admin_credentials
    try:

        # Login and create a page instance
        page = login_with_saved_state
        page.wait_for_timeout(3000)

        # Perform test cases sequentially
        add_admin(page, test_data)

        # Save the credentials in a global variable
        new_admin_credentials['username'] = test_data["username"]
        new_admin_credentials['password'] = test_data["password"]

        # Additional validation can be added here if applicable
        assert True, f"Admin created successfully for {test_data['first_name']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['first_name']}: {e}")

    logout(login_with_saved_state)



# @pytest.mark.skip(reason="already logged in")
@pytest.mark.dependency(name="admin_login")
@pytest.mark.dependency(depends=["add_admin"])
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


# @pytest.mark.skip(reason="teacher already added")
@pytest.mark.dependency(depends=["admin_login"])
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
        new_teacher_credentials['name'] = f'{test_data["first_name"]} {test_data["last_name"]}'
        new_teacher_credentials['username'] = test_data["username"]
        new_teacher_credentials['password'] = test_data["password"]

        # Additional validation can be added here if applicable
        assert True, f"Teacher created successfully for {test_data['first_name']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['first_name']}: {e}")



# @pytest.mark.skip(reason="student already added")
@pytest.mark.dependency(depends=["admin_login"])
@pytest.mark.parametrize("test_data", load_csv_data("new_student_without_batch_data.csv"))
def test_add_student_with_csv_data(login_with_saved_state, test_data):
    """
        Test student creation using data from CSV.
    """
    global new_student_credentials
    try:
        # Login and create a page instance
        page = login_with_saved_state

        # Perform test cases sequentially
        add_student_without_batch(page, test_data)

        # Save the credentials in a global variable
        new_student_credentials.append(test_data["firstName"])

        # Additional validation can be added here if applicable
        assert True, f"Student created successfully for {test_data['firstName']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['firstName']}: {e}")
    print(new_student_credentials)


@pytest.mark.dependency(depends=["admin_login"])
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
        create_batch(page, test_data)

        # Save the credentials in a global variable
        new_batch_information[test_data["batch_name"]] = {
            "batch_name": test_data["batch_name"],
            "teacher_name": test_data["teacher_name"],
        }

        # Additional validation can be added here if applicable
        assert True, f"Service recorded successfully for {test_data['batch_name']}."

    except Exception as e:
        pytest.fail(f"Test failed for {test_data['batch_name']}: {e}")


