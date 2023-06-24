import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.VerifyEvent import VerifyEvent
from pageObjects.calanderPo import CalanderPage
from utilities.BaseClass import BaseClass
from testData.calanderPageData import calanderPageData


class TestCalander(BaseClass):

    def test_opencalanderpage(self):
        # first do Login actitvity from baseclsaa
        # POM class object created
        cp = CalanderPage(self.driver)
        # Hover over menu and open calander page
        cp.menu()

    def test_opencreateevent(self):
        # Login not required again, will continue this test cases in same session
        # POM class object created
        cp = CalanderPage(self.driver)
        # Hover over menu and open calendar page
        cp.menu()
        # click on create event button
        cp.createbutton()
        # verify save button
        cp.savedisable()

    def test_createnewevent(self, getData):
        # Login not required again, will continue this test cases in same session
        # POM class object created
        cp = CalanderPage(self.driver)
        # Enter event title
        cp.event_title(getData["title"])
        # Click on category drop down
        cp.category_selection()
        # Store category list and use in tests
        categories = cp.cate_list_123()
        for category1 in categories:
            if category1.text == getData["category"]:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(category1))
                category1.click()
                break
        # Enter Description
        cp.text_description(getData["description"])
        # Enter Location
        cp.text_location(getData["location"])
        # Enter reminder_time
        cp.text_reminder_time(getData["reminder_time"])
        # Enter identifier
        cp.text_identifier(getData["identifier"])
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
        # click on save button
        cp.click_save()
        ve = VerifyEvent(self.driver)
        title1 = ve.getEventTitle()
        assert title1.text == getData["title"], "Title not matched"

    def test_addNote(self):

        # add note on created event
        ve = VerifyEvent(self.driver)
        # open add note pop-up
        ve.clickAddNote()
        # Verify pop-up header
        ve.verifyNoteHeader()
        # save note
        ve.saveNote()

    def test_cancleNote(self):

        # add note on created event
        ve = VerifyEvent(self.driver)
        # open add note pop-up
        ve.clickAddNote()
        # cancle note
        ve.cancleNote()

    # created fixture for data driver testing
    @pytest.fixture(params=calanderPageData.test_calanderPage_data)
    def getData(self, request):
        return request.param














