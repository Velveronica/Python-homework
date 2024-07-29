
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")

driver.find_element(By.ID, "username" ).send_keys("tomsmith")
driver.find_element(By.ID, "password" ).send_keys("SuperSecretPassword!")

sleep(3)

driver.find_element(By.XPATH, "//button[@type='submit']").click()

sleep(3)
driver.quit()