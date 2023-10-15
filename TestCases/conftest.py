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

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--name")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture
def name(request):
    return request.config.getoption("--name")
