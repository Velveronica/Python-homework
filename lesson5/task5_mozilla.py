
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(3)
input=driver.find_element(By.CSS_SELECTOR, '#content > div > div > div > input[type=number]' )

input.send_keys("1000")

sleep(3)
input.clear()

input.send_keys("999")
sleep(3)
driver.quit()