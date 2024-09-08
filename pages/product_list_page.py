from playwright.sync_api import Locator
from pages.base_page import BasePage

PRODUCT_LIST = ".features_items"
PRODUCT = ".col-sm-4"
VIEW_PRODUCT_BUTTON = "a[href^=\"/product_details/\"]"
ADD_TO_CART_BUTTON = ".product-overlay .btn.btn-default.add-to-cart"
SEARCH_INPUT = "#search_product"
SEARCH_BUTTON = "#submit_search"
CONTINUE_SHOPPING_BUTTON = ".btn.btn-success.close-modal.btn-block"

class ProductListPage(BasePage):
    def get_all_products_header(self) -> Locator:
        return self.page.get_by_text("All Products")

    def get_searched_products_header(self) -> Locator:
        return self.page.get_by_text("Searched Products")

    def get_product_list(self) -> Locator:
        return self.page.locator(PRODUCT_LIST)

    def get_products(self) -> Locator:
        return self.page.locator(PRODUCT)

    def get_search_input(self) -> Locator:
        return self.page.locator(SEARCH_INPUT)

    def get_search_button(self) -> Locator:
        return self.page.locator(SEARCH_BUTTON)

    def get_continue_shopping_button(self) -> Locator:
        return self.page.locator(CONTINUE_SHOPPING_BUTTON)

    def get_view_product_button(self, product: Locator) -> Locator:
        return product.locator(VIEW_PRODUCT_BUTTON)

    def get_product_name(self, product: Locator) -> str:
        return product.locator("p").first.inner_text().replace('\xa0', '')

    def get_product_price(self, product: Locator) -> int:
        return int(product.locator("h2").first.inner_text().removeprefix("Rs. "))

    def get_add_to_cart_button(self, product: Locator) -> Locator:
        return product.locator(ADD_TO_CART_BUTTON)

    def fill_search_input(self, text: str) -> None:
        self.get_search_input().fill(text)

    def click_continue_shopping_button(self) -> None:
        self.get_continue_shopping_button().click()

    def click_search_button(self) -> None:
        self.get_search_button().click()

    def click_add_to_cart_button(self, product: Locator) -> None:
        self.get_add_to_cart_button(product).click()

    def click_view_product_button(self, product: Locator) -> None:
        self.get_view_product_button(product).click()