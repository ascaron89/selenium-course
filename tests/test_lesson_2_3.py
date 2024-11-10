from tests.data.admin_selectors import INPUT_USER_NAME, INPUT_USER_PASSWORD, BUTTON_CONFIRM
from tests.data.settings import URL_ADMIN, ADMIN_NAME, ADMIN_PASSWORD

def test_user_login_chrome(driver_chrome):
    driver_chrome.get(URL_ADMIN)
    driver_chrome.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
    driver_chrome.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
    driver_chrome.find_element(*BUTTON_CONFIRM).click()

def test_user_login_firefox(driver_firefox):
    driver_firefox.get(URL_ADMIN)
    driver_firefox.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
    driver_firefox.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
    driver_firefox.find_element(*BUTTON_CONFIRM).click()

def test_user_login_safari(driver_safari):
    driver_safari.get(URL_ADMIN)
    driver_safari.find_element(*INPUT_USER_NAME).send_keys(ADMIN_NAME)
    driver_safari.find_element(*INPUT_USER_PASSWORD).send_keys(ADMIN_PASSWORD)
    driver_safari.find_element(*BUTTON_CONFIRM).click()