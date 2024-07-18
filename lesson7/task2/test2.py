
import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from button_page import Calc

def test_calc():

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    sum=Calc(driver)
    sum.timer(45)
    sum.summ()
    sum.wait(45)
    sum.get_sum()

    assert int(sum.get_sum())==15


