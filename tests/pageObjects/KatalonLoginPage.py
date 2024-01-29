# Page class

# Page Locators
# Page Actions
# Webdriver - Init
# Custom Functions
# No Assertion here

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class KatalonLoginPage(object):

    def __init__(self,driver):
        self.driver = driver

    # page locators
    make_appointment = (By.ID, "btn-make-appointment")

    def get_make_appointment(self):
        return self.driver.find_element(*KatalonLoginPage.make_appointment)


    def click_homepage(self):
        self.get_make_appointment().click()

