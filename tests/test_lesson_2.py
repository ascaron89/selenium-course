import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)

    return driver


def test_open_chrome(driver):
    driver.get("http://www.google.com/")
    WebDriverWait(driver, 10).until(EC.title_is("Google"))