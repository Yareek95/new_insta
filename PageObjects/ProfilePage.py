from selenium import webdriver
from selenium.webdriver.common.by import By


class ProfilePage:
    num_followers_xpath = "//a[contains(text(), ' followers')]/span"
    num_following_xpath = "//a[contains(text(), ' following')]/span"
    link_post_xpath = "//article[@class='x1iyjqo2']/div/div/div[1]/div[1]/a"
    btn_like_xpath = "//span[@class='_aamw']//div[@role='button']"
    btn_next_xpath = "//div[contains(@class,'_aaqg _aaqh')]//button[contains(@type,'button')]"
    def __init__(self, driver):
        self.driver = driver

    def num_of_followers(self):
        return self.driver.find_element(By.XPATH, self.num_followers_xpath).text

    def num_of_following(self):
        return self.driver.find_element(By.XPATH, self.num_following_xpath).text

    def open_post(self):
        self.driver.find_element(By.XPATH, self.link_post_xpath).click()

    def put_like(self):
        self.driver.find_element(By.XPATH, self.btn_like_xpath).click()

    def click_next(self):
        self.driver.find_element(By.XPATH, self.btn_next_xpath).click()

