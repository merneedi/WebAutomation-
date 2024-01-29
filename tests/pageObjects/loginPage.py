# Page class

# Page Locators
# Page Actions
# Webdriver - Init
# Custom Functions
# No Assertion here

from selenium.webdriver.common.by import By

class LoginPage(object):

    def __init__(self,driver):
        self.driver = driver

    # page locators
    username = (By.ID, "login-username")
    password = (By.NAME, "password")
    Submit_button = (By.XPATH, "//button[@id='js-login-btn']")
    #forgot_pwd__button = (By.XPATH, "//button[normalize-space()='Forgot Password?']")
    error_message = (By.CSS_SELECTOR, "#js-notification-box-msg")
    #free_trail = (By.XPATH, "//a[normalize-space()='Start a free trial']")
    #sso_login = (By.XPATH, "//button[normalize-space()='Sign in using SSO']")
    #remember_checkbox = (By.XPATH,"//span[normalize-space()='Remember me']")


    # Return a WebElement -> username
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.Submit_button)

    def get_error_message(self):
        return self.driver.find_element(*LoginPage.error_message)

    #def get_free_trail(self):
        #return self.driver.find_element(*LoginPage.free_trail)
    #def get_sso_login(self):
        #return self.driver.find_element(*LoginPage.sso_login)

    # page actions
    def login_to_vwo(self,user,pwd):
        self.get_username().send_keys(user)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_message_text(self):
        return self.get_error_message().text

    #def click_free_trail(self):
        #self.get_free_trail().click()