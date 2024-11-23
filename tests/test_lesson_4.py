from tests.data.admin_selectors import ITEM_MENU, ITEM_UNDER_MENU, ELEMENT_TITLE_H1
from tests.data.settings import URL_SHOP
from tests.data.shop_selectors import ITEM_PRODUCT, ITEM_STICKER

class TestLesson4:
    def test_left_menu(self, chrome_driver, admin_login):

        # Проход по меню
        menu_items = chrome_driver.find_elements(*ITEM_MENU)
        for i in range(len(menu_items)):
            menu_items = chrome_driver.find_elements(*ITEM_MENU)
            menu_items[i].click()
            chrome_driver.find_element(*ELEMENT_TITLE_H1)

            # Проход по подменю
            menu_under_items = chrome_driver.find_elements(*ITEM_UNDER_MENU)
            for j in range(len(menu_under_items)):
                menu_under_items = chrome_driver.find_elements(*ITEM_UNDER_MENU)
                menu_under_items[j].click()
                chrome_driver.find_element(*ELEMENT_TITLE_H1)

    def test_check_sticker(self, chrome_driver):

        chrome_driver.get(URL_SHOP)
        products = chrome_driver.find_elements(*ITEM_PRODUCT)
        for product in products:
            assert len(product.find_elements(*ITEM_STICKER)) == 1, "Wrong number of stickers"
