# Assertions here
import pytest
import allure
import time
from tests.pageObjects.loginPage import LoginPage
from tests.pageObjects.dashboardpage import DashboardPage


from selenium import webdriver
#from dotenv import load dotenv
#Start the web
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

@allure.feature("TC#1 - VWO App Positive Test")
@allure.epic("VWO Login Test")

def test_vwologin(setup):
    driver = setup
    driver.get("https://app.vwo.com")
    loginPage = LoginPage(driver)
    loginPage.login_to_vwo(user="contact+atb5x@thetestingacademy.com",pwd="ATBx@1234")
    time.sleep(5)
    assert "Dashboard" in driver.title
    time.sleep(2)

def teatDown():
    pass