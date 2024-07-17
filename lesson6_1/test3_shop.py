
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_fill_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys("standard_user")
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys("secret_sauce")
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    sleep(5)

    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-onesie"]').click()
    sleep(5)
    driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
    driver.find_element(By.XPATH, '//*[@id="checkout"]').click()

    driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("Nica")
    driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("Prokopets")
    driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("630000")
    driver.find_element(By.XPATH, '//*[@id="continue"]').click()
    total=driver.find_element(By.XPATH, '//*[@id="checkout_summary_container"]/div/div[2]/div[8]').text

    driver.quit()

    assert "58.29" in total


