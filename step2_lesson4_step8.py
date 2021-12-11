from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    book_button = browser.find_element_by_id("book")
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    book_button.click()
    
    x_element = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    button = browser.find_element_by_id("solve")
    
    x = x_element.text
    answer.send_keys(calc(x))
    
    button.click()
    
finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()