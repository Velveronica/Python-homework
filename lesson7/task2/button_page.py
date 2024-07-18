
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Calc:
    def __init__(self, browser) -> None:

        self.browser=browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def timer(self, time):
        
        self.browser.find_element(By.XPATH, '//*[@id="delay"]').clear()
        self.browser.find_element(By.XPATH, '//*[@id="delay"]').send_keys(time)
        
        
    def summ(self):

        self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def wait(self, time):
        
        WebDriverWait(self.browser, time+1).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))

    def get_sum(self):

        return self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').text
       