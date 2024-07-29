
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
from input import Input
from order import Order
from shop import Shopping

@allure.epic("Заказ в интернет-магазине") 
@allure.severity("blocker")

@allure.id("SKYPRO-1")
@allure.story("Заказ в интернет-магазине")
@allure.feature("CREATE")
@allure.title("Определение полной стоимости интернет-заказа")
@allure.description("Авторизация в интернет-магазине, выбор товаров, оформление заказа и получение итоговой стоимости")
def test_shop():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    client=Input(driver)
    client.vhod("standard_user", "secret_sauce")

    ORDER=Shopping(driver)
    ORDER.choise('//*[@id="add-to-cart-sauce-labs-backpack"]')
    ORDER.choise('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]')
    ORDER.choise('//*[@id="add-to-cart-sauce-labs-onesie"]')

    ORDER.cart()

    Address=Order(driver)
    Address.pill_form("Nica", "Prokopets", "630000")
    Address.click_continue()
    Address.price()
    assert "58.29" in Address.price()
