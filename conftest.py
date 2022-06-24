import pytest
import selenium.webdriver as webdriver

@pytest.fixture(autouse=True)
def driver():
    chrome_driver_binary = "./drivers/chromedriver"
    # safari_driver_binary = "/usr/bin/safaridriver"
    driver = webdriver.Chrome(chrome_driver_binary)
    # driver = webdriver.Safari()
    driver.get("https://www.bestbuy.com/?intl=nosplash")
    yield driver
    driver.close()