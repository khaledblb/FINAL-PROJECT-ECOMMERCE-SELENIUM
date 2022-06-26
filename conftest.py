import pytest
import selenium.webdriver as webdriver

@pytest.fixture(autouse=True)
def driver():
    WEBSITE_URL = "https://www.bestbuy.com/?intl=nosplash"
    WEBSITE_URL = "https://www.saucedemo.com/"
    chrome_driver_binary = "./drivers/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options = chrome_options)

    safari_driver_binary = "/usr/bin/safaridriver"
    # driver = webdriver.Safari()
    driver.get(WEBSITE_URL)

    # driver.fullscreen_window()
    yield driver
    driver.close()