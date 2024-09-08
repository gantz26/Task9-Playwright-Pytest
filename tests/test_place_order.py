import allure
import pytest
from playwright.sync_api import expect
from utils.helper import register_user, take_screenshot
from faker import Faker

@allure.feature("Place Order")
@pytest.mark.usefixtures("home_page", "product_list_page", "login_page", "cart_page", "checkout_page")
class TestPlaceOrder:

    @allure.title("Place Order: Register while Checkout")
    def test_place_order_register_while_checkout(self, home_page, product_list_page, login_page,
                                                 cart_page, checkout_page):
        with allure.step("Click on 'Products' button"):
            home_page.click_products_button()
            expect(product_list_page.get_all_products_header()).to_be_visible()
            take_screenshot(home_page.page, "Click on 'Products' button")

        products = [product_list_page.get_products().nth(1),
                    product_list_page.get_products().nth(2)]
        product_information = []
        with allure.step("Add products to cart"):
            for product in products:
                product_information.append({
                    "name": product_list_page.get_product_name(product),
                    "price": product_list_page.get_product_price(product),
                    "quantity": 1
                })
                product.hover()
                product_list_page.click_add_to_cart_button(product)
                product_list_page.click_continue_shopping_button()
                take_screenshot(home_page.page, "Add products to cart")

        with allure.step("Click 'Cart' button"):
            home_page.click_cart_button()
            take_screenshot(home_page.page, "Click 'Cart' button")

        with allure.step("Verify that cart page is displayed"):
            expect(cart_page.get_cart_info()).to_be_visible()
            take_screenshot(home_page.page, "Verify that cart page is displayed")

        with allure.step("Click Proceed To Checkout"):
            cart_page.click_proceed_to_checkout_button()
            take_screenshot(home_page.page, "Click Proceed To Checkout")

        with allure.step("Click 'Register / Login' button"):
            cart_page.click_login_button()
            take_screenshot(home_page.page, "Click 'Register / Login' button")

        with allure.step("Register new user"):
            user_data = register_user(home_page, login_page)
            take_screenshot(home_page.page, "Register new user")

        with allure.step("Click 'Cart' button"):
            home_page.click_cart_button()
            take_screenshot(home_page.page, "Click 'Cart' button")

        with allure.step("Click 'Proceed To Checkout' button"):
            cart_page.click_proceed_to_checkout_button()
            take_screenshot(home_page.page, "Click 'Proceed To Checkout' button")

        with allure.step("Verify Address Details and Review Your Order"):
            take_screenshot(home_page.page, "Verify Address Details and Review Your Order")
            expect(checkout_page.get_address_details_header()).to_be_visible()
            expect(checkout_page.get_review_order_header()).to_be_visible()

            full_name = checkout_page.get_full_name_label().split(" ")
            assert full_name[1] == user_data["first_name"]
            assert full_name[2] == user_data["last_name"]
            assert checkout_page.get_company_label() == user_data["company"]
            assert checkout_page.get_address_1_label() == user_data["address_1"]
            assert checkout_page.get_address_2_label() == user_data["address_2"]
            country_info = checkout_page.get_county_info_label()
            assert country_info == user_data["city"] + " " + user_data["state"] + " " + user_data["zipcode"]
            assert checkout_page.get_phone_numer_label() == user_data["mobile_number"]

            cart_products = checkout_page.get_products()
            actual_total_price = 0
            for i in range(cart_products.count() - 1):
                assert product_information[i]["name"] == cart_page.get_product_name(cart_products.nth(i))
                assert product_information[i]["price"] == cart_page.get_product_price(cart_products.nth(i))
                assert cart_page.get_product_quantity(cart_products.nth(i)) == 1
                assert cart_page.get_product_total(cart_products.nth(i)) == product_information[i]["price"]
                actual_total_price += product_information[i]["price"]

            assert checkout_page.get_total_price() == actual_total_price

        faker = Faker()
        with allure.step("Enter description in comment text area and click 'Place Order'"):
            checkout_page.fill_text_area(" ".join(faker.words(10)))
            checkout_page.click_place_order_button()
            take_screenshot(home_page.page, "Enter description in comment text area and click 'Place Order'")

        with allure.step("Enter payment details: Name on Card, Card Number, CVC, Expiration date"):
            checkout_page.fill_name_on_card_input(user_data["first_name"])
            checkout_page.fill_card_number_input(faker.credit_card_number())
            checkout_page.fill_card_cvc_input(faker.credit_card_security_code())
            checkout_page.fill_card_expiry_month_input(faker.credit_card_expire(start="now", end="+5y", date_format="%m"))
            checkout_page.fill_card_expiry_year_input(faker.credit_card_expire(start="now", end="+5y", date_format="%Y"))
            take_screenshot(home_page.page, "Enter payment details: Name on Card, Card Number, CVC, Expiration date")

        with allure.step("Click 'Pay and Confirm Order' button"):
            checkout_page.click_confirm_button()
            take_screenshot(home_page.page, "Click 'Pay and Confirm Order' button")

        with allure.step("Verify that order placed successfully"):
            take_screenshot(home_page.page, "Verify that order placed successfully")
            expect(checkout_page.get_success_message()).to_be_visible()
            expect(checkout_page.get_success_message()).to_have_text("Order Placed!")

        with allure.step("Click 'Delete Account' button"):
            home_page.click_delete_account_button()
            take_screenshot(home_page.page, "Click 'Delete Account' button")

        with allure.step("Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
            take_screenshot(home_page.page, "Verify 'ACCOUNT DELETED!' and click 'Continue' button")
            expect(home_page.get_account_deleted_header()).to_be_visible()

    @allure.title("Place Order: Register before Checkout")
    def test_place_order_register_before_checkout(self, home_page, product_list_page, login_page,
                                                 cart_page, checkout_page):
        with allure.step("Register new user"):
            user_data = register_user(home_page, login_page)
            take_screenshot(home_page.page, "Register new user")

        with allure.step("Click on 'Products' button"):
            take_screenshot(home_page.page, "Click on 'Products' button")
            home_page.click_products_button()
            expect(product_list_page.get_all_products_header()).to_be_visible()

        products = [product_list_page.get_products().nth(1),
                    product_list_page.get_products().nth(2)]
        product_information = []
        with allure.step("Add products to cart"):
            take_screenshot(home_page.page, "Add products to cart")
            for product in products:
                product_information.append({
                    "name": product_list_page.get_product_name(product),
                    "price": product_list_page.get_product_price(product),
                    "quantity": 1
                })
                product.hover()
                product_list_page.click_add_to_cart_button(product)
                product_list_page.click_continue_shopping_button()

        with allure.step("Click 'Cart' button"):
            home_page.click_cart_button()
            take_screenshot(home_page.page, "Click 'Cart' button")

        with allure.step("Verify that cart page is displayed"):
            take_screenshot(home_page.page, "Verify that cart page is displayed")
            expect(cart_page.get_cart_info()).to_be_visible()

        with allure.step("Click 'Proceed To Checkout' button"):
            cart_page.click_proceed_to_checkout_button()
            take_screenshot(home_page.page, "Click 'Proceed To Checkout' button")

        with allure.step("Verify Address Details and Review Your Order"):
            take_screenshot(home_page.page, "Verify Address Details and Review Your Order")
            expect(checkout_page.get_address_details_header()).to_be_visible()
            expect(checkout_page.get_review_order_header()).to_be_visible()

            full_name = checkout_page.get_full_name_label().split(" ")
            assert full_name[1] == user_data["first_name"]
            assert full_name[2] == user_data["last_name"]
            assert checkout_page.get_company_label() == user_data["company"]
            assert checkout_page.get_address_1_label() == user_data["address_1"]
            assert checkout_page.get_address_2_label() == user_data["address_2"]
            country_info = checkout_page.get_county_info_label()
            assert country_info == user_data["city"] + " " + user_data["state"] + " " + user_data["zipcode"]
            assert checkout_page.get_phone_numer_label() == user_data["mobile_number"]

            cart_products = checkout_page.get_products()
            actual_total_price = 0
            for i in range(cart_products.count() - 1):
                assert product_information[i]["name"] == cart_page.get_product_name(cart_products.nth(i))
                assert product_information[i]["price"] == cart_page.get_product_price(cart_products.nth(i))
                assert cart_page.get_product_quantity(cart_products.nth(i)) == 1
                assert cart_page.get_product_total(cart_products.nth(i)) == product_information[i]["price"]
                actual_total_price += product_information[i]["price"]

            assert checkout_page.get_total_price() == actual_total_price

        faker = Faker()

        with allure.step("Enter description in comment text area and click 'Place Order'"):
            checkout_page.fill_text_area(" ".join(faker.words(10)))
            checkout_page.click_place_order_button()
            take_screenshot(home_page.page, "Enter description in comment text area and click 'Place Order'")

        with allure.step("Enter payment details: Name on Card, Card Number, CVC, Expiration date"):
            checkout_page.fill_name_on_card_input(user_data["first_name"])
            checkout_page.fill_card_number_input(faker.credit_card_number())
            checkout_page.fill_card_cvc_input(faker.credit_card_security_code())
            checkout_page.fill_card_expiry_month_input(faker.credit_card_expire(start="now", end="+5y", date_format="%m"))
            checkout_page.fill_card_expiry_year_input(faker.credit_card_expire(start="now", end="+5y", date_format="%Y"))
            take_screenshot(home_page.page, "Enter payment details: Name on Card, Card Number, CVC, Expiration date")

        with allure.step("Click 'Pay and Confirm Order' button"):
            checkout_page.click_confirm_button()
            take_screenshot(home_page.page, "Click 'Pay and Confirm Order' button")

        with allure.step("Verify that order placed successfully"):
            take_screenshot(home_page.page, "Verify that order placed successfully")
            expect(checkout_page.get_success_message()).to_be_visible()
            expect(checkout_page.get_success_message()).to_have_text("Order Placed!")

        with allure.step("Click 'Delete Account' button"):
            home_page.click_delete_account_button()
            take_screenshot(home_page.page, "Click 'Delete Account' button")

        with allure.step("Verify 'ACCOUNT DELETED!' and click 'Continue' button"):
            take_screenshot(home_page.page, "Verify 'ACCOUNT DELETED!' and click 'Continue' button")
            expect(home_page.get_account_deleted_header()).to_be_visible()