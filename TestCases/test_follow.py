import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage




class Test_login:
    baseURL = "https://demo.nopcommerce.com/"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        time.sleep(5)

        print(self.driver.title)
