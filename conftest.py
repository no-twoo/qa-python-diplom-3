import pytest
from selenium import webdriver
from pages.login_page import *
from data import *


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    driver = None
    if request.param == "firefox":
        driver = webdriver.Firefox()
    elif request.param == "chrome":
        driver = webdriver.Chrome()

    driver.set_window_size(1920, 1080)

    yield driver
    driver.quit()


@pytest.fixture()
def login(driver):
    login_user = LoginPage(driver, LOGIN_URL)
    login_user.set_email()
    login_user.set_password()
    login_user.check_button_login()
