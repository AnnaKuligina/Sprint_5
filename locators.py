from selenium.webdriver.common.by import By


class Locators:

    ACCOUNT = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]") # кнопка "Личный Кабинет"
    REG_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']") # ссылка Зарегистрироваться
    USER_NAME = (By.XPATH, "//div[label[contains(text(),'Имя')]]//input") # Имя в форме регистрации
    EMAIL = (By.XPATH, "//div[label[contains(text(),'Email')]]//input") # Email в форме регистрации
    PASSWORD = (By.XPATH, "//input[@name= 'Пароль']") # Пароль в форме регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']") # Кнопка "Зарегистрироваться" в форме регистрации
    INCORRECT_PASSWORD_MESSAGE = (By.XPATH, "//p[text()='Некорректный пароль']") # Сообщение "Некорректный пароль"
    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    ENTER_BUTTON = (By.XPATH, "//button[text()='Войти']") # Кнопка "Войти" в форме входа
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']") # Кнопка "Оформить заказ"
    ENTER_LINK = (By.XPATH, "//a[text()='Войти']") # ссылка Войти в форме регистрации
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']") # ссылка Восстановить пароль
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']") # Кнопка "Конструктор"
    LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]/a") # Логотип сайта
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']") # Кнопка "Выход" в личном кабинете
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div") # меню Булки
    BUNS_SECTION_TITLE = (By.XPATH, "//h2[text()='Булки']")  # раздел "Булки"
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div") # меню Соусы
    SAUCES_SECTION_TITLE = (By.XPATH, "//h2[text()='Соусы']")  # раздел "Соусы"
    FILINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div") # меню Начинки
    FILLINGS_SECTION_TITLE = (By.XPATH, "//h2[text()='Начинки']") # раздел "Начинки"