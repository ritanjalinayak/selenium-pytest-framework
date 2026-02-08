import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture

def initial_setup():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

    time.sleep(2)
    yield driver
    driver.quit()
    


