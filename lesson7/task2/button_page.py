
import allure
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

    @allure.step("Выставить интервал {time}}")
    def timer(self, time: int):
        
        self.browser.find_element(By.XPATH, '//*[@id="delay"]').clear()
        self.browser.find_element(By.XPATH, '//*[@id="delay"]').send_keys(time)
        
    @allure.step("Сложить 7+8=")    
    def summ(self):

        self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
        self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
        self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
        self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    @allure.step("Ожидание интервала {time}+1")
    def wait(self, time: int):
        
        WebDriverWait(self.browser, time+1).until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="calculator"]/div[1]/div'), "15"))

    @allure.step("Получить результата {return}")
    def get_sum(self):

        return self.browser.find_element(By.XPATH, '//*[@id="calculator"]/div[1]/div').text
       