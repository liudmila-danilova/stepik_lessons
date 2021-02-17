from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_1():     #Тестовый сценарий 1.3.1 Переход на страницу регистрации пользователя

    '''
    Шаги:
- Шаг 1 | Найти кнопку Войти и зарегистрироваться | Кнопка Войти и зарегистрироваться есть на странице
- Шаг 2 | Кликнуть на ссылку | Происходит переход на страницу логина пользователя http://selenium1py.pythonanywhere.com/ru/accounts/login/.
    Предусловия:
Находиться на странице http://selenium1py.pythonanywhere.com/ru/
Быть незалогиненным.
    '''

    link = "http://selenium1py.pythonanywhere.com/ru/"
    search_button_login = "login_link"
    search_active_login_page = "[class='active']"


    try:
        browser = webdriver.Chrome()
        browser.get(link)

        button_login = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.ID, search_button_login)))
        button_login.click()
        active_login_page = browser.find_element_by_css_selector(search_active_login_page)

        assert "Войти или зарегистрироваться" in active_login_page.text
        print("test_1 'Переход на страницу регистрации пользователя' passed")


    finally:
        browser.quit()

test_1()

