from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.data.admin_selectors import INPUT_USER_NAME, INPUT_USER_PASSWORD, BUTTON_CONFIRM
from tests.data.settings import URL_ADMIN, ADMIN_NAME, ADMIN_PASSWORD

class TestLesson2:
    def test_user_login_chrome(self, chrome_driver):
        chrome_driver.get(URL_ADMIN)
        chrome_driver.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
        chrome_driver.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
        chrome_driver.find_element(*BUTTON_CONFIRM).click()

    def test_user_login_firefox(self, firefox_driver):
        firefox_driver.get(URL_ADMIN)
        firefox_driver.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
        firefox_driver.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
        firefox_driver.find_element(*BUTTON_CONFIRM).click()

    def test_user_login_safari(self, safari_driver):
        safari_driver.get(URL_ADMIN)
        safari_driver.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
        safari_driver.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
        safari_driver.find_element(*BUTTON_CONFIRM).click()
    def test_open_chrome(self, chrome_driver):
        chrome_driver.get("https://www.google.com")
        WebDriverWait(chrome_driver, 10).until(EC.title_is("Google"))