from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('http://demoqa.com/')

icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
buttons = driver.find_element(By.CSS_SELECTOR, 'div > div.card-up')
footer = driver.find_element(By.CSS_SELECTOR, 'span')
if icon is None:
    print('Элемент "icon" не найден')
else:
    print('Элемент "icon" найден')
if buttons is None:
    print('Элемент "buttons" не найден')
else:
    print('Элемент "buttons" найден')
if footer is None:
    print('Элемент "footer" не найден')
else:
    print('Элемент "footer" найден')
