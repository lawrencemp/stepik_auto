from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.XPATH, '//img[@id="treasure"]').get_attribute("valuex")
    answer = calc(int(x))
    browser.find_element(By.XPATH, '//input[@id="answer" and @required]').send_keys(answer)
    browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    radio_element = browser.find_element(By.XPATH, '//input[@type="radio" and @value="robots"]')
    radio_element.click()
    if radio_element.get_attribute("checked") is None:
        raise Exception
    browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default').click()
except Exception as e:
    print(e.with_traceback())
finally:
    time.sleep(10)
    browser.quit()

