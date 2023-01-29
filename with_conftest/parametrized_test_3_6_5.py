import creds
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

urls = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"]
time_to_wait = 13


def authorization(browser):
    login_btn = WebDriverWait(browser, time_to_wait)\
        .until(EC.element_to_be_clickable((By.XPATH, '//a[text() = "Войти" ]')))
    login_btn.click()
    browser.find_element(By.XPATH, '//input[@name="login"]').send_keys(creds.login)
    browser.find_element(By.XPATH, '//input[@name="password"]').send_keys(creds.parol)
    browser.find_element(By.XPATH, '//button[@type="submit"]').click()
    WebDriverWait(browser, time_to_wait).until_not(EC.visibility_of_element_located((By.XPATH, '//div[@class="box"]')))


class Test_3_6_5:
    @pytest.mark.parametrize('url', urls)
    def test_user_see_correct_feedback(self, browser, url):
        browser.get(url)
        authorization(browser)
        answer = math.log(int(time.time()))
        text_area = WebDriverWait(browser, time_to_wait).until(
            EC.visibility_of_element_located((By.XPATH, '//textarea[@required]')))
        text_area.send_keys(str(answer))
        submit_answer_btn = WebDriverWait(browser, time_to_wait)\
            .until(EC.element_to_be_clickable((By.XPATH, '//button[@class="submit-submission"]')))
        submit_answer_btn.click()
        feedback = WebDriverWait(browser, time_to_wait)\
            .until(EC.visibility_of_element_located((By.XPATH, '//p[@class="smart-hints__hint"]')))
        WebDriverWait(browser, time_to_wait)\
            .until(EC.element_to_be_clickable((By.XPATH, '//button[@class="again-btn white"]'))).click()
        assert feedback.text == "Correct!", 'Feedback text is not "Correct!"'
