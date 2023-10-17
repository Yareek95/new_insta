import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.MainPage import MainPage
from PageObjects.ProfilePage import ProfilePage
from PageObjects.SomePage import SomePage
from PageObjects.MessagePage import MessagePage

from utilities.readProperties import ReadConfig


@pytest.mark.message
class TestMessage:
    baseURL = ReadConfig.getApplicationURL()
    usernames = [1, 2, 3]
    # username = ReadConfig.getUserName1()
    password = ReadConfig.getPassword()

    def test_msg_1(self, setup, name):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.mp = MainPage(self.driver)
        self.sp = SomePage(self.driver)
        self.msg = MessagePage(self.driver)
        self.pp = ProfilePage(self.driver)

        for username_number in self.usernames:
            self.username = ReadConfig.getUserName(username_number)
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
            messages = ["Good night", "Sweet Dreams"]
            for repeat in range(3):
                for message in messages:
                    self.sp.write_and_send_msg(message)
                    time.sleep(2)
            self.mp.click_settings()
            self.mp.click_logOut()
            print(self.driver.title)
            assert True
"""
pytest -n auto -m like TestCases --browser chrome --name jerry.k_o

cd C:\MyGitHubDesktop\new_insta
pytest -n auto -m %action% --browser %browser% --name %username% --alluredir=Reports
allure serve Reports

"""