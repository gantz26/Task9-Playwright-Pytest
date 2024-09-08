import allure
import pytest
from playwright.sync_api import expect
from faker import Faker
from utils.helper import take_screenshot

@allure.feature("Contact Us Form")
@pytest.mark.usefixtures("home_page", "contact_us_page")
class TestContactForm:

    @allure.title("Contact us form")
    def test_contact_us_form(self, home_page, contact_us_page):
        with allure.step("Click on 'Contact Us' button"):
            home_page.click_contact_us_button()

        with allure.step("Verify 'GET IN TOUCH' is visible"):
            expect(contact_us_page.get_in_touch_header()).to_be_visible()
            take_screenshot(home_page.page, "Verify 'GET IN TOUCH' is visible")

        faker = Faker()
        name = faker.first_name()
        email = faker.email()
        subject = faker.word()
        message = ' '.join(faker.words(5))
        path_file = "data/file.txt"

        with open(path_file, "w") as file:
            file.write(' '.join(faker.words(10)))

        with allure.step("Enter name, email, subject, message, upload file and Click 'Submit' button"):
            contact_us_page.fill_contact_us_form(name, email, subject,
                                             message, path_file)
            take_screenshot(home_page.page, "Enter name, email, subject, message, upload file and Click 'Submit' button")

        with allure.step("Verify success message 'Success! Your details have been submitted successfully.' is visible"):
            expect(contact_us_page.get_success_message()).to_be_visible()
            expect(contact_us_page.get_success_message()).to_have_text("Success! Your details have been submitted successfully.")
            take_screenshot(home_page.page, "Verify success message 'Success! Your details have been submitted successfully.' is visible")

        with allure.step("Click 'Home' button and verify that landed to home page successfully"):
            contact_us_page.click_home_button()
            assert home_page.get_title() == "Automation Exercise"
            take_screenshot(home_page.page, "Click 'Home' button and verify that landed to home page successfully")