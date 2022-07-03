from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as firefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def driver():
    firefox_driver_binary = "./geckodriver"
    ser_firefox = FirefoxService(firefox_driver_binary)
    safari_options = SafariOptions()
    firefox_options = FireFoxOptions()
    chrome_options = ChromeOptions()
    browser_name = "firefox"

    # if isinstance(browserName,list):
    #     for browser_name in browserName:
    if browser_name == "firefox-webdriver":
        driver = webdriver.Firefox(service=ser_firefox)
    elif browser_name == "firefox":
        dc = {
            "browserName": "firefox",
            #"browserVersion": "101.0.1(x64)",
            "platformName": "MAC"
        }
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--disable-gpu")
        driver = webdriver.Remote("http://localhost:4444" ,desired_capabilities=dc,options=firefox_options)

    elif browser_name == "safari":
        safari_options.add_argument("--headless")
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
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Remote("http://192.168.1.189:4444", desired_capabilities=dc,options=chrome_options)

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

# def test_title(driver):
#     driver.get("https://www.google.com/")
#     title = driver.title
#     driver.save_screenshot("testgooletitle.png")
#
#     assert title == "Google"