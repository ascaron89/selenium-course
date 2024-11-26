from selenium.webdriver.common.by import By


# Страница Catalog
BUTTON_ADD_NEW_PRODUCT = (By.XPATH, '//a[contains(text(), "Add New Product")]')
BUTTON_SAVE_PRODUCT = (By.XPATH, '//button[@name="save"]')
BUTTON_CANSEL_PRODUCT = (By.XPATH, '//button[@name="cancel"]')
BUTTON_DELETE_PRODUCT = (By.XPATH, '//button[@name="delete"]')


# Вкладки параметров продукта
TAB_GENERAL = (By.XPATH, '//a[contains(text(), "General")]')
TAB_INFORMATION = (By.XPATH, '//a[contains(text(), "Information")]')
TAB_PRICE = (By.XPATH, '//a[contains(text(), "Prices")]')


# Tab general
RADIO_PRODUCT_STATUS_ENABLE = (By.XPATH, '//input[@name="status"][@value="1"]')
RADIO_PRODUCT_STATUS_DISABLE = (By.XPATH, '//input[@name="status"][@value="0"]')
INPUT_PRODUCT_NAME = (By.XPATH, '//input[@name="name[en]"]')
INPUT_PRODUCT_CODE = (By.XPATH, '//input[@name="code"]')
CHECKBOX_PRODUCT_CATEGORIES_ROOT = (By.XPATH, '//input[@name="categories[]"][@data-name="Root"]')
CHECKBOX_PRODUCT_CATEGORIES_RUBBER_DUCKS = (By.XPATH, '//input[@name="categories[]"][@data-name="Rubber Ducks"]')
SELECT_PRODUCT_DEFAULT_CATEGORY = (By.XPATH, '//select[@name="default_category_id"]')
CHECKBOX_PRODUCT_GENDER_FEMALE = (By.XPATH, '//td[contains(text(), "Female")]/preceding-sibling::td')
CHECKBOX_PRODUCT_GENDER_MALE = (By.XPATH, '//td[contains(text(), "Male")]/preceding-sibling::td')
CHECKBOX_PRODUCT_GENDER_UNISEX = (By.XPATH, '//td[contains(text(), "Unisex")]/preceding-sibling::td')
INPUT_PRODUCT_QUANTITY = (By.XPATH, '//input[@name="quantity"]')
FILE_PRODUCT_UPLOAD_IMAGES = (By.XPATH, '//input[@name="new_images[]"]')
CALENDAR_PRODUCT_DATE_VALID_FROM = (By.XPATH, '//input[@name="date_valid_from"]')
CALENDAR_PRODUCT_DATE_VALID_TO = (By.XPATH, '//input[@name="date_valid_to"]')

# Tab information
SELECT_PRODUCT_MANUFACTURE = (By.XPATH, '//select[@name="manufacturer_id"]')
SELECT_PRODUCT_SUPPLIER = (By.XPATH, '//select[@name="supplier_id"]')
INPUT_PRODUCT_KEYWORDS = (By.XPATH, '//input[@name="keywords"]')
INPUT_PRODUCT_SHORT_DESCRIPTION = (By.XPATH, '//input[@name="short_description[en]"]')
TEXTAREA_PRODUCT_DESCRIPTION = (By.XPATH, '//div[@class="trumbowyg-editor"]')
INPUT_PRODUCT_HEAD_TITLE = (By.XPATH, '//input[@name="head_title[en]"]')
INPUT_PRODUCT_META_DESCRIPTION = (By.XPATH, '//input[@name="meta_description[en]"]')

# Tab prices
INPUT_PRODUCT_PURCHASE_PRICE = (By.XPATH, '//input[@name="purchase_price"]')
SELECT_PRODUCT_PURCHASE_CURRENCY = (By.XPATH, '//select[@name="purchase_price_currency_code"]')
INPUT_PRODUCT_PRICE_USD = (By.XPATH, '//input[@name="prices[USD]"]')
INPUT_PRODUCT_PRICE_EUR = (By.XPATH, '//input[@name="prices[EUR]"]')
