import time

from tests.data.admin_selectors import ITEM_MENU, ITEM_UNDER_MENU, ELEMENT_TITLE_H1
from tests.data.settings import URL_SHOP
from tests.data.shop_selectors import ITEM_PRODUCT, ITEM_STICKER


def test_left_menu(driver_chrome, admin_login):

    # Проход по меню
    menu_items = driver_chrome.find_elements(*ITEM_MENU)
    for i in range(len(menu_items)):
        menu_items = driver_chrome.find_elements(*ITEM_MENU)
        menu_items[i].click()
        driver_chrome.find_element(*ELEMENT_TITLE_H1)

        # Проход по подменю
        menu_under_items = driver_chrome.find_elements(*ITEM_UNDER_MENU)
        for j in range(len(menu_under_items)):
            menu_under_items = driver_chrome.find_elements(*ITEM_UNDER_MENU)
            menu_under_items[j].click()
            driver_chrome.find_element(*ELEMENT_TITLE_H1)

def test_check_sticker(driver_chrome):

    driver_chrome.get(URL_SHOP)
    products = driver_chrome.find_elements(*ITEM_PRODUCT)
    for product in products:
        product.find_element(*ITEM_STICKER)
