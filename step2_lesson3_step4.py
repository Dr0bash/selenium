from selenium import webdriver
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
    
try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    button_mage = browser.find_element_by_css_selector("button.btn")
    button_mage.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    button = browser.find_element_by_css_selector("button.btn")
    
    x = x_element.text
    answer.send_keys(calc(x))
   
    time.sleep(1);
    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()