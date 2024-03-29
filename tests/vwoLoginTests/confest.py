import os

import pytest
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()

    username = os.getenv("NAME")
    password = os.getenv('PASSWORD')
    base_url = os.getenv("BASE_URL")
    katalon_url = os.getenv("KATALON_URL")
    #driver.get(base_url)

    request.cls.driver = driver
    request.cls.username = username
    request.cls.password = password
    request.cls.base_url = base_url
    request.cls.katalon_url = katalon_url

    yield driver  # automatically close the driver when it is not required and this is a s/gn to py int -> driver(sometime) > quiet

    driver.quit()
