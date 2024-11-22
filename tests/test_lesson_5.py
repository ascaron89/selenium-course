from time import sleep

import pytest

from elements.table import Table
from tests.conftest import driver_chrome, driver_firefox, driver_safari
from tests.data.settings import COUNTRIES_PAGE, GEO_ZONES_PAGE, URL_SHOP


def test_sorting_countries_zones(driver_chrome, admin_login):

    driver_chrome.get(COUNTRIES_PAGE)

    # Проверяем сортировку данных в таблице стран
    country_table = Table(driver_chrome)
    countries = country_table.get_table_data()
    countries_name = [country["Name"] for country in countries]
    assert countries_name == sorted(countries_name), "Sort error"

    # Проверяем сортировку данных в таблицах стран
    for i in range(len(country_table.table_rows)):
        row = country_table.table_rows[i]
        data_row = country_table.get_row_data(row)
        if int(data_row["Zones"][0]):
            country_table.edit_row(row)
            states_table = Table(driver_chrome)
            states = states_table.get_table_data()
            states_name = [state["Name"] for state in states]
            assert states_name == sorted(states_name), "Sort error"

            driver_chrome.back()

def test_sorting_geo_zones(driver_chrome, admin_login):

    driver_chrome.get(GEO_ZONES_PAGE)

    # Проверяем сортировку данных в таблицах гео зон
    geo_zone_table = Table(driver_chrome)
    for i in range(len(geo_zone_table.table_rows)):
        row = geo_zone_table.table_rows[i]
        data_row = geo_zone_table.get_row_data(row)
        if int(data_row["Zones"][0]):
            geo_zone_table.edit_row(row)
            states_table = Table(driver_chrome)
            states = states_table.get_table_data()
            states_name = [state["Zone"] for state in states]
            assert states_name == sorted(states_name), "Sort error"

            driver_chrome.back()

# @pytest.mark.parametrize(
#     'driver', [driver_firefox, driver_chrome, driver_safari],
#     ids=['driver_chrome', 'driver_firefox', 'driver_firefox']
# )
def test_product_card(driver_firefox, admin_login):
    driver_firefox.get(URL_SHOP)
    print(type(driver_firefox))
    sleep(2)