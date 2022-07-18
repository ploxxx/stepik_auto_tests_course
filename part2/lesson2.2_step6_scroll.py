from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try :
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element(By.ID,"input_value")
    x = x.text
    y = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)    
    browser.find_element(By.ID, "robotCheckbox").click()
    time.sleep(1)
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.ID , "robotsRule").click()
    time.sleep(1)
    button = browser.find_element(By.TAG_NAME , "button")    
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()  
    
finally:
    
    time.sleep(10)
    browser.quit()