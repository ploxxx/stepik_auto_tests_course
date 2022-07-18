from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x,y):
  return str(str(int(x)+int(y)))
try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element(By.CSS_SELECTOR, "span#num1")
    x =x.text
    y = browser.find_element(By.CSS_SELECTOR, "span#num2")
    y = y.text
    summ = calc(x,y)
    print(summ)
    #select = browser.find_element(By.ID, "dropdown").click()
    #option = browser.find.element(By.CSS_SELECTOR, "option[value='" + summ + "']")
    #option.click()
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(summ)
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
 
    time.sleep(15)
    browser.quit()