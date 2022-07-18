from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.TAG_NAME,"button").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x = browser.find_element(By.ID,"input_value")
    x = x.text
    y = calc(x)
    
    input1 = browser.find_element(By.ID,"answer")
    input1.send_keys(y)
    time.sleep(1)
    button = browser.find_element(By.TAG_NAME , "button")
    button.click()
    

finally:
 
    time.sleep(15)
    browser.quit()