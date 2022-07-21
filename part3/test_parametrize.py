import unittest
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    #print("\nquit browser..")
    #browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896" , "236897" , "236898", "236899", "236903","236904","236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    time.sleep(5)
    input1 = browser.find_element(By.XPATH,"//textarea")
    input1.send_keys(str(math.log(int(time.time()))))
    time.sleep(3)
    browser.find_element(By.XPATH, "//button[@class='submit-submission']").click()
    time.sleep(3)
    p = browser.find_element(By.TAG_NAME , "p")
    p = p.text
    print(p)
    assert "Correct!" == p , "Error"
    