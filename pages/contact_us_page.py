from playwright.sync_api import Locator
from pages.base_page import BasePage

NAME_INPUT = "input[data-qa=\"name\"]"
EMAIL_INPUT = "input[data-qa=\"email\"]"
SUBJECT_INPUT = "input[data-qa=\"subject\"]"
MESSAGE_INPUT = "#message"
UPLOAD_INPUT = "input[name=\"upload_file\"]"
SUBMIT_BUTTON = "input[data-qa=\"submit-button\"]"
SUCCESS_MESSAGE = ".status.alert.alert-success"
HOME_BUTTON = ".btn.btn-success"

class ContactUsPage(BasePage):
    def get_in_touch_header(self) -> Locator:
        return self.page.get_by_text("Get In Touch")

    def get_name_input(self) -> Locator:
        return self.page.locator(NAME_INPUT)

    def get_email_input(self) -> Locator:
        return self.page.locator(EMAIL_INPUT)

    def get_subject_input(self) -> Locator:
        return self.page.locator(SUBJECT_INPUT)

    def get_message_input(self) -> Locator:
        return self.page.locator(MESSAGE_INPUT)

    def get_upload_input(self) -> Locator:
        return self.page.locator(UPLOAD_INPUT)

    def get_submit_button(self) -> Locator:
        return self.page.locator(SUBMIT_BUTTON)

    def get_success_message(self) -> Locator:
        return self.page.locator(SUCCESS_MESSAGE)

    def get_home_button(self) -> Locator:
        return self.page.locator(HOME_BUTTON)

    def fill_name_input(self, name: str) -> None:
        self.get_name_input().fill(name)

    def fill_email_input(self, email: str) -> None:
        self.get_email_input().fill(email)

    def fill_subject_input(self, subject: str) -> None:
        self.get_subject_input().fill(subject)

    def fill_message_input(self, message: str) -> None:
        self.get_message_input().fill(message)

    def fill_upload_input(self, file_path: str) -> None:
        self.get_upload_input().set_input_files(file_path)

    def click_submit_button(self) -> None:
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.wait_for_load_state("load")
        self.get_submit_button().click()


    def click_home_button(self) -> None:
        self.get_home_button().click()

    def fill_contact_us_form(self, name: str, email: str, subject: str,
                             message: str, file_path: str) -> None:
        self.fill_name_input(name)
        self.fill_email_input(email)
        self.fill_subject_input(subject)
        self.fill_message_input(message)
        self.fill_upload_input(file_path)
        self.click_submit_button()