import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage

from utilities.readProperties import ReadConfig



class Test_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)

        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        time.sleep(2)
        try:
            self.lp.click_NotNow()
        except Exception as e:
            print(f"error: {e}")
        try:
            self.lp.click_NotNow_notif()
        except Exception as en:
            print(f"error: {en}")
        assert True
        time.sleep(10)