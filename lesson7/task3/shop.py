
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


class Shopping:
    def __init__(self, browser) -> None:

        self.browser=browser
        self.browser.get("https://www.saucedemo.com/inventory.html")

    @allure.step("Выбрать товар {product}")
    def choise(self, product: str):
        
        self.browser.find_element(By.XPATH, product).click()

    @allure.step("Перейти в корзину и оформить заказа")
    def cart(self):
        
        self.browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
        self.browser.find_element(By.XPATH, '//*[@id="checkout"]').click()