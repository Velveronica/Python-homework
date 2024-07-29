
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.implicitly_wait(25)
driver.get("https://uitestingplayground.com/ajax")

driver.find_element(By.XPATH, '//*[@id="ajaxButton"]').click()

content=driver.find_element(By.CSS_SELECTOR, "#content > p")
txt=content.find_element(By.XPATH, '//*[@id="content"]/p').text
print(txt)

driver.quit()