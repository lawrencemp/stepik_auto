from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 14).until(EC.text_to_be_present_in_element((By.XPATH, '//h5[@id="price"]'), "100"))
    browser.find_element(By.XPATH, '//button[@class="btn btn-primary"]').click()
    x = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(calc(x))
    browser.find_element(By.XPATH, '//button[@id="solve"]').click()

except Exception as e:
    print(e.with_traceback())
finally:
    time.sleep(10)
    browser.quit()
