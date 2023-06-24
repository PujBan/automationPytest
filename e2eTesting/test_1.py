from telnetlib import EC

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    baseURL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h5[normalize-space()='Login']"))
        )
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('Admin')
        self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        # Verify title
        matchheading = self.driver.title
        print(matchheading)
        if matchheading == "Dashboard":
            assert True
        else:
            assert False

