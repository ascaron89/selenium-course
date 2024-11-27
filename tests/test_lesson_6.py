import time
from pathlib import Path

import pytest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.table import Table
from tests.conftest import chrome_driver

from tests.data.admin_selectors import INPUT_USER_PASSWORD
from tests.data.catalog_selectors import (
    BUTTON_ADD_NEW_PRODUCT,
    TAB_GENERAL,
    RADIO_PRODUCT_STATUS_ENABLE,
    INPUT_PRODUCT_NAME,
    INPUT_PRODUCT_CODE,
    CHECKBOX_PRODUCT_CATEGORIES_RUBBER_DUCKS,
    SELECT_PRODUCT_DEFAULT_CATEGORY,
    CHECKBOX_PRODUCT_GENDER_UNISEX,
    INPUT_PRODUCT_QUANTITY,
    FILE_PRODUCT_UPLOAD_IMAGES,
    TAB_INFORMATION,
    SELECT_PRODUCT_MANUFACTURE,
    INPUT_PRODUCT_KEYWORDS,
    INPUT_PRODUCT_SHORT_DESCRIPTION,
    TEXTAREA_PRODUCT_DESCRIPTION,
    INPUT_PRODUCT_HEAD_TITLE,
    INPUT_PRODUCT_META_DESCRIPTION,
    TAB_PRICE,
    INPUT_PRODUCT_PURCHASE_PRICE,
    SELECT_PRODUCT_PURCHASE_CURRENCY,
    INPUT_PRODUCT_PRICE_USD,
    INPUT_PRODUCT_PRICE_EUR,
    BUTTON_SAVE_PRODUCT
)
from tests.data.settings import URL_SHOP, CATALOG_PAGE
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
    SELECT_CREATE_STATE,
    BUTTON_CREATE_ACCOUNT, ITEM_OPENER_SELECT_CREATE_COUNTRY, ITEM_OPTION_US
)

class TestLesson6:
    @pytest.mark.parametrize(
        'driver', ['chrome_driver', 'firefox_driver', 'safari_driver'],
        ids=['chrome', 'firefox', 'safari']
    )
    def test_create_user(self, request, driver):

        driver = request.getfixturevalue(driver)
        wait = WebDriverWait(driver, 10)
        driver.get(URL_SHOP)
        password = str(int(time.time()))
        email = f'test@{password}test.com'

        # Переход к форме создания пользователя
        driver.find_element(*LINK_USER_CREATE).click()

        # Заполнение формы создания пользователя

        wait.until(EC.visibility_of_element_located(INPUT_CREATE_FIRST_NAME)).send_keys('test_first_name')
        driver.find_element(*INPUT_CREATE_LAST_NAME).send_keys('test_last_name')
        driver.find_element(*INPUT_CREATE_ADDRESS_1).send_keys('test_address_1')
        driver.find_element(*INPUT_CREATE_POST_CODE).send_keys('12345')
        driver.find_element(*INPUT_CREATE_CITY).send_keys('test_city')
        driver.find_element(*INPUT_CREATE_PHONE).send_keys('+11234567890')
        driver.find_element(*ITEM_OPENER_SELECT_CREATE_COUNTRY).click()
        driver.find_element(*ITEM_OPTION_US).click()
        wait.until(EC.element_to_be_clickable(SELECT_CREATE_STATE))
        Select(driver.find_element(*SELECT_CREATE_STATE)).select_by_value('AK')
        driver.find_element(*INPUT_CREATE_EMAIL).send_keys(email)
        driver.find_element(*INPUT_CREATE_PASSWORD).send_keys(password)
        driver.find_element(*INPUT_CREATE_CONFIRM_PASSWORD).send_keys(password)
        driver.find_element(*BUTTON_CREATE_ACCOUNT).click()

        # Разлогинивание пользователя
        wait.until(EC.visibility_of_element_located(LINK_USER_LOGOUT)).click()

        # Авторизация созданного пользователя
        wait.until(EC.visibility_of_element_located(INPUT_USER_EMAIL)).send_keys(email)
        driver.find_element(*INPUT_USER_PASSWORD).send_keys(password)
        driver.find_element(*BUTTON_USER_LOGIN).click()

        # Повторное разлогинивание пользователя
        wait.until(EC.visibility_of_element_located(LINK_USER_LOGOUT)).click()

    def test_create_product(self, chrome_driver, admin_login):
        driver = chrome_driver
        driver.get(CATALOG_PAGE)
        wait = WebDriverWait(driver, 10)
        file_path = Path(__file__).resolve().parent.parent / 'duck_image.jpg'

        # Открываем форму добавления нового продукта
        driver.find_element(*BUTTON_ADD_NEW_PRODUCT).click()

        # Заполняем вкладку General
        driver.find_element(*TAB_GENERAL).click()
        wait.until(EC.visibility_of_element_located(RADIO_PRODUCT_STATUS_ENABLE))
        driver.find_element(*RADIO_PRODUCT_STATUS_ENABLE).click()
        driver.find_element(*INPUT_PRODUCT_NAME).send_keys("test_duck")
        driver.find_element(*INPUT_PRODUCT_CODE).send_keys("1234567890")
        driver.find_element(*CHECKBOX_PRODUCT_CATEGORIES_RUBBER_DUCKS).click()
        Select(driver.find_element(*SELECT_PRODUCT_DEFAULT_CATEGORY)).select_by_visible_text("Rubber Ducks")
        driver.find_element(*CHECKBOX_PRODUCT_GENDER_UNISEX).click()
        driver.find_element(*INPUT_PRODUCT_QUANTITY).clear()
        driver.find_element(*INPUT_PRODUCT_QUANTITY).send_keys("100")
        driver.find_element(*FILE_PRODUCT_UPLOAD_IMAGES).send_keys(str(file_path))

        # Заполняем вкладку Information
        driver.find_element(*TAB_INFORMATION).click()
        wait.until(EC.visibility_of_element_located(SELECT_PRODUCT_MANUFACTURE))
        Select(driver.find_element(*SELECT_PRODUCT_MANUFACTURE)).select_by_visible_text("ACME Corp.")
        driver.find_element(*INPUT_PRODUCT_KEYWORDS).send_keys("duck")
        driver.find_element(*INPUT_PRODUCT_SHORT_DESCRIPTION).send_keys("test duck")
        driver.find_element(*TEXTAREA_PRODUCT_DESCRIPTION).send_keys("test duck")
        driver.find_element(*INPUT_PRODUCT_HEAD_TITLE).send_keys("test duck")
        driver.find_element(*INPUT_PRODUCT_META_DESCRIPTION).send_keys("test duck")

        # Заполняем вкладку Price
        driver.find_element(*TAB_PRICE).click()
        wait.until(EC.visibility_of_element_located(INPUT_PRODUCT_PURCHASE_PRICE))
        driver.find_element(*INPUT_PRODUCT_PURCHASE_PRICE).clear()
        driver.find_element(*INPUT_PRODUCT_PURCHASE_PRICE).send_keys("15")
        Select(driver.find_element(*SELECT_PRODUCT_PURCHASE_CURRENCY)).select_by_value("USD")
        driver.find_element(*INPUT_PRODUCT_PRICE_USD).send_keys("20")
        driver.find_element(*INPUT_PRODUCT_PRICE_EUR).send_keys("20")

        # Сохраняем новый товар
        driver.find_element(*BUTTON_SAVE_PRODUCT).click()

        # Проверяем товар
        catalog_table = Table(chrome_driver)
        products = catalog_table.get_table_data()
        products_name = [product["Name"][0] for product in products]
        assert "test_duck" in products_name, "Test item not found."