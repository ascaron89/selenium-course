from time import sleep

import pytest

from elements.table import Table
from tests.conftest import chrome_driver
from tests.data.settings import (
    COUNTRIES_PAGE,
    GEO_ZONES_PAGE,
    URL_SHOP
)
from tests.data.shop_selectors import (
    BOX_CAMPAIGNS,
    CARD,
    CARD_NAME,
    ITEM_PRODUCT,
    ITEM_NAME,
    ITEM_PRICE,
    ITEM_CAMPAIGN_PRICE,
)

class TestLesson5:
    def test_sorting_countries_zones(self, chrome_driver, admin_login):

        chrome_driver.get(COUNTRIES_PAGE)

        # Проверяем сортировку данных в таблице стран
        country_table = Table(chrome_driver)
        countries = country_table.get_table_data()
        countries_name = [country["Name"] for country in countries]
        assert countries_name == sorted(countries_name), "Sort error"

        # Проверяем сортировку данных в таблицах стран
        for i in range(len(country_table.table_rows)):
            row = country_table.table_rows[i]
            data_row = country_table.get_row_data(row)
            if int(data_row["Zones"][0]):
                country_table.edit_row(row)
                states_table = Table(chrome_driver)
                states = states_table.get_table_data()
                states_name = [state["Name"] for state in states]
                assert states_name == sorted(states_name), "Sort error"

                chrome_driver.back()

    def test_sorting_geo_zones(self, chrome_driver, admin_login):

        chrome_driver.get(GEO_ZONES_PAGE)

        # Проверяем сортировку данных в таблицах гео зон
        geo_zone_table = Table(chrome_driver)
        for i in range(len(geo_zone_table.table_rows)):
            row = geo_zone_table.table_rows[i]
            data_row = geo_zone_table.get_row_data(row)
            if int(data_row["Zones"][0]):
                geo_zone_table.edit_row(row)
                states_table = Table(chrome_driver)
                states = states_table.get_table_data()
                states_name = [state["Zone"] for state in states]
                assert states_name == sorted(states_name), "Sort error"

                chrome_driver.back()

    @pytest.mark.parametrize(
        'driver', ['chrome_driver', 'firefox_driver', 'safari_driver'],
        ids=['driver_chrome', 'driver_firefox', 'safari_driver']
    )
    def test_product_card(self, request, driver):
        driver = request.getfixturevalue(driver)
        driver.get(URL_SHOP)

        box = driver.find_element(*BOX_CAMPAIGNS)
        product = box.find_elements(*ITEM_PRODUCT)[0]
        name = product.find_element(*ITEM_NAME)
        price = product.find_element(*ITEM_PRICE)
        camp_price = product.find_element(*ITEM_CAMPAIGN_PRICE)

        # Параметры товара на главной странице
        text_name_main = name.text
        text_price_main = price.text
        text_camp_price_main = camp_price.text
        text_main = (text_name_main, text_price_main, text_camp_price_main)
        color_price_main = price.value_of_css_property("color").strip('rgba()').replace(' ', '').split(',')
        decoration_price_main = price.value_of_css_property("text-decoration").split()[0]
        color_camp_price_main = camp_price.value_of_css_property("color").strip('rgba()').replace(' ', '').split(',')

        assert color_price_main[0] == color_price_main[1] == color_price_main[2], "Wrong price color"
        assert decoration_price_main == 'line-through', "The price is not decorated"
        assert color_camp_price_main[1] == '0' and color_camp_price_main[2] == '0', "Wrong campaign price color"

        product.click()
        sleep(1) # Без этого костыля NoSuchFrameException на Safari, явные и не явные ожидания не дают результата
        card = driver.find_element(*CARD)
        name = card.find_element(*CARD_NAME)
        price = card.find_element(*ITEM_PRICE)
        camp_price = card.find_element(*ITEM_CAMPAIGN_PRICE)

        # Параметры товара в карточке товара
        text_name_card = name.text
        text_price_card = price.text
        text_camp_price_card = camp_price.text
        text_card = (text_name_card, text_price_card, text_camp_price_card)
        color_price_card = price.value_of_css_property("color").strip('rgba()').replace(' ', '').split(',')
        decoration_price_card = price.value_of_css_property("text-decoration").split()[0]
        color_camp_price_card = camp_price.value_of_css_property("color").strip('rgba()').replace(' ', '').split(',')

        assert color_price_card[0] == color_price_card[1] == color_price_card[2], "Wrong price color"
        assert decoration_price_card == 'line-through', "The price is not decorated"
        assert color_camp_price_card[1] == '0' and color_camp_price_card[2] == '0', "Wrong campaign price color"

        assert text_main == text_card, "Text data does not match"
