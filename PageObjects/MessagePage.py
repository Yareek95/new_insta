import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class MessagePage:
    btn_sendmsg_xpath = "//div[contains(text(),'Send message')]"
    txtbox_search_xpath = "//input[@placeholder='Search...']"
    #search_result_xpath = "//span[contains(text(),'vlad___kramar')]"
    btn_chat_xpath = "//div[contains(text(),'Chat')]"


    def __init__(self, driver):
        self.driver = driver

    def click_send_msg(self):
        self.driver.find_element(By.XPATH, self.btn_sendmsg_xpath).click()

    def search_and_click(self, name):
        self.driver.find_element(By.XPATH, self.txtbox_search_xpath).send_keys(name)
        time.sleep(1)
        self.driver.find_element(By.XPATH, f"//div[@role='dialog']//span[contains(text(),'{name}')]").click()
        #//div[@role='dialog']//span[contains(text(),'jerry.k_o')]
        #//span[contains(text(),'{name}')]

    def click_chat(self):
        self.driver.find_element(By.XPATH, self.btn_chat_xpath).click()