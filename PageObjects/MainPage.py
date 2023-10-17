from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:
    link_profile_xpath = "//div[@class='x1n2onr6']//a"
    btn_search_xpath = "//div[@class='x1iyjqo2 xh8yej3']/div[2]//a"
    btn_messages_xpath = "//div[@class='x1iyjqo2 xh8yej3']/div[5]//a"
    btn_settings_xpath = "//div[@class='xl5mz7h xhuyl8g']/span//a"
    btn_logOut_xpath = "//div[@role='button'][.//span[contains(text(), 'Log out')]]"
    input_search_xpath = "//div[@class='x78zum5 xdt5ytf x5yr21d']//input"


    #search_result_xpath = "//a//div/span[contains(text(), 'vlad___kramar')]"

    def __init__(self, driver):
        self.driver = driver

    def click_profile(self):
        self.driver.find_element(By.XPATH, self.link_profile_xpath).click()

    def click_search(self):
        self.driver.find_element(By.XPATH, self.btn_search_xpath).click()

    #Search:
    def search_and_click(self, input_search):
        self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(input_search)
        self.driver.find_element(By.XPATH, f"//div/span[contains(text(), '{input_search}')]").click()

    def click_msg(self):
        self.driver.find_element(By.XPATH, self.btn_messages_xpath).click()

    def click_settings(self):
        self.driver.find_element(By.XPATH, self.btn_settings_xpath).click()

    def click_logOut(self):
        self.driver.find_element(By.XPATH, self.btn_logOut_xpath).click()
