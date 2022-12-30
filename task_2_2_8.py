from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


with open("str.txt", "w") as f:
    f.write("not a empty file now!")
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'str.txt')
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.XPATH, '//input[contains(@placeholder,"first name")]')
    first_name.send_keys("Petr")
    last_name = browser.find_element(By.XPATH, '//input[contains(@placeholder,"last name")]')
    last_name.send_keys("Ivanov")
    email = browser.find_element(By.XPATH, '//input[contains(@placeholder,"email")]')
    email.send_keys("mail@mail.ru")
    browser.find_element(By.XPATH, '//input[@type="file" and @required]').send_keys(file_path)


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()