
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://uitestingplayground.com/dynamicid")

sleep(10)
count=0
for i in range (3):
    
    driver.find_element("xpath", '//button[text()="Button with Dynamic ID"]').click()
    count=count+1
    print(count)


driver.quit()