from playwright.sync_api import Locator
from pages.base_page import BasePage
import random

NAME_INPUT = "input[data-qa=\"signup-name\"]"
EMAIL_INPUT = "input[data-qa=\"signup-email\"]"
EMAIL_LOGIN_INPUT = "input[data-qa=\"login-email\"]"
PASSWORD_LOGIN_INPUT = "input[data-qa=\"login-password\"]"
LOGIN_BUTTON = "button[data-qa=\"login-button\"]"
SIGNUP_BUTTON = "button[data-qa=\"signup-button\"]"
ACCOUNT_CREATED_HEADER = "h2[data-qa=\"account-created\"]"
PASSWORD_INPUT = "input[data-qa=\"password\"]"
DAY_SELECTOR = "#days"
MONTH_SELECTOR = "#months"
YEAR_SELECTOR = "#years"
NEWSLETTER_CHECKBOX = "#newsletter"
OFFERS_CHECKBOX = "#optin"
GENDER_1 = "#id_gender1"
GENDER_2 = "#id_gender2"
FIRST_NAME_INPUT = "#first_name"
LAST_NAME_INPUT = "#last_name"
COMPANY_INPUT = "#company"
ADDRESS_1_INPUT = "#address1"
ADDRESS_2_INPUT = "#address2"
COUNTRY_SELECTOR = "#country"
STATE_INPUT = "#state"
CITY_INPUT = "#city"
ZIPCODE_INPUT = "#zipcode"
MOBILE_NUMBER_INPUT = "#mobile_number"
CREATE_ACCOUNT_BUTTON = "button[data-qa=\"create-account\"]"
CONTINUE_BUTTON = "a[data-qa=\"continue-button\"]"

