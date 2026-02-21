from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import configparser

def get_driver():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    browser = config["DEFAULT"]["browser"]

    if browser == "chrome":
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
    else:
        raise Exception("Browser not supported")

    driver.maximize_window()
    return driver
