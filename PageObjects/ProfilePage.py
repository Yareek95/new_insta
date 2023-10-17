from selenium import webdriver
from selenium.webdriver.common.by import By


class ProfilePage:
    num_followers_xpath = "//a[contains(text(), ' followers')]/span"
    num_following_xpath = "//a[contains(text(), ' following')]/span"
    link_post_xpath = "//article[@class='x1iyjqo2']/div/div/div[1]/div[1]/a"
    btn_like_xpath = "//span[@class='_aamw']//div[@role='button']"
    btn_next_xpath = "//div[@class=' _aaqg _aaqh']//button[@type='button']"
    btn_follow_xpath = "//div[contains(text(), 'Follow')]/ancestor::button"
    txt_tryAgainLater_xpath = "//span[contains(text(), 'Try Again Later')]"
    btn_tryAgainLater_xpath = "//button[normalize-space()='OK']"
    btn_closePost_xpath = "//div[@class='x160vmok x10l6tqk x1eu8d0j x1vjfegm']/div[@role='button']"

    def __init__(self, driver):
        self.driver = driver

    def num_of_followers(self):
        return self.driver.find_element(By.XPATH, self.num_followers_xpath).text

    def num_of_following(self):
        return self.driver.find_element(By.XPATH, self.num_following_xpath).text

    def click_follow(self):
        self.driver.find_element(By.XPATH, self.btn_follow_xpath).click()

    def open_post(self):
        self.driver.find_element(By.XPATH, self.link_post_xpath).click()

    def put_like(self):
        self.driver.find_element(By.XPATH, self.btn_like_xpath).click()

    def tryAgainLater_txt(self):
        tal_txt = self.driver.find_element(By.XPATH, self.txt_tryAgainLater_xpath).text
        return tal_txt == "Try Again Later"
    def ok_tryAgainLater(self):
        self.driver.find_element(By.XPATH, self.btn_tryAgainLater_xpath).click()

    def click_next(self):
        self.driver.find_element(By.XPATH, self.btn_next_xpath).click()

    def close_post(self):
        self.driver.find_element(By.XPATH, self.btn_closePost_xpath).click()

