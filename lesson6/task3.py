
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(25)
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

driver.find_element(By.XPATH, '//*[@id="landscape"]')
sleep(5)

href=driver.find_element(By.CSS_SELECTOR, '#award').get_attribute("src")

print(href)