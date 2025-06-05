from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *



class TestMoveToAccount:

    def test_account_account_opened(self, driver, login): #тест перехода в личный кабинет

        driver.find_element(*Locators.ACCOUNT).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(profile_site))

        assert driver.current_url == profile_site
