from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_open_chrome(driver_chrome):
    driver_chrome.get("https://www.google.com")
    WebDriverWait(driver_chrome, 10).until(EC.title_is("Google"))