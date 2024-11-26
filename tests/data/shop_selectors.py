from selenium.webdriver.common.by import By

# USER
INPUT_USER_EMAIL = (By.XPATH, '//input[@name="email"]')
INPUT_USER_PASS = (By.XPATH, '//input[@name="password"]')
BUTTON_USER_LOGIN = (By.XPATH, '//button[@name="login"]')
LINK_USER_CREATE = (By.XPATH, '//a[contains(text(), "New customers")]')
LINK_USER_LOGOUT = (By.XPATH, '//a[contains(text(), "Logout")]')
INPUT_CREATE_FIRST_NAME = (By.XPATH, '//input[@name="firstname"]')
INPUT_CREATE_LAST_NAME = (By.XPATH, '//input[@name="lastname"]')
INPUT_CREATE_ADDRESS_1 = (By.XPATH, '//input[@name="address1"]')
INPUT_CREATE_POST_CODE = (By.XPATH, '//input[@name="postcode"]')
INPUT_CREATE_CITY = (By.XPATH, '//input[@name="city"]')
INPUT_CREATE_EMAIL = (By.XPATH, '//input[@name="email"]')
INPUT_CREATE_PHONE = (By.XPATH, '//input[@name="phone"]')
INPUT_CREATE_PASSWORD = (By.XPATH, '//input[@name="password"]')
INPUT_CREATE_CONFIRM_PASSWORD = (By.XPATH, '//input[@name="confirmed_password"]')
SELECT_CREATE_COUNTRY = (By.XPATH, '//select[@name="country_code"]')
SELECT_CREATE_STATE = (By.XPATH, '//select[@name="zone_code"]')
BUTTON_CREATE_ACCOUNT = (By.XPATH, '//button[@name="create_account"]')


# BOX
BOX_CAMPAIGNS = (By.XPATH, '//div[@id="box-campaigns"]')

# ITEM
ITEM_PRODUCT = (By.XPATH, './/li[contains(@class, "product")]')
ITEM_STICKER = (By.XPATH, './/div[contains(@class, "sticker")]')
ITEM_NAME = (By.XPATH, './/*[@class="name"]')
ITEM_PRICE = (By.XPATH, './/*[@class="regular-price"]')
ITEM_CAMPAIGN_PRICE = (By.XPATH, './/*[@class="campaign-price"]')

# ITEM CARD
ITEM_CARD = (By.XPATH, '//div[@id="box-product"]')
ITEM_CARD_NAME = (By.XPATH, './/h1')
BUTTON_ADD_TO_CART = (By.XPATH, '//button[@name="add_cart_product"]')
SELECT_CARD_SIZE = (By.XPATH, '//select[@name="options[Size]"]')

# CART
ITEM_QUANTITY_CART = (By.XPATH, '//span[@class="quantity"]')
BUTTON_REMOVE_PRODUCT_FROM_CART = (By.XPATH, '//button[@name="remove_cart_item"]')

