from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Открываем браузер
browser = webdriver.Chrome()

try:
    # 1. Открыть страницу
    browser.get("https://suninjuly.github.io/selects1.html")

    # 2. Посчитать сумму заданных чисел
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    result = str(num1 + num2)

    # 3. Выбрать в выпадающем списке значение, равное рассчитанной сумме
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(result)

    # 4. Нажать кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Ждем, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрываем браузер
    browser.quit()