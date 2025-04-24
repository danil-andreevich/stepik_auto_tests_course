from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Открываем браузер
browser = webdriver.Chrome()

try:
    # Переходим на страницу
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

    # Вводим ответ
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)
    # Скроллим страницу вниз
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # Отмечаем чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем радиокнопку
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Нажимаем кнопку Submit
    button.click()



finally:
    # Закрываем браузер
    time.sleep(5)
    browser.quit()