import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from tests.data.admin_selectors import ELEMENT_FORM_POST, LINK_ON_NEW_PAGE
from tests.data.country_selectors import BUTTON_ADD_NEW_COUNTRY
from tests.data.settings import COUNTRIES_PAGE


class TestLesson8:
    @pytest.mark.parametrize(
        'driver', ['chrome_driver', 'firefox_driver', 'safari_driver'],
        ids=['driver_chrome', 'driver_firefox', 'safari_driver']
    )
    def test_open_new_windows(self,request, driver, custom_admin_login):

        driver = request.getfixturevalue(driver)
        custom_admin_login(driver)
        driver.get(COUNTRIES_PAGE)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.visibility_of_element_located(BUTTON_ADD_NEW_COUNTRY)).click()
        total_link = len(driver.find_element(*ELEMENT_FORM_POST).find_elements(*LINK_ON_NEW_PAGE))
        current_handle = driver.current_window_handle
        for i in range(total_link):
            current_handles = driver.window_handles
            links = driver.find_element(*ELEMENT_FORM_POST).find_elements(*LINK_ON_NEW_PAGE)
            links[i].click()
            wait.until(EC.new_window_is_opened(current_handles))
            new_handle = next(filter(lambda x: x != current_handle, driver.window_handles))
            driver.switch_to.window(new_handle)
            driver.close()
            driver.switch_to.window(current_handle)