from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from curl import *


class TestConstructor:

    def test_constructor_main_site_opened(self, driver, login):  #тест переход из «Личного кабинета» в «Конструктор»

        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()
        WebDriverWait(driver, 7).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site


    def test_constructor_logo_main_site_opened(self, driver, login):  #тест перехода из «Личного кабинета» в «Конструктор» по клику на логотип

        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 7).until(EC.url_to_be(main_site))
        assert driver.current_url == main_site