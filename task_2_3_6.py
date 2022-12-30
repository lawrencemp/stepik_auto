from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x: str):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.XPATH, '//button[@class="trollface btn btn-primary"]').click()
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(calc(x))
    browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

except Exception as e:
    print(e.with_traceback())
finally:
    time.sleep(10)
    browser.quit()
