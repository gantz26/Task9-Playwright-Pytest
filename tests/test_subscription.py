import allure
import pytest
from playwright.sync_api import expect
from faker import Faker
from utils.helper import take_screenshot

@allure.feature("Subscription")
@pytest.mark.usefixtures("home_page", "cart_page")
class TestSubscription:

    @allure.title("Verify Subscription in home page")
    def test_verify_subscription_in_home_page(self, home_page):
        with allure.step("Scroll down to footer"):
            home_page.scroll_down_to_footer()
            take_screenshot(home_page.page, "Scroll down to footer")

        with allure.step("Verify text 'SUBSCRIPTION'"):
            expect(home_page.get_subscription_header()).to_be_visible()
            expect(home_page.get_subscription_header()).to_have_text("SUBSCRIPTION")

        faker = Faker()
        with allure.step("Enter email address in input and click arrow button"):
            home_page.fill_subscription_input(faker.email())
            home_page.click_subscription_button()
            take_screenshot(home_page.page, "Enter email address in input and click arrow button")

        with allure.step("Verify success message 'You have been successfully subscribed!' is visible"):
            expect(home_page.get_subscription_success_message()).to_be_visible()
            expect(home_page.get_subscription_success_message()).to_have_text("You have been successfully subscribed!")
            take_screenshot(home_page.page, "Verify success message 'You have been successfully subscribed!' is visible")

    @allure.title("Verify Subscription in cart page")
    def test_verify_subscription_in_cart_page(self, home_page, cart_page):
        with allure.step("Click 'Cart' button"):
            home_page.click_cart_button()
            expect(cart_page.get_cart_info()).to_be_visible()
            take_screenshot(home_page.page, "Click 'Cart' button")

        with allure.step("Scroll down to footer"):
            home_page.scroll_down_to_footer()
            take_screenshot(home_page.page, "Scroll down to footer")

        with allure.step("Verify text 'SUBSCRIPTION'"):
            expect(home_page.get_subscription_header()).to_be_visible()
            expect(home_page.get_subscription_header()).to_have_text("SUBSCRIPTION")

        faker = Faker()
        with allure.step("Enter email address in input and click arrow button"):
            home_page.fill_subscription_input(faker.email())
            home_page.click_subscription_button()
            take_screenshot(home_page.page, "Enter email address in input and click arrow button")

        with allure.step("Verify success message 'You have been successfully subscribed!' is visible"):
            expect(home_page.get_subscription_success_message()).to_be_visible()
            expect(home_page.get_subscription_success_message()).to_have_text("You have been successfully subscribed!")
            take_screenshot(home_page.page, "Verify success message 'You have been successfully subscribed!' is visible")