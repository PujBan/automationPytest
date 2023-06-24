import time

import pytest
from selenium.webdriver.chrome.options import Options

from pageObjects.loginPo import LoginPage
from utilities.BaseClass import BaseClass
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


#@pytest.mark.usefixtures("setup")
class TestLogin(BaseClass):
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen.loggen()

    def test_login(self):
        self.logger.info("*************************** test_login ********************************")
        self.logger.info("*************************** Verify login test ********************************")
        # call fixture which has login instruction
        time.sleep(5000)
