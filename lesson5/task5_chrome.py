
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(3)
input=driver.find_element(By.CSS_SELECTOR, '#content > div > div > div > input[type=number]' )

input.send_keys("1000")

sleep(3)
input.clear()

input.send_keys("999")
sleep(3)
driver.quit()