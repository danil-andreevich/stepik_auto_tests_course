from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Открываем браузер
browser = webdriver.Chrome()

try:
    # 1. Открыть страницу
    browser.get("http://suninjuly.github.io/alert_accept.html")

    # 2. Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 3. Принять confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # 4. Решить капчу для роботов
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Получить результат
    time.sleep(5)  # Ждем, чтобы увидеть результат
finally:
    # Закрыть браузер
    browser.quit()