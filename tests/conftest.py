from collections.abc import Callable
from typing import Union

import pytest
from enum import Enum

from selenium.webdriver import Chrome, Firefox, Safari
from selenium.webdriver.ie.webdriver import WebDriver

from elements.driver import Driver, DriverType
from tests.data.admin_selectors import INPUT_USER_NAME, INPUT_USER_PASSWORD, BUTTON_CONFIRM, ICON_LOGOUT
from tests.data.settings import URL_ADMIN, ADMIN_NAME, ADMIN_PASSWORD


@pytest.fixture(scope="class")
def chrome_driver(request) -> Chrome:
    driver = Driver(DriverType.CHROME).driver
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture(scope="class")
def firefox_driver(request) -> Firefox:
    driver = Driver(DriverType.FIREFOX).driver
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture(scope="class")
def safari_driver(request) -> Safari:
    driver = Driver(DriverType.SAFARI).driver
    request.addfinalizer(driver.quit)
    return driver


@pytest.fixture
def admin_login(request, chrome_driver):

    def _logout():
        chrome_driver.find_element(*ICON_LOGOUT).click()

    chrome_driver.get(URL_ADMIN)
    chrome_driver.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
    chrome_driver.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
    chrome_driver.find_element(*BUTTON_CONFIRM).click()

    request.addfinalizer(_logout)

@pytest.fixture
def custom_admin_login(request):
    def _login(driver: WebDriver) -> Callable[WebDriver]:
        driver.get(URL_ADMIN)
        driver.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
        driver.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
        driver.find_element(*BUTTON_CONFIRM).click()

    return _login