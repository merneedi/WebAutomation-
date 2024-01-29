import time

import allure
import pytest

from tests.pageObjects.KatalonLoginPage import KatalonLoginPage


class TestLogin():

    @allure.epic("Katalon home page")
    @allure.feature("TC#1 - katalon home page")
    @pytest.mark.usefixtures("setup")
    @pytest.mark.smoke
    def test_katalon_login_positive(self, setup):
        driver = setup
        driver.get(self.katalon_url)
        # driver.get("https://app.vwo.com")
        khp = KatalonLoginPage(driver)
        khp.click_homepage()
        time.sleep(5)
        assert "profile.php#login" in driver.current_url
        time.sleep(2)


