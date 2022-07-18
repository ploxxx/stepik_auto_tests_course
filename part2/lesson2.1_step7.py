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

    # функция text получает текст из выбранного селектора
    x_element = browser.find_element(By.CSS_SELECTOR, "img#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input1.send_keys(y)
    time.sleep(2)
    option1 = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    option1.click()
    time.sleep(2)
    radiobutton = browser.find_element(By.CSS_SELECTOR,"input#robotsRule")
    radiobutton.click()
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
 
    time.sleep(15)
    browser.quit()