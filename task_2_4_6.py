import time
from selenium import webdriver
from selenium.webdriver.common.by import By


link = 'http://suninjuly.github.io/cats.html'
browser = webdriver.Chrome()
browser.find_element(By.ID, "button")
time.sleep(3)
browser.quit()
