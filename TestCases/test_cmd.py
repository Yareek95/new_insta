import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_cmd:
    baseURL = "https://demo.nopcommerce.com/"

    def test_login(self, setup, name):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys(name)
        time.sleep(5)
        print(self.driver.title)
