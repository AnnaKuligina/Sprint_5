from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from geniration_ep import generate_wrong_password
from geniration_ep import generate_empty_password
from geniration_ep import generate_registration_data
from locators import Locators
from curl import *

class TestRegistrationWithNewCredentials:

    def test_success_registration(self, driver): #тест регистрации валидных данных: имя, email в формате логин@домен, и минимальным паролем в 6 символов

        email, password, username = generate_registration_data()
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.USER_NAME).send_keys(username)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.url_to_be(login_site))

        assert driver.current_url == login_site


class TestRegistrationWithInvalidPassword:

    def test_registration_invalid_password_error_message(self, driver): #тест появления ошибки при вводе невалидных данных

        email, password, username = generate_wrong_password()
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.USER_NAME).send_keys(username)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        wrong_pw_message = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(Locators.INCORRECT_PASSWORD_MESSAGE)).text

        assert driver.current_url == main_site + 'register'
        assert wrong_pw_message == 'Некорректный пароль'

class TestRegistrationWithEmptyPassword:

    def test_registration_empty_password_no_message(self, driver): #тест появления ошибки, если пароль не задан

        email, password, username = generate_empty_password()
        driver.find_element(*Locators.ACCOUNT).click()
        driver.find_element(*Locators.REG_LINK).click()
        driver.find_element(*Locators.USER_NAME).send_keys(username)
        driver.find_element(*Locators.EMAIL).send_keys(email)
        driver.find_element(*Locators.PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        assert driver.current_url == main_site + 'register'