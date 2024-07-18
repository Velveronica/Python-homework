
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_fill_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    driver.find_element(By.XPATH, '/html/body/main/div/form/div[1]/div[1]/label/input').send_keys("Иван")
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[1]/div[2]/label/input').send_keys("Петров")
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[1]/label/input').send_keys("Ленина 55-3")
    #driver.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[2]/label/input').send_keys("")
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[3]/label/input').send_keys("Москва")
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[2]/div[4]/label/input').send_keys("Россия")
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[3]/div[1]/label/input').send_keys("test@skypro.com")
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[3]/div[2]/label/input').send_keys("+7985899998787")
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[4]/div[1]/label/input').send_keys("QA")
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[4]/div[2]/label/input').send_keys("SkyPro")

    sleep(5)
    driver.find_element(By.XPATH, '/html/body/main/div/form/div[5]/div/button').click()

    sleep(5)

    assert "danger" in driver.find_element(By.ID, 'zip-code').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'first-name').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'last-name').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'address').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'e-mail').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'phone').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'city').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'country').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'job-position').get_attribute("class")
    assert "success" in driver.find_element(By.ID, 'company').get_attribute("class")