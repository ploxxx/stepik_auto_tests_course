from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
import time
import math


try: 
    link = "https://stepik.org/lesson/236895/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(5)
    input1 = browser.find_element(By.XPATH,"//textarea")
    input1.send_keys(str(math.log(int(time.time()))))
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='submit-submission']").click()
    p = browser.find_element(By.TAG_NAME , "p")
    p = p.text
    assert "Correct!" == p , "Error"

    

finally:
 
    time.sleep(15)
    browser.quit()