
import allure
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from form_page import Formtest

@allure.epic("Проверка формы") 
@allure.severity("blocker")

@allure.id("SKYPRO-1")
@allure.story("Заполнение формы")
@allure.feature("CREATE")
@allure.title("Заполнение формы с одним пустым полем")
@allure.description("Проверка подсветки заполненных и незаполненных полей формы")

def test_fill_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    form=Formtest(driver)

    form.pill_form("Иван", "Петров", "Ленина 55-3", "", "Москва", "Россия", "test@skypro.com", "+7985899998787", "QA","SkyPro")
    form.click_submit()
    assert "danger" in form.color_check('zip-code')
    assert "success" in form.color_check('first-name')
    assert "success" in form.color_check('last-name')
    assert "success" in form.color_check('address')
    assert "success" in form.color_check('e-mail')
    assert "success" in form.color_check('phone')
    assert "success" in form.color_check('city')
    assert "success" in form.color_check('country')
    assert "success" in form.color_check('job-position')
    assert "success" in form.color_check('company')
