from time import sleep

from tests.data.settings import URL_SHOP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from tests.data.shop_selectors import ITEM_PRODUCT, BUTTON_ADD_TO_CART, ITEM_QUANTITY_CART, \
    BUTTON_REMOVE_PRODUCT_FROM_CART, SELECT_CARD_SIZE


class TestLesson7:
    def test_add_product_to_basket(self, chrome_driver):
        driver = chrome_driver
        driver.get(URL_SHOP)
        wait = WebDriverWait(driver, 10)

        # Добавление товара в корзину
        for i in range(1,4):
            driver.find_elements(*ITEM_PRODUCT)[0].click()
            if size := driver.find_elements(*SELECT_CARD_SIZE):
                select = Select(size[0])
                option = select.options[-1].text
                Select(size[0]).select_by_visible_text(option)
            driver.find_element(*BUTTON_ADD_TO_CART).click()
            wait.until(EC.text_to_be_present_in_element(ITEM_QUANTITY_CART, str(i)))
            driver.back()

        # Удаление товаров из корзины
        driver.find_element(*ITEM_QUANTITY_CART).click()
        while driver.find_elements(*BUTTON_REMOVE_PRODUCT_FROM_CART):
            remove_product = driver.find_element(*BUTTON_REMOVE_PRODUCT_FROM_CART)
            remove_product.click()
            wait.until(EC.staleness_of(remove_product))
