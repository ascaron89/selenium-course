import pytest
from selenium import webdriver

@pytest.fixture
def driver_chrome(request):
    driver = webdriver.Chrome()
    request.addfinalizer(driver.quit)

    return driver

@pytest.fixture
def driver_firefox(request):
    driver = webdriver.Firefox()
    request.addfinalizer(driver.quit)

    return driver

@pytest.fixture
def driver_safari(request):
    driver_safari = webdriver.Safari()
    request.addfinalizer(driver_safari.quit)

    return driver_safari