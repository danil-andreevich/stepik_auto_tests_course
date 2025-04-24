from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция для вычисления значения
def calculate(x):
    return math.log(abs(12 * math.sin(x)))

# Настройка WebDriver
driver = webdriver.Chrome()  # Убедитесь, что chromedriver установлен
driver.get("http://suninjuly.github.io/redirect_accept.html")

try:
    # Нажать на кнопку
    button = driver.find_element(By.TAG_NAME, "button")
    button.click()

    # Переключиться на новую вкладку
    new_tab = driver.window_handles[1]
    driver.switch_to.window(new_tab)

    # Найти значение x на новой странице
    x_element = driver.find_element(By.ID, "input_value")
    x = int(x_element.text)

    # Вычислить результат
    result = calculate(x)

    # Ввести результат в поле
    answer_field = driver.find_element(By.ID, "answer")
    answer_field.send_keys(str(result))

    # Нажать кнопку Submit
    submit_button = driver.find_element(By.TAG_NAME, "button")
    submit_button.click()

    # Подождать, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрыть браузер
    driver.quit()