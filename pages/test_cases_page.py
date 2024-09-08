from playwright.sync_api import Locator
from pages.base_page import BasePage

HEADER = "h2.title.text-center"

class TestCasesPage(BasePage):
    def get_header(self) -> Locator:
        return self.page.locator(HEADER)