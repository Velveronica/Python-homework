
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)
driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p' ).click()

driver.quit()

