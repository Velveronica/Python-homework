
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_fill_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.find_element(By.XPATH, '//*[@id="delay"]').clear()
    driver.find_element(By.XPATH, '//*[@id="delay"]').send_keys(45)

    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
    driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()
    WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))

    sum=driver.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').text
    assert sum=="15"