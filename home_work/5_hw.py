from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.saucedemo.com/')

username = driver.find_element(By.CSS_SELECTOR, '#user-name')
password = driver.find_element(By.CSS_SELECTOR, '#password')
submit = driver.find_element(By.CSS_SELECTOR, '#login-button')


def test_page(a, b, c):
    if None in [a, b, c]:
        text = 'Элемент/Элементы не найдены'
    else:
        text = 'Элементы найдены'
    return text


print(test_page(username, password, submit))