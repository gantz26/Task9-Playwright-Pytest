import allure
import pytest
from playwright.sync_api import expect
from utils.helper import take_screenshot

@allure.feature("Page Verification")
@pytest.mark.usefixtures("home_page", "test_cases_page",
                         "product_list_page", "product_page")
class TestPageVerification:

    @allure.title("Verify Test Cases Page")
    def test_verify_test_cases_paged(self, home_page, test_cases_page):
        with allure.step("Click on 'Test Cases' button"):
            home_page.click_test_case_button()
            take_screenshot(home_page.page, "Click on 'Test Cases' button")

        with allure.step("Verify user is navigated to test cases page successfully"):
            expect(test_cases_page.get_header()).to_be_visible()
            take_screenshot(test_cases_page.page, "Verify user is navigated to test cases page successfully")

    @allure.title("Verify All Products and product detail page")
    def test_all_products_and_product_detail_page(self, home_page, product_list_page,
                                                  product_page):
        with allure.step("Click on 'Products' button"):
            home_page.click_products_button()
            take_screenshot(home_page.page, "Click on 'Products' button")

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            expect(product_list_page.get_all_products_header()).to_be_visible()
            take_screenshot(product_list_page.page, "Verify user is navigated to ALL PRODUCTS page successfully")

        with allure.step("The products list is visible"):
            expect(product_list_page.get_product_list()).to_be_visible()
            take_screenshot(product_list_page.page, "The products list is visible")

        first_product = product_list_page.get_products().nth(1)
        with allure.step("Click on 'View Product' of first product"):
            product_list_page.click_view_product_button(first_product)
            take_screenshot(product_list_page.page, "Click on 'View Product' of first product")

        with allure.step("User is landed to product detail page"):
            expect(product_page.get_product_details()).to_be_visible()
            take_screenshot(product_page.page, "User is landed to product detail page")

        with allure.step("Verify that detail detail is visible: product name, category, price,"
                         "availability, condition, brand"):
            take_screenshot(product_page.page, "Verify that detail detail is visible: product name, category, price, etc.")
            expect(product_page.get_product_name()).to_be_visible()
            expect(product_page.get_product_category()).to_be_visible()
            expect(product_page.get_product_price()).to_be_visible()
            expect(product_page.get_product_quantity()).to_be_visible()
            expect(product_page.get_product_availability()).to_be_visible()
            expect(product_page.get_product_condition()).to_be_visible()
            expect(product_page.get_product_brand()).to_be_visible()

    @allure.title("Search Product")
    def test_search_product(self, home_page, product_list_page):
        with allure.step("Click on 'Products' button"):
            home_page.click_products_button()
            take_screenshot(home_page.page, "Click on 'Products' button")

        with allure.step("Verify user is navigated to ALL PRODUCTS page successfully"):
            expect(product_list_page.get_all_products_header()).to_be_visible()
            take_screenshot(product_list_page.page, "Verify user is navigated to ALL PRODUCTS page successfully")

        searched_product = "jeans"
        with allure.step("Enter product name in search input and click search button"):
            product_list_page.fill_search_input(searched_product)
            product_list_page.click_search_button()
            take_screenshot(product_list_page.page, "Enter product name in search input and click search button")

        with allure.step("Verify 'SEARCHED PRODUCTS' is visible"):
            expect(product_list_page.get_searched_products_header()).to_be_visible()
            take_screenshot(product_list_page.page, "Verify 'SEARCHED PRODUCTS' is visible")

        with allure.step("Verify all the products related to search are visible"):
            take_screenshot(product_list_page.page, "Verify all the products related to search are visible")
            products = product_list_page.get_products()
            for i in range(1, products.count()):
                product = products.nth(i)
                expect(product).to_contain_text(searched_product, ignore_case=True)