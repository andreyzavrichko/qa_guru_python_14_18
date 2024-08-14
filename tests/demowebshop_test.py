import allure
from allure_commons._allure import step
from selene import browser, be
from selene.support.conditions import have
from tests.api_call import api_call
from utils.data import WEB_URL


@allure.title("Test add to cart")
def test_add_to_cart_api():
    with step("Add to cart"):
        api_call.add_item_to_cart("/31/1/1")

    with step("Open browser"):
        browser.open(WEB_URL)

    with step("Verify successful add to cart"):
        browser.element(".cart-qty").should(have.text("(1)"))
        browser.element('#topcartlink').click()
        browser.element(".product-unit-price").should(have.text("1590.00"))
        browser.element(".product-name").should(have.text("14.1-inch Laptop"))


@allure.title("Test add book to cart")
def test_add_to_cart_book_api():
    with step("Add to cart"):
        api_call.add_item_to_cart("/45/1/1")
        api_call.add_item_to_cart("/22/1/1")

    with step("Open browser"):
        browser.open(WEB_URL)

    with step("Verify successful add to cart"):
        browser.element(".cart-qty").should(have.text("(2)"))


