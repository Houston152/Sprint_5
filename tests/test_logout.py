from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestLogout:
    def test_logout(self, login, driver):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.ACCAUNT_BUTTON)).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.PROFILE_EXIT_BUTTON)).click()

        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.AUTHORIZATION_PANEL))
