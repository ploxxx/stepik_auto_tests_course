from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
#driver = webdriver.Firefox()

driver.get("https://stepik.org/lesson/25969/step/8")

