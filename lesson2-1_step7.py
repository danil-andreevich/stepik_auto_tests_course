from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функция для вычисления значения
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открываем браузер
browser = webdriver.Chrome()

try:
    # 1. Открыть страницу
    link = "http://suninjuly.github.io/get_attribute.html"
    browser.get(link)

    # 2. Найти элемент-картинку (сундук)
    treasure = browser.find_element(By.ID, "treasure")

    # 3. Взять значение атрибута valuex
    x = treasure.get_attribute("valuex")

    # 4. Посчитать математическую функцию от x
    y = calc(x)

    # 5. Ввести ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # 6. Отметить checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # 7. Выбрать radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # 8. Нажать на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Ждем, чтобы увидеть результат
    time.sleep(10)

finally:
# Закрываем браузер
 browser.quit()