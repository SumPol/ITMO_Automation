from selenium import webdriver
from selenium.webdriver.common.by import By

def search_elements(url: str, field_username: str, field_password: str, button: str):
    driver = webdriver.Chrome()
    driver.get(url)

    f_username = driver.find_element(By.CSS_SELECTOR, field_username)
    f_password = driver.find_element(By.CSS_SELECTOR, field_password)
    f_button = driver.find_element(By.CSS_SELECTOR, button)

    if f_username and f_password and f_button:
        print('Элементы найдены')
    else:
        print('Элементы не найдены')

    driver.quit()

open_url = 'https://www.saucedemo.com/'
username = '[id="user-name"]'
password = '[id="password"]'
button = '[id="login-button"]'

search_elements(open_url, username, password, button)
