import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser.............")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser.............")
    else:
        driver = webdriver.Ie()
    return driver


def pytest_addoption(parser):       #This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       #This will return the Browser value to setup method
    return request.config.getoption("--browser")