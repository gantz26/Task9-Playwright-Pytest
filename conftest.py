import pytest
import allure
from playwright.sync_api import Page, expect
from pages.home_page import HomePage
from pages.test_cases_page import TestCasesPage
from pages.login_page import LoginPage
from pages.contact_us_page import ContactUsPage
from pages.product_list_page import ProductListPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="function", autouse=True)
@allure.step("Before each test")
def before_each(page: Page):
    home_page = HomePage(page)

    with allure.step("Navigate to site"):
        home_page.open()
    with allure.step("Verify that home page is visible successfully"):
        expect(page).to_have_title("Automation Exercise")

@pytest.fixture()
def home_page(page: Page):
    return HomePage(page)

@pytest.fixture()
def test_cases_page(page: Page):
    return TestCasesPage(page)

@pytest.fixture()
def login_page(page: Page):
    return LoginPage(page)

@pytest.fixture()
def contact_us_page(page: Page):
    return ContactUsPage(page)

@pytest.fixture()
def product_list_page(page: Page):
    return ProductListPage(page)

@pytest.fixture()
def product_page(page: Page):
    return ProductPage(page)

@pytest.fixture()
def cart_page(page: Page):
    return CartPage(page)

@pytest.fixture()
def checkout_page(page: Page):
    return CheckoutPage(page)