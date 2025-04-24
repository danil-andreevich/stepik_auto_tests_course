from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import math
import time

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открываем браузер
browser = webdriver.Chrome()

try:
    # 1. Открыть страницу
    link = "https://suninjuly.github.io/math.html"
    browser.get(link)

    # 2. Считать значение для переменной x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text

    # 3. Посчитать математическую функцию от x
    y = calc(x)

    # 4. Ввести ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 5. Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # 6. Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # 7. Нажать на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Ждем, чтобы увидеть результат
    time.sleep(10)

finally:
    # Закрываем браузер
    browser.quit()