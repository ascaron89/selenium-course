import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.data.admin_selectors import INPUT_USER_PASSWORD
from tests.data.settings import URL_SHOP
from tests.data.shop_selectors import (
    LINK_USER_CREATE,
    LINK_USER_LOGOUT,
    INPUT_USER_EMAIL,
    BUTTON_USER_LOGIN,
    INPUT_CREATE_FIRST_NAME,
    INPUT_CREATE_LAST_NAME,
    INPUT_CREATE_ADDRESS_1,
    INPUT_CREATE_POST_CODE,
    INPUT_CREATE_CITY,
    INPUT_CREATE_EMAIL,
    INPUT_CREATE_PASSWORD,
    INPUT_CREATE_CONFIRM_PASSWORD,
    INPUT_CREATE_PHONE,
    SELECT_CREATE_COUNTRY,
    SELECT_CREATE_STATE,
    BUTTON_CREATE_ACCOUNT
)


def test_create_user(chrome_driver):
    driver = chrome_driver
    driver.get(URL_SHOP)
    password = str(int(time.time()))
    email = f'test@{password}test.com'

    # Переход к форме создания пользователя
    driver.find_element(*LINK_USER_CREATE).click()

    # Заполнение формы создания пользователя
    driver.find_element(*INPUT_CREATE_FIRST_NAME).send_keys('test_first_name')
    driver.find_element(*INPUT_CREATE_LAST_NAME).send_keys('test_last_name')
    driver.find_element(*INPUT_CREATE_ADDRESS_1).send_keys('test_address_1')
    driver.find_element(*INPUT_CREATE_POST_CODE).send_keys('12345')
    driver.find_element(*INPUT_CREATE_CITY).send_keys('test_city')
    driver.find_element(*INPUT_CREATE_PHONE).send_keys('+11234567890')
    Select(driver.find_element(*SELECT_CREATE_COUNTRY)).select_by_value('US')
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(SELECT_CREATE_STATE))
    Select(driver.find_element(*SELECT_CREATE_STATE)).select_by_value('AK')
    driver.find_element(*INPUT_CREATE_EMAIL).send_keys(email)
    driver.find_element(*INPUT_CREATE_PASSWORD).send_keys(password)
    driver.find_element(*INPUT_CREATE_CONFIRM_PASSWORD).send_keys(password)
    driver.find_element(*BUTTON_CREATE_ACCOUNT).click()

    # Разлогинивание пользователя
    driver.find_element(*LINK_USER_LOGOUT).click()

    # Авторизация созданного пользователя
    driver.find_element(*INPUT_USER_EMAIL).send_keys(email)
    driver.find_element(*INPUT_USER_PASSWORD).send_keys(password)
    driver.find_element(*BUTTON_USER_LOGIN).click()

    # Повторное разлогинивание пользователя
    driver.find_element(*LINK_USER_LOGOUT).click()
