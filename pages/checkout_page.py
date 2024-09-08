from playwright.sync_api import Locator
from pages.base_page import BasePage

FULL_NAME_LABEL = "#address_delivery >> .address_firstname.address_lastname"
COMPANY_LABEL = "#address_delivery >> .address_address1.address_address2"
ADDRESS_1_LABEL = "#address_delivery >> .address_address1.address_address2"
ADDRESS_2_LABEL = "#address_delivery >> .address_address1.address_address2"
COUNTY_INFO_LABEL = "#address_delivery >> .address_city.address_state_name.address_postcode"
PHONE_NUMER_LABEL = "#address_delivery >> .address_phone"
PRODUCTS = "#cart_info >> tbody > tr"
PRODUCT_NAME = ".cart_description >> a[href^=\"/product_details/\"]"
PRODUCT_PRICE = ".cart_price > p"
PRODUCT_QUANTITY = ".cart_quantity > button"
PRODUCT_TOTAL = ".cart_total > .cart_total_price"
TOTAL_PRICE = "#cart_info >> .cart_total_price"
TEXT_AREA = "textarea.form-control"
PLACE_ORDER_BUTTON = ".btn.btn-default.check_out"
NAME_ON_CARD_INPUT = "input[data-qa=\"name-on-card\"]"
CARD_NUMBER_INPUT = "input[data-qa=\"card-number\"]"
CARD_CVC_INPUT = "input[data-qa=\"cvc\"]"
CARD_EXPIRY_MONTH_INPUT = "input[data-qa=\"expiry-month\"]"
CARD_EXPIRY_YEAR_INPUT = "input[data-qa=\"expiry-year\"]"
CONFIRM_BUTTON = "#submit"
SUCCESS_MESSAGE = "h2[data-qa=\"order-placed\"]"

class CheckoutPage(BasePage):
    def get_address_details_header(self) -> Locator:
        return self.page.get_by_text("Address Details")

    def get_review_order_header(self) -> Locator:
        return self.page.get_by_text("Review Your Order")

    def get_payment_header(self) -> Locator:
        return self.page.get_by_text("Payment")

    def get_success_message(self) -> Locator:
        return self.page.locator(SUCCESS_MESSAGE)

    def get_name_on_card_input(self) -> Locator:
        return self.page.locator(NAME_ON_CARD_INPUT)

    def get_card_number_input(self) -> Locator:
        return self.page.locator(CARD_NUMBER_INPUT)

    def get_card_cvc_input(self) -> Locator:
        return self.page.locator(CARD_CVC_INPUT)

    def get_card_expiry_month_input(self) -> Locator:
        return self.page.locator(CARD_EXPIRY_MONTH_INPUT)

    def get_card_expiry_year_input(self) -> Locator:
        return self.page.locator(CARD_EXPIRY_YEAR_INPUT)

    def get_confirm_button(self) -> Locator:
        return self.page.locator(CONFIRM_BUTTON)

    def get_place_order_button(self) -> Locator:
        return self.page.locator(PLACE_ORDER_BUTTON)

    def get_text_area(self) -> Locator:
        return self.page.locator(TEXT_AREA)

    def get_full_name_label(self) -> str:
        return self.page.locator(FULL_NAME_LABEL).inner_text()

    def get_company_label(self) -> str:
        return self.page.locator(COMPANY_LABEL).first.inner_text()

    def get_address_1_label(self) -> str:
        return self.page.locator(ADDRESS_1_LABEL).nth(1).inner_text()

    def get_address_2_label(self) -> str:
        return self.page.locator(ADDRESS_2_LABEL).last.inner_text()

    def get_county_info_label(self) -> str:
        return self.page.locator(COUNTY_INFO_LABEL).inner_text()

    def get_phone_numer_label(self) -> str:
        return self.page.locator(PHONE_NUMER_LABEL).inner_text()

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

    def get_total_price(self) -> int:
        return int(self.page.locator(TOTAL_PRICE).last.inner_text().removeprefix("Rs. "))

    def fill_text_area(self, text: str) -> None:
        self.get_text_area().fill(text)

    def fill_name_on_card_input(self, name: str) -> None:
        self.get_name_on_card_input().fill(name)

    def fill_card_number_input(self, card_number: str) -> None:
        self.get_card_number_input().fill(card_number)

    def fill_card_cvc_input(self, cvc: str) -> None:
        self.get_card_cvc_input().fill(cvc)

    def fill_card_expiry_month_input(self, expiry_month: str) -> None:
        self.get_card_expiry_month_input().fill(expiry_month)

    def fill_card_expiry_year_input(self, expiry_year: str) -> None:
        self.get_card_expiry_year_input().fill(expiry_year)

    def click_place_order_button(self) -> None:
        self.get_place_order_button().click()

    def click_confirm_button(self) -> None:
        self.get_confirm_button().click()