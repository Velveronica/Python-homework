
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


class Input:
    def __init__(self, browser) -> None:

        self.browser=browser
        self.browser.get("https://www.saucedemo.com/")

    @allure.step("Авторизация, {client}:{password}")
    def vhod(self, client, password):

        self.browser.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(client)
        self.browser.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
        self.browser.find_element(By.XPATH, '//*[@id="login-button"]').click()