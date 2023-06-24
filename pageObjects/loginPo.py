import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class LoginPage:

    textbox_username_xpath = "//input[@placeholder='Email']"
    textbox_password_xpath = "//input[@placeholder='Password']"
    button_login_xpath = "(//div[@class='ui fluid large blue submit button'])[1]"
    user_display_xpath = "//div[@class='ui fluid large blue submit button']"


    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)

    def submit(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        # explicit wait
        w = WebDriverWait(self.driver, 20)
        w.until(expected_conditions.presence_of_element_located((By.XPATH, self.user_display_xpath)))













