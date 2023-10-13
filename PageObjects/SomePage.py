from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class SomePage:
    btn_message_xpath = "//div[contains(text(), 'Message')]"
    txt_field_xpath = "//div[@aria-label='Message']"
    def __init__(self, driver):
        self.driver = driver

    def click_message(self):
        self.driver.find_element(By.XPATH, self.btn_message_xpath).click()

    def write_message(self, my_message):
        self.driver.find_element(By.XPATH, self.txt_field_xpath).send_keys(my_message)
        self.driver.find_element(By.XPATH, self.txt_field_xpath).send_keys(Keys.ENTER)



