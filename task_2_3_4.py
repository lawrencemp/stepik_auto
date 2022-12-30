from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()
    browser.switch_to.alert.accept()
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    browser.find_element(By.XPATH, '//input[@id="answer" and @required]').send_keys(calc(x))
    browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()

except Exception as e:
    print(e.with_traceback())
finally:
    time.sleep(10)
    browser.quit()

