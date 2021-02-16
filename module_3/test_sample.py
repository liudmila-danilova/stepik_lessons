from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    #Тестовый сценарий 1.1.1 Просмотр главной страницы при незалогиненном пользователе
    browser = webdriver.Chrome()
    browser.get("http://selenium1py.pythonanywhere.com/ru/")

    #здесь неудачная попытка получить заголовок и сравнить его с ожидаемым результатом
    #title = browser.title
    #text_title = (title.text)
    #print(text_title)
    #assert "Oscar - Sandbox" == text_title

    #проверяем на видимость блок выбора языка
    lang = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, "language_selector")))

    #проверка на видимость блока логина
    login_btn = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, "login_link")))
    actual_url_login = login_btn.get_attribute("href")

    #сравнение актуальной ссылки на логин с ожидаемой
    assert "http://selenium1py.pythonanywhere.com/ru/accounts/login/" == actual_url_login


    basket_look = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "span>a")))
    actual_url_basket_look = basket_look.get_attribute("href")

    #сравнение актуальной ссылки на корзину с ожидаемой
    assert "http://selenium1py.pythonanywhere.com/ru/basket/" == actual_url_basket_look

finally:
    browser.quit()


