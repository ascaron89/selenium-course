from selenium.webdriver.common.by import By

# BOX
BOX_CAMPAIGNS = (By.XPATH, '//div[@id="box-campaigns"]')

# ITEM
ITEM_PRODUCT = (By.XPATH, './/li[contains(@class, "product")]')
ITEM_STICKER = (By.XPATH, './/div[contains(@class, "sticker")]')
ITEM_NAME = (By.XPATH, './/*[@class="name"]')
ITEM_PRICE = (By.XPATH, './/*[@class="regular-price"]')
ITEM_CAMPAIGN_PRICE = (By.XPATH, './/*[@class="campaign-price"]')

# ITEM CARD
CARD = (By.XPATH, '//div[@id="box-product"]')
CARD_NAME = (By.XPATH, './/h1')