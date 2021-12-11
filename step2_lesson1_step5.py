from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  
try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_css_selector("#input_value")
    answer_element = browser.find_element_by_css_selector("#answer")
    checkbox = browser.find_element_by_css_selector("#robotcheckbox")
    radiobutton = browser.find_element_by_css_selector("#robotsRule")
    button = browser.find_element_by_css_selector("button.btn")
    
    x = x_element.text
    y = calc(x)
    answer_element.send_keys(y)
    checkbox.click()
    radiobutton.click()
    time.sleep(1);


    # Отправляем заполненную форму    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()