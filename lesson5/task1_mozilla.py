
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

for i in range (5):
    
    driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()

    del_but=driver.find_elements(By.XPATH, '//button[text()="Delete"]')

print({len(del_but)})

driver.quit()