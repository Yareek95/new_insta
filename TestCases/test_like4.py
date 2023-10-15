import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.MainPage import MainPage
from PageObjects.SomePage import SomePage
from PageObjects.MessagePage import MessagePage
from PageObjects.ProfilePage import ProfilePage

from utilities.readProperties import ReadConfig


class TestMessage:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName4()
    password = ReadConfig.getPassword()

    def test_like4(self, setup, name):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.mp = MainPage(self.driver)
        self.sp = SomePage(self.driver)
        self.msg = MessagePage(self.driver)
        self.pp = ProfilePage(self.driver)

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
        self.mp.click_search()
        self.mp.search_and_click(name)
        self.pp.open_post()
        times = 0
        while times < 5:
            self.pp.put_like()
            self.pp.click_next()
            times += 1
