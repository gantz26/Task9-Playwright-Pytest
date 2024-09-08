import allure
import pytest
from playwright.sync_api import expect
from random import randint
from utils.helper import take_screenshot

@allure.feature("Cart Operations")
@pytest.mark.usefixtures("home_page", "product_list_page", "product_page", "cart_page")
class TestCartOperations:

    @allure.title("Add Product to Cart")
    def test_add_product_to_cart(self, home_page, product_list_page,cart_page):
        with allure.step("Click on 'Products' button"):
            home_page.click_products_button()
            expect(product_list_page.get_all_products_header()).to_be_visible()
            take_screenshot(home_page.page, "Click on 'Products' button")

        products = [product_list_page.get_products().nth(1),
                    product_list_page.get_products().nth(2)]
        product_information = []
        for product in products:
            product_information.append({
                "name": product_list_page.get_product_name(product),
                "price": product_list_page.get_product_price(product)
            })
            with allure.step("Hover over first product and click 'Add to cart'"):
                product.hover()
                product_list_page.click_add_to_cart_button(product)
                take_screenshot(home_page.page, "Hover over first product and click 'Add to cart'")

            with allure.step("Click 'Continue Shopping' button"):
                product_list_page.click_continue_shopping_button()
                take_screenshot(home_page.page, "Click 'Continue Shopping' button")

        with allure.step("Click 'View Cart' button"):
            home_page.click_cart_button()
            expect(cart_page.get_cart_info()).to_be_visible()
            take_screenshot(home_page.page, "Click 'View Cart' button")

        with allure.step("Verify both products are added to Cart"):
            cart_products = cart_page.get_products()
            for i in range(cart_products.count()):
                with allure.step("Verify their prices, quantity and total price"):
                    take_screenshot(
                        home_page.page,
                        f"Verify both products are added to Cart: {i + 1}/{cart_products.count()}")
                    assert product_information[i]["name"] == cart_page.get_product_name(cart_products.nth(i))
                    assert product_information[i]["price"] == cart_page.get_product_price(cart_products.nth(i))
                    assert cart_page.get_product_quantity(cart_products.nth(i)) == 1
                    assert cart_page.get_product_total(cart_products.nth(i)) == product_information[i]["price"]

    @allure.title("Verify Product Quantity in Cart")
    def test_verify_product_quantity_in_cart(self, home_page, product_list_page, product_page, cart_page):
        with allure.step("Click on 'Products' button"):
            home_page.click_products_button()
            expect(product_list_page.get_all_products_header()).to_be_visible()
            take_screenshot(home_page.page, "Click on 'Products' button")

        products = product_list_page.get_products()
        product = products.nth(randint(0, products.count() - 1))
        product_information = {
            "name": product_list_page.get_product_name(product),
            "price": product_list_page.get_product_price(product)
        }

        with allure.step("Click 'View Product' for any product on home page"):
            product_list_page.click_view_product_button(product)
            take_screenshot(home_page.page, "Click 'View Product' for any product on home page")

        with allure.step("Verify product detail is opened"):
            expect(product_page.get_product_details()).to_be_visible()
            take_screenshot(home_page.page, "Verify product detail is opened")

        product_quantity = 4
        with allure.step("Increase quantity to 4"):
            product_page.fill_quantity_field(product_quantity)
            take_screenshot(home_page.page, "Increase quantity to 4")

        with allure.step("Click 'Add to cart' button"):
            product_page.click_add_to_cart_button()
            take_screenshot(home_page.page, "Click 'Add to cart' button")

        with allure.step("Click 'View Cart' button"):
            product_page.click_view_cart_button()
            expect(cart_page.get_cart_info()).to_be_visible()
            take_screenshot(home_page.page, "Click 'View Cart' button")

        with allure.step("Verify that product is displayed in cart page with exact quantity"):
            cart_product = cart_page.get_products()
            take_screenshot(home_page.page, "Verify that product is displayed in cart page with exact quantity")
            assert product_information["name"] == cart_page.get_product_name(cart_product)
            assert product_information["price"] == cart_page.get_product_price(cart_product)
            assert cart_page.get_product_quantity(cart_product) == product_quantity
            assert cart_page.get_product_total(cart_product) == product_information["price"] * product_quantity