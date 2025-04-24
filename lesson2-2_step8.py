import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Укажите путь к вашему WebDriver
driver = webdriver.Chrome()

try:
    # 1. Открыть страницу
    driver.get("http://suninjuly.github.io/file_input.html")

    # 2. Заполнить текстовые поля
    driver.find_element(By.NAME, "firstname").send_keys("Иван")
    driver.find_element(By.NAME, "lastname").send_keys("Иванов")
    driver.find_element(By.NAME, "email").send_keys("ivanov@example.com")

    # 3. Создать файл и получить его абсолютный путь
    file_name = "test.txt"
    with open(file_name, "w") as file:
        file.write("Это тестовый файл.")  # Создаем файл
    file_path = os.path.abspath(file_name)  # Преобразуем в абсолютный путь

    # 4. Загрузить файл
    file_input = driver.find_element(By.ID, "file")
    file_input.send_keys(file_path)  # Используем абсолютный путь

    # 5. Нажать кнопку "Submit"
    driver.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Подождать, чтобы увидеть результат
    time.sleep(5)

finally:
    # Закрыть браузер
    driver.quit()