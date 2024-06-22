import time
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestRegistration:
    def test_registration_successful_registration(self, driver):
        driver.find_element(*Locators.ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_PAGE_BUTTON)).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.REGISTRATION_HEADER))
        driver.find_element(*Locators.REGISTRATION_NAME_FIELD).send_keys('Андрей')
        driver.find_element(*Locators.REGISTRATION_EMAIL_FIELD).send_keys('vinogradov_andrey_10_111@yandex.ru')
        driver.find_element(*Locators.REGISTRATION_PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.PASSWORD_FIELD))
        time.sleep(3)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('vinogradov_andrey_10_111@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.ACCAUNT_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element_attribute(Locators.PROFILE_EMAIL_FIELD, 'value', 'vinogradov_andrey_10_111@yandex.ru'))

    def test_registration_invalid_password_unsuccessful_registration(self, driver):

        driver.find_element(*Locators.ACCAUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_PAGE_BUTTON)).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.REGISTRATION_HEADER))
        driver.find_element(*Locators.REGISTRATION_NAME_FIELD).send_keys('Андрей')
        driver.find_element(*Locators.REGISTRATION_EMAIL_FIELD).send_keys('vinogradov_andrey_10_111@yandex.ru')
        driver.find_element(*Locators.REGISTRATION_PASSWORD_FIELD).send_keys('12345')
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        incorrect_password = driver.find_element(*Locators.INVALID_PASSWORD).text

        assert incorrect_password == 'Некорректный пароль'
