from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  
try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("treasure")
    
    answer_element = browser.find_element_by_id("answer")
    checkbox = browser.find_element_by_id("robotCheckbox")
    radiobutton = browser.find_element_by_id("robotsRule")
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    button = browser.find_element_by_css_selector("button.btn")
    
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"
    
    robots_checked = radiobutton.get_attribute("checked")
    assert robots_checked is None
    
    x = x_element.get_attribute("valuex")
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