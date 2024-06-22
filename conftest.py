import pytest
from selenium import webdriver
from locators import Locators


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/')
    yield browser
    browser.quit()


@pytest.fixture
def login(driver):
    driver.find_element(*Locators.ACCAUNT_BUTTON).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys('vinogradov_andrey_10_000@yandex.ru')
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
    driver.find_element(*Locators.LOGIN_BUTTON).click()
