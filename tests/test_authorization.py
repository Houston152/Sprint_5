import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestAuthorizationInStellarBurgers:

    @pytest.mark.parametrize("button", [Locators.ENTER_ACCAUNT_BUTTON, Locators.ACCAUNT_BUTTON])
    def test_authorization_through_enter_account_button_successful_authorization(self, driver, button):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(button)).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('vinogradov_andrey_10_000@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACCAUNT_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.PROFILE_NAME_FIELD, 'value', 'Андрей'))

    def test_authorization_through_registration_form_successful_authorization(self, driver):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENTER_ACCAUNT_BUTTON)).click()
        driver.find_element(*Locators.REGISTRATION_PAGE_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('vinogradov_andrey_10_000@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACCAUNT_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.PROFILE_NAME_FIELD, 'value', 'vinogradov_andrey_10_000@yandex.ru'))

    def test_authorization_through_password_recovery_form_successful_authorization(self, driver):
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ENTER_ACCAUNT_BUTTON)).click()
        driver.find_element(*Locators.REGISTRATION_PAGE_BUTTON).click()
        driver.find_element(*Locators.REGISTRATION_LOGIN_BUTTON).click()
        driver.find_element(*Locators.EMAIL_FIELD).send_keys('vinogradov_andrey_10_000@yandex.ru')
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys('123456')
        driver.find_element(*Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.ACCAUNT_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_attribute(Locators.PROFILE_NAME_FIELD, 'value', 'vinogradov_andrey_10_000@yandex.ru'))
