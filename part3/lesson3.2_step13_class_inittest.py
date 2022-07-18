from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestReg(unittest.TestCase) :
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//form/div[1]//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input1 = browser.find_element(By.XPATH, "//form/div[1]//input[@class='form-control second']")
        input1.send_keys("Petrov")
        input2 = browser.find_element(By.XPATH, "//form/div[1]//input[@class='form-control third']")
        input2.send_keys("zharkov.kill@yadnex.by")
        input3 = browser.find_element(By.XPATH, "//form/div[2]//input[@class='form-control first']")
        input3.send_keys("+3343452")
        input4 = browser.find_element(By.XPATH, "//form/div[2]//input[@class='form-control second']")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error")
        
    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.XPATH, "//form/div[1]//input[@class='form-control first']")
        input1.send_keys("Ivan")
        input1 = browser.find_element(By.XPATH, "//form/div[1]//input[@class='form-control second']")
        input1.send_keys("Petrov")
        input2 = browser.find_element(By.XPATH, "//form/div[1]//input[@class='form-control third']")
        input2.send_keys("zharkov.kill@yadnex.by")
        input3 = browser.find_element(By.XPATH, "//form/div[2]//input[@class='form-control first']")
        input3.send_keys("+3343452")
        input4 = browser.find_element(By.XPATH, "//form/div[2]//input[@class='form-control second']")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error")
        
if __name__ == "__main__":
    unittest.main()