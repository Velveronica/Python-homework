
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://uitestingplayground.com/textinput?")


input=driver.find_element(By.XPATH, '//*[@id="newButtonName"]' )

input.send_keys("Skypro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()
name=driver.find_element(By.CSS_SELECTOR, "#updatingButton").text
print(name)