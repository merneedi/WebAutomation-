import time

import allure
import pytest

from tests.pageObjects.loginPage import LoginPage


class TestLogin():

    @allure.feature("TC#1 - VWO App Positive Test")
    @allure.epic("VWO Login Test")
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_positive(self, setup):
        driver = setup
        driver.get(self.base_url)
        # driver.get("https://app.vwo.com")
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user=self.username, pwd=self.password)
        time.sleep(5)
        assert "Dashboard" in driver.title
        time.sleep(2)

    @allure.feature("TC#2 - VWO App Negative Test")
    @allure.epic("VWO Login Test")
    @pytest.mark.usefixtures("setup")
    def test_vwo_login_negative(self, setup):
        driver = setup
        driver.get(self.base_url)
        # driver.get("https://app.vwo.com")
        loginPage = LoginPage(driver)
        loginPage.login_to_vwo(user="admin", pwd="admin")
        time.sleep(5)
        error_message = loginPage.get_error_message_text()
        assert error_message == "Your email, password, IP address or location did not match"
        time.sleep(2)
