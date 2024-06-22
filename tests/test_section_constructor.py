import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestConstructorSectionInStellarBurgers:

    @pytest.mark.parametrize('element,section', [
        [Locators.FILLING, Locators.FILLING_SECTION],
        [Locators.SAUCE, Locators.SAUCE_SECTION],
        [Locators.BUN, Locators.BUN_SECTION]
    ])
    def test_switching_between_sections_desired_section_is_displayed(self, login, driver, element, section):
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.MENU_INGRIDIENTS))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(element)).click()

        assert WebDriverWait(driver, 5).until(
            EC.text_to_be_present_in_element_attribute(section, 'class', 'tab_tab_type_current'))