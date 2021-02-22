from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_goto_signup_page():  # Тестовый сценарий 1.3.1 Переход на страницу регистрации пользователя

    '''
    Шаги:
- Шаг 1 | Найти кнопку Войти и зарегистрироваться | Кнопка Войти и зарегистрироваться есть на странице
- Шаг 2 | Кликнуть на ссылку | Происходит переход на страницу логина пользователя http://selenium1py.pythonanywhere.com/ru/accounts/login/.
    Предусловия:
Находиться на странице http://selenium1py.pythonanywhere.com/ru/
Быть незалогиненным.
    '''

    link = "http://selenium1py.pythonanywhere.com/ru/"
    button_login_locator = "login_link"
    active_login_page_locator = "[class='active']"

    try:
        #arrange
        browser = webdriver.Chrome()
        browser.get(link)

        #act
        button_login = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, button_login_locator)))
        button_login.click()
        active_login_page = browser.find_element_by_css_selector(active_login_page_locator)

        #assert
        assert "Войти или зарегистрироваться" in active_login_page.text, "Неверная страница!"
        print("test_goto_signup_page 'Переход на страницу регистрации пользователя' passed")


    finally:
        browser.quit()


test_goto_signup_page()
