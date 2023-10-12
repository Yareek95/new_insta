import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

from utilities.readProperties import ReadConfig



class Test_login:
    baseURL = "https://demo.nopcommerce.com/"
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        print(self.driver.title)
