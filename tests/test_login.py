import allure
import pytest
from playwright.sync_api import expect
from faker import Faker
from utils.helper import register_user

@allure.feature("Login")
@pytest.mark.usefixtures("home_page", "login_page")
class TestLogin:

    @allure.title("Register User")
    def test_register_user(self, home_page, login_page):
        register_user(home_page, login_page)

        with allure.step("Click 'Delete Account' button"):
            home_page.click_delete_account_button()

        with allure.step("Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button"):
            expect(home_page.get_account_deleted_header()).to_be_visible()
            home_page.click_continue_button()

    @allure.title("Login with valid credentials")
    def test_login_with_valid_credentials(self, home_page, login_page):
        user_data = register_user(home_page, login_page)

        with allure.step("Click 'Logout' button"):
            home_page.click_logout_button()

        with allure.step("Verify 'Login to your account' is visible"):
            expect(login_page.get_login_header()).to_be_visible()

        with allure.step("Enter correct email address and password and click 'Login' button"):
            login_page.login(user_data["email"], user_data["password"])

        with allure.step("Verify that 'Logged in as username' is visible"):
            expect(home_page.get_logged_in_user(user_data["first_name"]))

        with allure.step("Click 'Delete Account' button"):
            home_page.click_delete_account_button()

        with allure.step("Verify that 'ACCOUNT DELETED!' is visible"):
            expect(home_page.get_account_deleted_header()).to_be_visible()

    @allure.title("Login with invalid credentials")
    def test_login_with_invalid_credentials(self, home_page, login_page):
        register_user(home_page, login_page)

        with allure.step("Click 'Logout' button"):
            home_page.click_logout_button()

        with allure.step("Verify 'Login to your account' is visible"):
            expect(login_page.get_login_header()).to_be_visible()

        faker = Faker()
        with allure.step("Enter incorrect email address and password and click 'Login' button"):
            login_page.login(faker.email(), faker.password())

        with allure.step("Verify error 'Your email or password is incorrect!' is visible"):
            expect(login_page.get_login_error_message()).to_be_visible()

    @allure.title("Logout")
    def test_logout(self, home_page, login_page):
        register_user(home_page, login_page)

        with allure.step("Click 'Logout' button"):
            home_page.click_logout_button()

        with allure.step("Verify that user is navigated to login page"):
            expect(login_page.get_login_header()).to_be_visible()

    @allure.title("Register with existing email")
    def test_register_with_existing_email(self, home_page, login_page):
        user_data = register_user(home_page, login_page)

        with allure.step("Click 'Logout' button"):
            home_page.click_logout_button()

        with allure.step("Verify 'New User Signup!' is visible"):
            expect(login_page.get_login_header()).to_be_visible()

        with allure.step("Enter name and already registered email address and click 'Signup' button"):
            login_page.signup(user_data["first_name"], user_data["email"])

        with allure.step("Verify error 'Email Address already exist!' is visible"):
            expect(login_page.get_signup_error_message()).to_be_visible()