
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Order:
    def __init__(self, browser) -> None:

        self.browser=browser
        self.browser.get("https://www.saucedemo.com/checkout-step-one.html")

    def pill_form(self, firstname, lastname, zip_code):

        self.browser.find_element(By.XPATH, '//*[@id="first-name"]').send_keys(firstname)
        self.browser.find_element(By.XPATH, '//*[@id="last-name"]').send_keys(lastname)
        self.browser.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(zip_code)

    def click_continue(self):

        self.browser.find_element(By.XPATH, '//*[@id="continue"]').click()

    def price(self):

        return self.browser.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text

