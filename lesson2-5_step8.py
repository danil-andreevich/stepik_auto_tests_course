from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


# Функция для вычисления значения математической задачи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Открываем браузер
browser = webdriver.Chrome()

try:
    # Переходим на страницу
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Ждем, пока цена не станет равной $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # Нажимаем кнопку "Book"
    browser.find_element(By.ID, "book").click()

    # Находим значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

    # Вводим ответ в поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    # Отправляем форму
    browser.find_element(By.ID, "solve").click()
    time.sleep(10)

finally:
    browser.quit()
