import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


class TestRandomCases(unittest.TestCase):
    # test for first registration page
    def test_from_task_1_6_11_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, '//input[contains(@placeholder,"first name")]')
        first_name.send_keys("Petr")
        last_name = browser.find_element(By.XPATH, '//input[contains(@placeholder,"last name")]')
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.XPATH, '//input[contains(@placeholder,"email")]')
        email.send_keys("mail@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    # test for second registration page
    def test_from_task_1_6_11_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element(By.XPATH, '//input[contains(@placeholder,"first name")]')
        first_name.send_keys("Petr")
        last_name = browser.find_element(By.XPATH, '//input[contains(@placeholder,"last name")]')
        last_name.send_keys("Ivanov")
        email = browser.find_element(By.XPATH, '//input[contains(@placeholder,"email")]')
        email.send_keys("mail@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    pytest.main()

