В проекте 5 спринта мной реализовано UI тестирование сайта Stellar Burgers.

Содержание проекта:
curl.py - хранит в себе URL-адреса используемых страниц,
data.py - хранит учетные данные, 
geniration_ep.py - хранит функции для генерации данных,
locators.py - хранит в себе локаторы,
conftest.py - хранит в себе фикстуры

В папке tests хранятся сами тесты:

**test_check_entrance:**
1. Тест входа в аккаунт по кнопке «Войти в аккаунт» на главной странице
test_enter_account_main_page_valid_credentials_account_opened
2. Тест входа через кнопку «Личный кабинет»
test_enter_account_account_page_valid_credentials_account_opened
3. Тест входа со страницы регистрации
test_enter_account_registration_form_valid_credentials_account_opened

**test_constructor**
1. Тест перехода к разделу "Соусы"
test_sauces_scroll_to_sauces_section
2. Тест перехода к разделу "Булки"
test_buns_scroll_to_buns_section
3. Тест перехода к разделу "Начинки"
test_fillings_scroll_to_fillings_section

**test_exit_account**
1. Тест выхода из аккаунта
test_exit_account_main_site_opened

**test_move_to_account**
1. Тест перехода в личный кабинет
test_account_account_opened

**test_move_to_constructor**
1. Тест перехода из «Личного кабинета» в «Конструктор»
test_constructor_main_site_opened
2. Тест перехода из «Личного кабинета» в «Конструктор» по клику на логотип
test_constructor_logo_main_site_opened

**test_registration**
1. Тест регистрации валидных данных
test_success_registration
2. Тест появления ошибки при вводе невалидных данных
test_registration_invalid_password_error_message
3. Тест появления ошибки, если пароль не задан
test_registration_empty_password_no_message





