import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser, be
from selene.support.conditions import have
import allure

LOGIN = "andrey@zavrichko.dev"
PASSWORD = "kyvL2$DqcbRTLh5"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_add_to_cart_api():
    """Successful authorization to some demowebshop (API)"""
    with step("Login with API"):
        result = requests.post(
            url=API_URL + "/login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
    with step("Get cookie from API"):
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")
    with step("Add to cart"):
        add_to_cart = requests.post(
            url=API_URL + "addproducttocart/catalog/31/1/1",
            cookies={"NOPCOMMERCE.AUTH": cookie})
        assert add_to_cart.json()["success"]
    with step("Set cookie from API"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)

    with step("Verify successful add to cart"):
        browser.element(".cart-qty").should(have.text("(1)"))


def test_add_to_cart_book_api():
    """Successful authorization to some demowebshop (API)"""
    with step("Login with API"):
        result = requests.post(
            url=API_URL + "/login",
            data={"Email": LOGIN, "Password": PASSWORD, "RememberMe": False},
            allow_redirects=False
        )
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
    with step("Get cookie from API"):
        cookie = result.cookies.get("NOPCOMMERCE.AUTH")
    with step("Add to cart"):
        add_to_cart = requests.post(
            url=API_URL + "addproducttocart/catalog/45/1/1",
            cookies={"NOPCOMMERCE.AUTH": cookie})
        assert add_to_cart.json()["success"]
    with step("Add to cart"):
        add_to_cart = requests.post(
            url=API_URL + "addproducttocart/catalog/22/1/1",
            cookies={"NOPCOMMERCE.AUTH": cookie})
        assert add_to_cart.json()["success"]
    with step("Set cookie from API"):
        browser.open(WEB_URL)
        browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": cookie})
        browser.open(WEB_URL)
    with step("Verify successful add to cart"):
        browser.element(".cart-qty").should(have.text("(2)"))
    with step("Delete cart"):
        browser.element('#topcartlink').click()
        browser.element('td.remove-from-cart input[type=checkbox]').should(
            be.visible).click()
        browser.element('td.remove-from-cart input[type=checkbox]').should(
            be.visible).click()
        browser.element('.update-cart-button').click()