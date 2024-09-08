import allure
import pytest
from playwright.sync_api import expect
from faker import Faker
from utils.helper import register_user, take_screenshot

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
            take_screenshot(home_page.page, "account_deleted")
            home_page.click_continue_button()

    @allure.title("Login with valid credentials")
    def test_login_with_valid_credentials(self, home_page, login_page):
        user_data = register_user(home_page, login_page)

        with allure.step("Click 'Logout' button"):
            home_page.click_logout_button()

        with allure.step("Verify 'Login to your account' is visible"):
            expect(login_page.get_login_header()).to_be_visible()
            take_screenshot(login_page.page, "Verify 'Login to your account' is visible")

        with allure.step("Enter correct email address and password and click 'Login' button"):
            login_page.login(user_data["email"], user_data["password"])
            take_screenshot(login_page.page, "login_success")

        with allure.step("Verify that 'Logged in as username' is visible"):
            expect(home_page.get_logged_in_user(user_data["first_name"]))
            take_screenshot(home_page.page, "Logged in as username")

        with allure.step("Click 'Delete Account' button"):
            home_page.click_delete_account_button()

        with allure.step("Verify that 'ACCOUNT DELETED!' is visible"):
            expect(home_page.get_account_deleted_header()).to_be_visible()
            take_screenshot(home_page.page, "account_deleted")

    @allure.title("Login with invalid credentials")
    def test_login_with_invalid_credentials(self, home_page, login_page):
        register_user(home_page, login_page)

        with allure.step("Click 'Logout' button"):
            home_page.click_logout_button()

        with allure.step("Verify 'Login to your account' is visible"):
            expect(login_page.get_login_header()).to_be_visible()
            take_screenshot(login_page.page, "Verify 'Login to your account' is visible")

        faker = Faker()
        with allure.step("Enter incorrect email address and password and click 'Login' button"):
            login_page.login(faker.email(), faker.password())
            take_screenshot(login_page.page, "login_failed")

        with allure.step("Verify error 'Your email or password is incorrect!' is visible"):
            expect(login_page.get_login_error_message()).to_be_visible()
            take_screenshot(login_page.page, "Your email or password is incorrect!")

    @allure.title("Logout")
    def test_logout(self, home_page, login_page):
        register_user(home_page, login_page)

        with allure.step("Click 'Logout' button"):
            home_page.click_logout_button()

        with allure.step("Verify that user is navigated to login page"):
            expect(login_page.get_login_header()).to_be_visible()
            take_screenshot(login_page.page, "user_is_navigated_to_login_page")

    @allure.title("Register with existing email")
    def test_register_with_existing_email(self, home_page, login_page):
        user_data = register_user(home_page, login_page)

        with allure.step("Click 'Logout' button"):
            home_page.click_logout_button()

        with allure.step("Verify 'New User Signup!' is visible"):
            expect(login_page.get_login_header()).to_be_visible()
            take_screenshot(login_page.page, "Verify 'New User Signup!' is visible")

        with allure.step("Enter name and already registered email address and click 'Signup' button"):
            login_page.signup(user_data["first_name"], user_data["email"])
            take_screenshot(login_page.page, "Enter name and already registered email address and click 'Signup' button")

        with allure.step("Verify error 'Email Address already exist!' is visible"):
            expect(login_page.get_signup_error_message()).to_be_visible()
            take_screenshot(login_page.page, "error_email_address_already_exist")