from selenium.webdriver.chrome import webdriver
from selenium.webdriver.firefox import webdriver
from selenium.webdriver.safari import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FireFoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    firefox_driver_binary = "./geckodriver"
    chrome_driver_binary = "./chromedriver"
    ser_firefox = FirefoxService(firefox_driver_binary)

    firefox_options = FireFoxOptions()
    chrome_options = ChromeOptions()
    browser_name = "chrome"

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
        # firefox_options.add_argument("--headless")
        # firefox_options.add_argument("--disable-gpu")
        # driver = webdriver.Remote("http://localhost:4444" ,desired_capabilities=dc,options=firefox_options)
        driver = webdriver.Remote("http://localhost:4444" ,desired_capabilities=dc)

    elif browser_name == "safari":

        dc = {
            "browserName" : "safari",
            "platformName" : "MAC"
        }
        driver = webdriver.Remote("http://localhost:4444",desired_capabilities=dc)

    elif browser_name == "chrome":
        dc = {
            "browserName": "chrome",
            "platformName": "MAC"
        }
        # chrome_options.add_argument("--headless")
        # chrome_options.add_argument("--disable-gpu")
        # driver = webdriver.Remote("http://192.168.1.189:4444", desired_capabilities=dc,options=chrome_options)
        driver = webdriver.Remote("http://192.168.1.189:4444",desired_capabilities=dc)


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

def test_title(driver) :
    driver.get("https://www.google.com/")
    title = driver.title
    driver.save_screenshot("testgooletitle.png")

    assert title == "Google"