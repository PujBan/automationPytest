import time

import pytest
from selenium import webdriver
from pageObjects.loginPo import LoginPage


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome",
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "IE":
        driver = webdriver.Edge()

    driver.get("https://ui.cogmento.com/")
    driver.maximize_window()
    lp = LoginPage(driver)
    # enter username
    lp.setUserName("bansari.pujara@simformsolutions.com")
    # enter password
    lp.setPassword("Bansari@2206")
    # CLick on login button
    lp.submit()
    time.sleep(10)
    # when yield is used reutun statment is not worked
    # That's why below request instance is used
    # Below defined driver is sent to class object in test files
    # cls.driver = class driver - use this add request ad setup method argument
    request.cls.driver = driver
    yield
    driver.close()
