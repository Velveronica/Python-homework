
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

for i in range (3):
    
    driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    sleep(3)
    driver.switch_to.alert.accept()

driver.quit()