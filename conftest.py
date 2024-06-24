import pytest
from selenium import webdriver
from locators import Locators
from urls import Urls
from user_data import email_user, password_user


url = Urls().urls()


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get(url)
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ACCAUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(email_user)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password_user)
    driver.find_element(*Locators.LOGIN_BUTTON).click()
