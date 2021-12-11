from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
  
  
try: 
    browser = webdriver.Chrome()
    browser.execute_script("document.title='Script executing';alert('Robots at work');")

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()