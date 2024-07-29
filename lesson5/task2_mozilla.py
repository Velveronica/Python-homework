
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("https://uitestingplayground.com/dynamicid")

count=0
for i in range (3):
    
    driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
    count=count+1
    print(count)


driver.quit()