import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig

@pytest.mark.test
class Test_cmd:
    usernames = [2, 1, 3, 4]
    baseURL = "https://demo.nopcommerce.com/"

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        for username_number in self.usernames:
            name = ReadConfig.getUserName(username_number)
            self.driver.find_element(By.XPATH, "//input[@id='small-searchterms']").clear()
            self.driver.find_element(By.XPATH, "//input[@id='small-searchterms']").send_keys(name)
            time.sleep(3)
            print(self.driver.title + f"***===>>> {name}")
