from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os 

try :
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    inputf = browser.find_element(By.XPATH , "//div[@class='form-group']//input[@name='firstname']")
    inputf.send_keys("Vlad")
    inputl = browser.find_element(By.XPATH , "//div[@class='form-group']//input[@name='lastname']")
    inputl.send_keys("Zharkov")
    inputl = browser.find_element(By.XPATH , "//div[@class='form-group']//input[@name='email']")
    inputl.send_keys("zharkov@mail.com")
    time.sleep(1)
    
    # получаем путь к директории текущего исполняемого файла    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # добавляем к этому пути имя файла    
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element(By.ID , "file")
    element.send_keys(file_path)
    time.sleep(1)
    button = browser.find_element(By.TAG_NAME,"button")
    button.click()
    
     
    
finally:
    
    time.sleep(10)
    browser.quit()