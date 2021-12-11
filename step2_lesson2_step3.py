from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
  
  
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Поиск элементов страницы
    sum_a = browser.find_element_by_css_selector("span#num1")
    sum_b = browser.find_element_by_css_selector("span#num2")
    sum_x = int(sum_a.text) + int(sum_b.text)
    sum_x = str(sum_x)
    submit_button = browser.find_element_by_css_selector("button.btn")
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum_x)
    
    time.sleep(1)
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()