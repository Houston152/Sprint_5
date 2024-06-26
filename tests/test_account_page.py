from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestPersonalAccountPageInStellarBurgers:

    def test_constructor_button_constructor_page_opens(self, login, driver):
        driver.find_element(*Locators.ACCAUNT_BUTTON).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MENU_INGRIDIENTS))

    def test_stellar_burgers_button_constructor_page_opens(self, login, driver):
        driver.find_element(*Locators.LOGO).click()
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MENU_INGRIDIENTS))
