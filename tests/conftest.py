import time

import pytest
from selenium import webdriver
from enum import Enum
from tests.data.admin_selectors import INPUT_USER_NAME, INPUT_USER_PASSWORD, BUTTON_CONFIRM, ICON_LOGOUT
from tests.data.settings import URL_ADMIN, ADMIN_NAME, ADMIN_PASSWORD


class DriverType(Enum):
    CHROME = webdriver.Chrome
    FIREFOX = webdriver.Firefox
    SAFARI = webdriver.Safari


@pytest.fixture
def create_driver(request):

    def _create_driver(driver_type):
        driver = driver_type.value()
        request.addfinalizer(driver.quit)

        return driver

    return _create_driver

@pytest.fixture
def driver_chrome(request, create_driver):

    return create_driver(DriverType.CHROME)

@pytest.fixture
def driver_firefox(request, create_driver):

    return create_driver(DriverType.FIREFOX)

@pytest.fixture
def driver_safari(request, create_driver):

    return create_driver(DriverType.SAFARI)

@pytest.fixture
def admin_login(request, driver_chrome):

    def _logout():
        driver_chrome.find_element(*ICON_LOGOUT).click()

    driver_chrome.get(URL_ADMIN)
    driver_chrome.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
    driver_chrome.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
    driver_chrome.find_element(*BUTTON_CONFIRM).click()

    request.addfinalizer(_logout)