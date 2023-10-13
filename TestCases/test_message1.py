import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.MainPage import MainPage
from PageObjects.SomePage import SomePage

from utilities.readProperties import ReadConfig



class TestMessage:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName1()
    password = ReadConfig.getPassword()
    search_name = ReadConfig.getSearchName()


    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.mp = MainPage(self.driver)
        self.sp = SomePage(self.driver)


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
        time.sleep(1)
        self.mp.search_and_click(self.search_name)
        self.sp.click_message()
        messages = ["Have a good day", "Лох", "Good Morning", "Говно", "Safe Travel", "Додик"]
        for repeat in range(10):
            for message in messages:
                self.sp.write_message(message)