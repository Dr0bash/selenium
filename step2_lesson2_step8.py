from selenium import webdriver
import time
import math
import os
    
try: 

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 

    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    firstname_input = browser.find_element_by_css_selector(".form-group input[name='firstname']")
    lastname_input = browser.find_element_by_css_selector(".form-group input[name='lastname']")
    email_input = browser.find_element_by_css_selector(".form-group input[name='email']")
    file_attach = browser.find_element_by_css_selector("input#file")
    button = browser.find_element_by_css_selector("button.btn")
    
    firstname_input.send_keys("kekweshnik")
    lastname_input.send_keys("kekov")
    email_input.send_keys("da@mail.ru")
    file_attach.send_keys(file_path)
   
    time.sleep(1);
    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()