from selenium.webdriver.common.by import By

USER_NAME_SELECTOR = (By.XPATH, '//input[@autocomplete="username"]')
USER_PASSWORD_SELECTOR = (By.XPATH, '//input[@autocomplete="current-password"]')
CONFIRM_BUTTON_SELECTOR = (By.XPATH, '//input[@id="loginbtn"]')

URL = "https://software-testing.ru/lms/login"
USER_NAME = "test_name" # Нужно указать имя пользователя
USER_PASSWORD = "test_password" # Нужно указать пароль пользователя


def test_user_login(driver):
    driver.get(URL)
    driver.find_element(*USER_NAME_SELECTOR).send_keys(USER_NAME)
    driver.find_element(*USER_PASSWORD_SELECTOR).send_keys(USER_PASSWORD)
    driver.find_element(*CONFIRM_BUTTON_SELECTOR).click()

