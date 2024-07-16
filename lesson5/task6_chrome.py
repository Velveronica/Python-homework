
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username" ).send_keys("tomsmith")
driver.find_element(By.ID, "password" ).send_keys("SuperSecretPassword!")

sleep(3)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

sleep(3)
driver.quit()