import allure
from faker import Faker
from playwright.sync_api import expect, Page
from pages.home_page import HomePage
from pages.login_page import LoginPage

def generate_user_data() -> dict[str, str]:
    faker = Faker()
    return {
        "first_name": faker.first_name(),
        "last_name": faker.last_name(),
        "email": faker.email(),
        "password": faker.password(),
        "company": faker.company(),
        "address_1": faker.address().replace('\n', ' '),
        "address_2": faker.address().replace('\n', ' '),
        "state": faker.state(),
        "city": faker.city(),
        "zipcode": faker.zipcode(),
        "mobile_number": faker.phone_number()
    }

def register_user(home_page: HomePage, login_page: LoginPage) -> dict[str, str]:
    user_data = generate_user_data()

    with allure.step("Click on 'Signup / Login' button"):
        home_page.click_login_signup_button()

    with allure.step("Verify 'New User Signup!' is visible"):
        expect(login_page.get_signup_header()).to_be_visible()
        take_screenshot(login_page.page, "Verify 'New User Signup!' is visible")

    with allure.step("Enter name and email address and click 'Signup' button"):
        login_page.signup(user_data["first_name"], user_data["email"])
        take_screenshot(login_page.page, "Enter name and email address and click 'Signup' button")

    with allure.step("Verify that 'ENTER ACCOUNT INFORMATION' is visible"):
        expect(login_page.get_account_info_header()).to_be_visible()
        take_screenshot(login_page.page, "Verify that 'ENTER ACCOUNT INFORMATION' is visible")

    with allure.step("Fill details: Title, Name, Email, Password, Date of birth,"
                     "First name, Last name, Company, Address, Address2, Country, State, City, Zipcode, Mobile Number"
                     "and select checkboxes"):
        login_page.fill_account_info(user_data["password"])
        login_page.fill_address_info(
            user_data["first_name"], user_data["last_name"], user_data["company"],
            user_data["address_1"], user_data["address_2"], user_data["state"],
            user_data["city"], user_data["zipcode"], user_data["mobile_number"]
        )
        take_screenshot(login_page.page, "Fill details: Title, Name, Email, Password, Date of birth, etc.")

    with allure.step("Click 'Create Account button'"):
        login_page.click_create_account_button()

    with allure.step("Verify that 'ACCOUNT CREATED!' is visible"):
        expect(login_page.get_account_created_header()).to_be_visible()
        take_screenshot(login_page.page, "Verify that 'ACCOUNT CREATED!' is visible")

    with allure.step("Click 'Continue' button"):
        login_page.click_continue_button()

    with allure.step("Verify that 'Logged in as username' is visible"):
        expect(home_page.get_logged_in_user(user_data["first_name"])).to_be_visible()
        take_screenshot(home_page.page, "Verify that 'Logged in as username' is visible")

    return user_data

def take_screenshot(page: Page, name: str):
    allure.attach(
        body=page.screenshot(full_page=True),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )