from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.XPATH, '//span[@id="num1"]').text)
    y = int(browser.find_element(By.XPATH, '//span[@id="num2"]').text)
    select = Select(browser.find_element(By.XPATH, '//select[@class="custom-select"]'))
    select.select_by_visible_text(str(x+y))
    browser.find_element(By.XPATH, '//button[@class="btn btn-default"]').click()

except Exception as e:
    print(e.with_traceback())

finally:
    time.sleep(10)
    browser.quit()
