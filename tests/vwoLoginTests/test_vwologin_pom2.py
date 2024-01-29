
import time

import allure
import pytest
from selenium import webdriver

from tests.pageObjects.loginPage import LoginPage

class TestLogin():
    @pytest.fixture
    def setup(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://app.vwo.com")
        return driver

    @allure.feature("TC#1 - VWO App Positive Test")
    @allure.epic("VWO Login Test")
    def test_vwo_login_positive(self,setup):
        driver = setup

        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user="contact+atb5x@thetestingacademy.com", pwd="ATBx@1234")
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)

    @allure.feature("TC#2 - VWO App Negative Test")
    @allure.epic("VWO Login Test")
    def test_vwo_login_negative(self,setup):
        driver = setup
        
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user="admin", pwd="admin")
        time.sleep(5)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"
        time.sleep(2)
