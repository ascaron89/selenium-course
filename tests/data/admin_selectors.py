from selenium.webdriver.common.by import By

# Форма авторизации
INPUT_USER_NAME = (By.XPATH, '//input[@name="username"]')
INPUT_USER_PASSWORD = (By.XPATH, '//input[@name="password"]')
BUTTON_CONFIRM = (By.XPATH, '//button[@name="login"]')

# Боковая панель
ICON_LOGOUT = (By.XPATH, '//a[@title="Logout"]')
ITEM_MENU = (By.XPATH, '//ul[@id="box-apps-menu"]/li')
ITEM_UNDER_MENU = (By.XPATH, '//ul[@class="docs"]/li')

# Общие элементы Страницы
ELEMENT_TITLE_H1 = (By.XPATH, '//*[@id="content"]//h1')