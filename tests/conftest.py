import pytest
from selene import browser
import allure
from utils.tools import get_auth_cookie, add_auth_cookie


@pytest.fixture(scope='session', autouse=True)
def set_browser():
    with allure.step('Browser config'):
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    with allure.step('Add authorization cookie'):
        get_auth_cookie()
        add_auth_cookie()

    yield browser

    with allure.step('Close browser'):
        browser.quit()
