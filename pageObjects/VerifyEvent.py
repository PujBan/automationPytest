import time

from selenium.webdriver.common.by import By


class VerifyEvent:
    title_created_event = (By.XPATH,"//span[contains(@class,'selectable')]//span[1]")
    notes = (By.XPATH, "//*[contains(@class,'custom-note-btn')]")
    note_popup_header = (By.XPATH, "//div[normalize-space()='Add Note']")
    add_note = (By.XPATH, "//*[contains(@class,'ui form')]")
    save = (By.XPATH, "//*[contains(@class,'green button')]")
    cancle = (By.XPATH, "//*[contains(@class,'red button')]")

    # Constructor
    def __init__(self, driver):
        self.driver = driver

    def getEventTitle(self):
        return self.driver.find_element(*VerifyEvent.title_created_event)

    def clickAddNote(self):
        self.driver.find_element(*VerifyEvent.notes).click()

    def verifyNoteHeader(self):
        popup = self.driver.find_element(*VerifyEvent.note_popup_header)
        assert popup.text == "Add Note", "Add note pop-up not opened"

    def enterNote(self):
        self.driver.find_element(*VerifyEvent.add_note).send_keys('Lorem Ipsum is simply dummy text of the printing and typesetting industry')


    def saveNote(self):
        self.driver.find_element(*VerifyEvent.save).click()

    def cancleNote(self):
        self.driver.find_element(*VerifyEvent.cancle).click()




