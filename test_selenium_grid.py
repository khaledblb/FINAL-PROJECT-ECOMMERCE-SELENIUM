import time
from select import select
from selenium.common import NoSuchElementException, ElementNotInteractableException, TimeoutException, \
    StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pytest
'''
@pytest.fixture()
def driver():
    firefox_driver_binary = "./geckodriver"
    ser_firefox = FirefoxService(firefox_driver_binary)

    browser_name = "safari"

    # if isinstance(browserName,list):
    #     for browser_name in browserName:
    if browser_name == "firefox-webdriver":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":
        dc = {
            "browserName": "firefox",
            # "browserVersion": "101.0.1(x64)",
            "platformName": "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444",desired_capabilities=dc)

    elif browser_name == "safari":
        dc = {
            "browserName": "safari",
            "platformName": "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444",desired_capabilities=dc)

    elif browser_name == "chrome":
        dc = {
            "browserName": "chrome",
            "platformName": "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)

    elif browser_name == "firefox-mobile":
        firefox_options = FireFoxOptions()
        firefox_options.add_argument("--width=375")
        firefox_options.add_argument("--height=812")
        firefox_options.set_preference("general.useragent.override", "userAgent=Mozilla/5.0 "
                                                                     "(iPhone; CPU iPhone OS 15_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like "
                                                                     "Gecko) CriOS/101.0.4951.44 Mobile/15E148 Safari/604.1")
        # firefox_options.set_preference("general.useragent.override", "Nexus 7")

        driver = webdriver.Firefox(service=ser_firefox, options=firefox_options)

    yield driver
    driver.close()
'''