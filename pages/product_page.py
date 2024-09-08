from playwright.sync_api import Locator
from pages.base_page import BasePage

PRODUCTS_DETAILS = ".product-details"
PRODUCT_NAME = ".product-information h2"
PRODUCT_INFO = ".product-information p"
PRODUCT_PRICE = ".product-information span span"
PRODUCT_QUANTITY = "#quantity"
ADD_TO_CART_BUTTON = ".btn.btn-default.cart"
VIEW_CART_BUTTON = ".modal-content >> a[href=\"/view_cart\"]"

class ProductPage(BasePage):
    def get_product_details(self) -> Locator:
        return self.page.locator(PRODUCTS_DETAILS)

    def get_product_name(self) -> Locator:
        return self.page.locator(PRODUCT_NAME)

    def get_product_category(self) -> Locator:
        return self.page.locator(PRODUCT_INFO).filter(has_text="Category")

    def get_product_price(self) -> Locator:
        return self.page.locator(PRODUCT_PRICE)

    def get_product_quantity(self) -> Locator:
        return self.page.locator(PRODUCT_QUANTITY)

    def get_add_to_cart_button(self) -> Locator:
        return self.page.locator(ADD_TO_CART_BUTTON)

    def get_view_cart_button(self) -> Locator:
        return self.page.locator(VIEW_CART_BUTTON)

    def get_product_availability(self) -> Locator:
        return self.page.locator(PRODUCT_INFO).filter(has_text="Availability")

    def get_product_condition(self) -> Locator:
        return self.page.locator(PRODUCT_INFO).filter(has_text="Condition")

    def get_product_brand(self) -> Locator:
        return self.page.locator(PRODUCT_INFO).filter(has_text="Brand")

    def fill_quantity_field(self, value: int) -> None:
        self.get_product_quantity().fill(str(value))

    def click_add_to_cart_button(self) -> None:
        self.get_add_to_cart_button().click()

    def click_view_cart_button(self) -> None:
        self.get_view_cart_button().click()