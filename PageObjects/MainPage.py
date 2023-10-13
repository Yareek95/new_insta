from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPage:
    link_profile_xpath = "//div[@class='x1n2onr6']//a"
    link_search_xpath = "//div[@class='x1iyjqo2 xh8yej3']/div[2]//a"
    input_search_xpath = "//div[@class='x78zum5 xdt5ytf x5yr21d']//input"
    search_result_xpath = "//span[contains(text(), 'vlad___kramar')]"

    def __init__(self, driver):
        self.driver = driver

    def click_profile(self):
        self.driver.find_element(By.XPATH, self.link_profile_xpath).click()

    def click_search(self):
        self.driver.find_element(By.XPATH, self.link_search_xpath).click()

    #Search:
    def search_and_click(self, input_search):
        self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(input_search)
        self.driver.find_element(By.XPATH, f"//a[@href='/{input_search}/']//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xxbr6pl xbbxn1n xwib8y2 x1y1aw1k x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']").click()

