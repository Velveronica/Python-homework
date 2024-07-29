
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(3)
driver.find_element(By.XPATH, '//*[@id="modal"]/div[2]/div[3]/p' ).click()

sleep(3)
driver.quit()