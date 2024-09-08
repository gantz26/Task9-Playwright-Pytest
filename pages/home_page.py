from playwright.sync_api import Locator
from pages.base_page import BasePage

ACCOUNT_DELETED_HEADER = "h2[data-qa=\"account-deleted\"]"
LOGIN_SIGNUP_BUTTON = "li >> a[href=\"/login\"]"
TEST_CASE_BUTTON = "li >> a[href=\"/test_cases\"]"
PRODUCTS_BUTTON = "li >> a[href=\"/products\"]"
CART_BUTTON = "li >> a[href=\"/view_cart\"]"
DELETE_ACCOUNT_BUTTON = "li >> a[href=\"/delete_account\"]"
LOGOUT_BUTTON = "li >> a[href=\"/logout\"]"
CONTACT_US_BUTTON = "li >> a[href=\"/contact_us\"]"
CONTINUE_BUTTON = "a[data-qa=\"continue-button\"]"
FOOTER = ".footer-widget"
SUBSCRIPTION_INPUT = "#susbscribe_email"
SUBSCRIPTION_BUTTON = "#subscribe"
SUBSCRIPTION_SUCCESS_MESSAGE = "#success-subscribe"

class HomePage(BasePage):
    def open(self) -> None:
        self.page.goto("/")

    def get_products_button(self) -> Locator:
        return self.page.locator(PRODUCTS_BUTTON)

    def get_title(self) -> str:
        return self.page.title()

    def get_login_signup_button(self) -> Locator:
        return self.page.locator(LOGIN_SIGNUP_BUTTON)

    def get_test_case_button(self) -> Locator:
        return self.page.locator(TEST_CASE_BUTTON)

    def get_delete_account_button(self) -> Locator:
        return self.page.locator(DELETE_ACCOUNT_BUTTON)

    def get_account_deleted_header(self) -> Locator:
        return self.page.locator(ACCOUNT_DELETED_HEADER)

    def get_continue_button(self) -> Locator:
        return self.page.locator(CONTINUE_BUTTON)

    def get_logged_in_user(self, username: str) -> Locator:
        return self.page.get_by_text(f"Logged in as {username}")

    def get_logout_button(self) -> Locator:
        return self.page.locator(LOGOUT_BUTTON)

    def get_contact_us_button(self) -> Locator:
        return self.page.locator(CONTACT_US_BUTTON)

    def get_subscription_header(self) -> Locator:
        return self.page.locator(FOOTER).get_by_text("Subscription")

    def get_subscription_input(self) -> Locator:
        return self.page.locator(SUBSCRIPTION_INPUT)

    def get_subscription_button(self) -> Locator:
        return self.page.locator(SUBSCRIPTION_BUTTON)

    def get_subscription_success_message(self) -> Locator:
        return self.page.locator(SUBSCRIPTION_SUCCESS_MESSAGE)

    def get_cart_button(self) -> Locator:
        return self.page.locator(CART_BUTTON)

    def fill_subscription_input(self, email: str) -> None:
        self.get_subscription_input().fill(email)

    def click_cart_button(self) -> None:
        self.get_cart_button().click()

    def click_subscription_button(self) -> None:
        self.get_subscription_button().click()

    def click_products_button(self) -> None:
        self.get_products_button().click()

    def click_contact_us_button(self) -> None:
        self.get_contact_us_button().click()

    def click_logout_button(self) -> None:
        self.get_logout_button().click()

    def click_continue_button(self) -> None:
        self.get_continue_button().click()

    def click_delete_account_button(self) -> None:
        self.get_delete_account_button().click()

    def click_login_signup_button(self) -> None:
        self.get_login_signup_button().click()

    def click_test_case_button(self) -> None:
        self.get_test_case_button().click()

    def scroll_down_to_footer(self) -> None:
        self.page.locator(FOOTER).scroll_into_view_if_needed()