from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    txt_userName_xpath = "//input[@name='username']"
    txt_password_xpath = "//input[@name='password']"
    btn_login_xpath = "//button[@type='submit']"
    btn_NotNow_xpath = "//div[@role='button' and contains(text(), 'Not Now')]"
    btn_NotNowNotif_xpath = "//button[contains(text(), 'Not Now')]"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.txt_userName_xpath).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.XPATH, self.txt_password_xpath).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_NotNow(self):
        self.driver.find_element(By.XPATH, self.btn_NotNow_xpath).click()

    def click_NotNow_notif(self):
        self.driver.find_element(By.XPATH, self.btn_NotNowNotif_xpath).click()