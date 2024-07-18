
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Formtest:
    def __init__(self, browser) -> None:
        
        self.browser=browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    def pill_form(self, firstname, lastname, address, zip_code, city, country, email, telephone, job_position,company):
        
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[1]/div[1]/label/input').send_keys(firstname)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[1]/div[2]/label/input').send_keys(lastname)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[1]/label/input').send_keys(address)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[2]/label/input').send_keys(zip_code)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[3]/label/input').send_keys(city)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[4]/label/input').send_keys(country)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[3]/div[1]/label/input').send_keys(email)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[3]/div[2]/label/input').send_keys(telephone)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[4]/div[1]/label/input').send_keys(job_position)
        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[4]/div[2]/label/input').send_keys(company)
    
    def click_submit(self):

        self.browser.find_element(By.XPATH, '/html/body/main/div/form/div[5]/div/button').click()

    def color_check(self, element):

        return self.browser.find_element(By.ID, element).get_attribute("class")