class LoginPage(BasePage):
    def get_signup_header(self) -> Locator:
        return self.page.get_by_text("New User Signup!")

    def get_login_header(self) -> Locator:
        return self.page.get_by_text("Login to your account")

    def get_login_error_message(self) -> Locator:
        return self.page.get_by_text("Your email or password is incorrect!")

    def get_signup_error_message(self) -> Locator:
        return self.page.get_by_text("Email Address already exist!")

    def get_name_input(self) -> Locator:
        return self.page.locator(NAME_INPUT)

    def get_email_input(self) -> Locator:
        return self.page.locator(EMAIL_INPUT)

    def get_signup_button(self) -> Locator:
        return self.page.locator(SIGNUP_BUTTON)

    def get_account_info_header(self) -> Locator:
        return self.page.get_by_text("Enter Account Information")

    def get_password_input(self) -> Locator:
        return self.page.locator(PASSWORD_INPUT)

    def get_day_selector(self) -> Locator:
        return self.page.locator(DAY_SELECTOR)

    def get_month_selector(self) -> Locator:
        return self.page.locator(MONTH_SELECTOR)

    def get_year_selector(self) -> Locator:
        return self.page.locator(YEAR_SELECTOR)

    def get_newsletter_checkbox(self) -> Locator:
        return self.page.locator(NEWSLETTER_CHECKBOX)

    def get_offers_checkbox(self) -> Locator:
        return self.page.locator(OFFERS_CHECKBOX)

    def get_first_name_input(self) -> Locator:
        return self.page.locator(FIRST_NAME_INPUT)

    def get_last_name_input(self) -> Locator:
        return self.page.locator(LAST_NAME_INPUT)

    def get_company_input(self) -> Locator:
        return self.page.locator(COMPANY_INPUT)

    def get_address_1_input(self) -> Locator:
        return self.page.locator(ADDRESS_1_INPUT)

    def get_address_2_input(self) -> Locator:
        return self.page.locator(ADDRESS_2_INPUT)

    def get_country_selector(self) -> Locator:
        return self.page.locator(COUNTRY_SELECTOR)

    def get_state_input(self) -> Locator:
        return self.page.locator(STATE_INPUT)

    def get_city_input(self) -> Locator:
        return self.page.locator(CITY_INPUT)

    def get_zipcode_input(self) -> Locator:
        return self.page.locator(ZIPCODE_INPUT)

    def get_mobile_number_input(self) -> Locator:
        return self.page.locator(MOBILE_NUMBER_INPUT)

    def get_create_account_button(self) -> Locator:
        return self.page.locator(CREATE_ACCOUNT_BUTTON)

    def get_account_created_header(self) -> Locator:
        return self.page.locator(ACCOUNT_CREATED_HEADER)

    def get_continue_button(self) -> Locator:
        return  self.page.locator(CONTINUE_BUTTON)

    def get_email_login_input(self) -> Locator:
        return self.page.locator(EMAIL_LOGIN_INPUT)

    def get_password_login_input(self) -> Locator:
        return self.page.locator(PASSWORD_LOGIN_INPUT)

    def get_login_button(self) -> Locator:
        return self.page.locator(LOGIN_BUTTON)

    def click_login_button(self) -> None:
        self.get_login_button().click()

    def click_continue_button(self) -> None:
        self.get_continue_button().click()

    def click_create_account_button(self) -> None:
        self.get_create_account_button().click()

    def select_title(self) -> None:
        gender_1 = self.page.locator(GENDER_1)
        gender_2 = self.page.locator(GENDER_2)
        choice = random.choice([0, 1])

        if choice == 1:
            gender_1.click()
        else:
            gender_2.click()

    def check_newsletter_checkbox(self) -> None:
        self.get_newsletter_checkbox().check()

    def check_offers_checkbox(self) -> None:
        self.get_offers_checkbox().check()

    def select_day(self) -> None:
        count_of_options = self.get_day_selector().locator("option").count()
        index_of_option = random.randint(1, count_of_options - 1)
        self.get_day_selector().select_option(index=index_of_option)

    def select_month(self) -> None:
        count_of_options = self.get_month_selector().locator("option").count()
        index_of_option = random.randint(1, count_of_options - 1)
        self.get_month_selector().select_option(index=index_of_option)

    def select_year(self) -> None:
        count_of_options = self.get_year_selector().locator("option").count()
        index_of_option = random.randint(1, count_of_options - 1)
        self.get_year_selector().select_option(index=index_of_option)

    def signup(self, name: str, email: str) -> None:
        self.get_name_input().fill(name)
        self.get_email_input().fill(email)
        self.get_signup_button().click()

    def login(self, email: str, password: str) -> None:
        self.fill_email_login_input(email)
        self.fill_password_login_input(password)
        self.click_login_button()

    def fill_email_login_input(self, email: str) -> None:
        self.get_email_login_input().fill(email)

    def fill_password_login_input(self, password: str) -> None:
        self.get_password_login_input().fill(password)

    def fill_password_input(self, password: str) -> None:
        self.get_password_input().fill(password)

    def fill_first_name_input(self, first_name: str) -> None:
        self.get_first_name_input().fill(first_name)

    def fill_last_name_input(self, last_name: str) -> None:
        self.get_last_name_input().fill(last_name)

    def fill_company_input(self, company: str) -> None:
        self.get_company_input().fill(company)

    def fill_address_1_input(self, address: str) -> None:
        self.get_address_1_input().fill(address)

    def fill_address_2_input(self, address: str) -> None:
        self.get_address_2_input().fill(address)

    def select_country(self) -> None:
        count_of_options = self.get_country_selector().locator("option").count()
        index_of_option = random.randint(1, count_of_options - 1)
        self.get_country_selector().select_option(index=index_of_option)

    def fill_state_input(self, state: str) -> None:
        self.get_state_input().fill(state)

    def fill_city_input(self, city: str) -> None:
        self.get_city_input().fill(city)

    def fill_zipcode_input(self, zipcode: str) -> None:
        self.get_zipcode_input().fill(zipcode)

    def fill_mobile_number_input(self, mobile_number: str) -> None:
        self.get_mobile_number_input().fill(mobile_number)

    def fill_account_info(self, password: str) -> None:
        self.select_title()
        self.fill_password_input(password)
        self.select_day()
        self.select_month()
        self.select_year()
        self.check_newsletter_checkbox()
        self.check_offers_checkbox()

    def fill_address_info(self, first_name: str, last_name: str, company: str,
                          address_1: str, address_2: str, state: str,
                          city: str, zipcode: str, mobile_number: str) -> None:
        self.fill_first_name_input(first_name)
        self.fill_last_name_input(last_name)
        self.fill_company_input(company)
        self.fill_address_1_input(address_1)
        self.fill_address_2_input(address_2)
        self.select_country()
        self.fill_state_input(state)
        self.fill_city_input(city)
        self.fill_zipcode_input(zipcode)
        self.fill_mobile_number_input(mobile_number)