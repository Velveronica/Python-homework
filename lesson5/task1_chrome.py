
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
sleep(5)

for i in range (5):
    
    #driver.find_element(By.XPATH, '//button[text()="Add Element"]').click()]
    driver.find_element(By.XPATH, '//*[@id="content"]/div/button').click()

    del_but=driver.find_elements(By.XPATH, '//button[text()="Delete"]')

print({len(del_but)})

driver.quit()