from selenium.webdriver.common.by import By

USER_NAME_SELECTOR = (By.XPATH, '//input[@name="username"]')
USER_PASSWORD_SELECTOR = (By.XPATH, '//input[@name="password"]')
CONFIRM_BUTTON_SELECTOR = (By.XPATH, '//button[@name="login"]')

URL = "http://localhost/litecart/admin/"
USER_NAME = "admin" # Нужно указать имя пользователя
USER_PASSWORD = "admin" # Нужно указать пароль пользователя


def test_user_login_chrome(driver_chrome):
    driver_chrome.get(URL)
    driver_chrome.find_element(*USER_NAME_SELECTOR).send_keys(USER_NAME)
    driver_chrome.find_element(*USER_PASSWORD_SELECTOR).send_keys(USER_PASSWORD)
    driver_chrome.find_element(*CONFIRM_BUTTON_SELECTOR).click()

def test_user_login_firefox(driver_firefox):
    driver_firefox.get(URL)
    driver_firefox.find_element(*USER_NAME_SELECTOR).send_keys(USER_NAME)
    driver_firefox.find_element(*USER_PASSWORD_SELECTOR).send_keys(USER_PASSWORD)
    driver_firefox.find_element(*CONFIRM_BUTTON_SELECTOR).click()

def test_user_login_safari(driver_safari):
    driver_safari.get(URL)
    driver_safari.find_element(*USER_NAME_SELECTOR).send_keys(USER_NAME)
    driver_safari.find_element(*USER_PASSWORD_SELECTOR).send_keys(USER_PASSWORD)
    driver_safari.find_element(*CONFIRM_BUTTON_SELECTOR).click()