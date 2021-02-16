from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

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
    print(lang.get_attribute("id"))

    login_btn = WebDriverWait(browser, 20).until(
        EC.visibility_of_element_located((By.ID, "login_link")))
    #actual_url_login = login_btn.get_attribute("href")

    #сравнение актуальной ссылки на логин с ожидаемой
    #assert "http://selenium1py.pythonanywhere.com/ru/accounts/login/" == actual_url_login
    #print(lang_btn.get_attribute("href"))

    #basket = WebDriverWait(browser, 20).until(
        #EC.visibility_of_element_located((By.CLASS_NAME, "basket-mini pull-right hidden-xs")))
    #actual_url_login = login_btn.get_attribute("href")

    # сравнение актуальной ссылки на логин с ожидаемой
    #assert "http://selenium1py.pythonanywhere.com/ru/accounts/login/" == actual_url_login
    #print(basket.get_attribute("class"))



finally:
    browser.quit()


