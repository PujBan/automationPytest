import time
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.VerifyEvent import VerifyEvent


class CalanderPage:

    home = (By.XPATH, "//i[@class='home icon']")
    calander = (By.XPATH, "//a[@href='/calendar']")
    create = (By.XPATH, "//button[normalize-space()='Create']")
    save = (By.XPATH, "//button[normalize-space()='Save']")
    cancel = (By.XPATH,"//button[normalize-space()='Cancel']")
    title = (By.XPATH, "//*[contains(@name, 'title')]")
    category = (By.XPATH, "//*[contains(@name, 'category')]")
    category_list = (By.XPATH, "//div[@class='visible menu transition']//span")
    description = (By.XPATH, "//*[contains(@name, 'description')]")
    location = (By.XPATH, "//*[contains(@name, 'location')]")
    reminder_time = (By.XPATH, "//*[contains(@name, 'reminder_minutes')]")
    identifier= (By.XPATH,"//*[contains(@name, 'identifier')]")


    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def menu(self):
        home = self.driver.find_element(*CalanderPage.home)
        # object of ActionChains
        a = ActionChains(self.driver)
        # Hover over element
        a.move_to_element(home)
        # open calander page
        time.sleep(5)
        self.driver.find_element(*CalanderPage.calander).click()
        time.sleep(5)

    def createbutton(self):
        self.driver.find_element(*CalanderPage.create).click()
        time.sleep(5)
        # verify title
        header = self.driver.find_element(By.XPATH, "//span[@class='selectable ']")
        assert header.text == "Create new Event", "Add event page not loaded"

    def savedisable(self):

        # verify save button is disabled or not
        if self.driver.find_element(*CalanderPage.save).is_enabled():
            print('Button Enabled')
            self.driver.save_screenshot(".\\screenShots\\" + "savebuttonenable.png")
        else:
            print('Button disbled')
            self.driver.save_screenshot(".\\screenShots\\" + "savebuttondisable.png")

    def event_title(self,title):
        # Enter title
        self.driver.find_element(*CalanderPage.title).send_keys(title)

    def category_selection(self):
        # Enter category
        self.driver.find_element(*CalanderPage.category).click()

    def cate_list_123(self):
        #Category list
        return self.driver.find_elements(*CalanderPage.category_list)

    def text_description(self,desc):
        self.driver.find_element(*CalanderPage.description).send_keys(desc)

    def text_location(self, loc):
        self.driver.find_element(*CalanderPage.location).send_keys(loc)

    def text_reminder_time(self, rt):
        self.driver.find_element(*CalanderPage.reminder_time).send_keys(rt)

    def text_identifier(self, idtf):
        self.driver.find_element(*CalanderPage.identifier).send_keys(idtf)

    def click_save(self):
        self.driver.find_element(*CalanderPage.save).click()
        time.sleep(10)










