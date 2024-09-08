from pages.base_page import BasePage
from playwright.sync_api import Locator

CART_INFO = "#cart_info"
PRODUCTS = "#cart_info >> tbody > tr"
PRODUCT_NAME = ".cart_description >> a[href^=\"/product_details/\"]"
PRODUCT_PRICE = ".cart_price > p"
PRODUCT_QUANTITY = ".cart_quantity > button"
PRODUCT_TOTAL = ".cart_total > .cart_total_price"
PROCEED_CHECKOUT_BUTTON = ".btn.btn-default.check_out"
LOGIN_BUTTON = ".modal-content >> a[href=\"/login\"]"

class CartPage(BasePage):
    def get_cart_info(self) -> Locator:
        return self.page.locator(CART_INFO)

    def get_proceed_to_checkout_button(self) -> Locator:
        return self.page.locator(PROCEED_CHECKOUT_BUTTON)

    def get_login_button(self) -> Locator:
        return self.page.locator(LOGIN_BUTTON)

    def get_products(self) -> Locator:
        return self.page.locator(PRODUCTS)

    def get_product_name(self, product: Locator) -> str:
        return product.locator(PRODUCT_NAME).inner_text().replace('\xa0', '')

    def get_product_price(self, product: Locator) -> int:
        return int(product.locator(PRODUCT_PRICE).inner_text().removeprefix("Rs. "))

    def get_product_quantity(self, product: Locator) -> int:
        return int(product.locator(PRODUCT_QUANTITY).inner_text())

    def get_product_total(self, product: Locator) -> int:
        return int(product.locator(PRODUCT_TOTAL).inner_text().removeprefix("Rs. "))

    def click_proceed_to_checkout_button(self) -> None:
        self.get_proceed_to_checkout_button().click()

    def click_login_button(self) -> None:
        self.get_login_button().click()