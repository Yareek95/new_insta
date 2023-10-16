import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.MainPage import MainPage
from PageObjects.SomePage import SomePage
from PageObjects.MessagePage import MessagePage

from utilities.readProperties import ReadConfig


class TestMessage:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName4()
    password = ReadConfig.getPassword()

    def test_msg_3(self, setup, name):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.mp = MainPage(self.driver)
        self.sp = SomePage(self.driver)
        self.msg = MessagePage(self.driver)

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
        self.mp.click_msg()
        time.sleep(1)
        self.msg.click_send_msg()
        time.sleep(1)
        self.msg.search_and_click(name)
        self.msg.click_chat()
        time.sleep(1)
        messages = ["Have a good day", "Stay Safe"]
        for repeat in range(3):
            for message in messages:
                self.sp.write_and_send_msg(message)
                time.sleep(2)
