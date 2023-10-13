from selenium import webdriver
from selenium.webdriver.common.by import By


class ProfilePage:
    num_followers_xpath = "//a[contains(text(), ' followers')]/span"
    num_following_xpath = "//a[contains(text(), ' following')]/span"

    def __init__(self, driver):
        self.driver = driver

    def num_of_followers(self):
        return self.driver.find_element(By.XPATH, self.num_followers_xpath).text

    def num_of_following(self):
        return self.driver.find_element(By.XPATH, self.num_following_xpath).text
