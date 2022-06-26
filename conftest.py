import pytest
import selenium.webdriver as webdriver
# from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(autouse=True)
def driver():

    chrome_driver_binary = "./drivers/chromedriver"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("start-maximized")
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options = chrome_options)
    driver.set_window_size(340,695)

    # firefox_driver_binary = "./drivers/geckodriver"
    # driver = webdriver.Firefox(executable_path=firefox_driver_binary)

    # safari_driver_binary = "/usr/bin/safaridriver"
    # driver = webdriver.Safari()

    WEBSITE_URL = "https://automationexercise.com/"
    driver.get(WEBSITE_URL)
    yield driver
    # TODO->logout
    driver.close()