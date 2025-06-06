from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *

class TestExitAccount:

    def test_exit_account_main_site_opened(self, driver, login): #тест выхода из аккаунта

        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(Locators.LOGOUT_BUTTON))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.url_to_be(login_site))
        assert driver.current_url == login_site
