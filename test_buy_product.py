import time
import pytest
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By

def test_testaddproducttocart(driver):
    driver.find_element(By.ID,"gh-search-input").send_keys("LG - 55” Class UP7000 Series LED 4K UHD Smart webOS TV")
    driver.find_element(By.ID,"gh-search-input").send_keys(Keys.ENTER)
    time.sleep(10)
    res = driver.find_element(By.LINK_TEXT,"LG - 55” Class UP7000 Series LED 4K UHD Smart webOS TV")
    assert res.is_displayed()
    # driver.find_element(By.ID,"gh-search-input").send_keys("iphone 7")
    # driver.implicitly_wait(10)
    # driver.find_element(By.ID,"gh-search-input").send_keys(Keys.ENTER)
    # driver.implicitly_wait(10)
    #
    # driver.find_element(By.LINK_TEXT, "iphone 7").click()

    # driver.find_element(By.ID,"gh-search-input").send_keys(Keys.ENTER)
    # driver.implicitly_wait(10)
    # driver.find_element(By.CSS_SELECTOR,".shop-sku-list-item:nth-child(2).product-image").click()
    # driver.execute_script("window.scrollTo(0,134)")
    # driver.execute_script("window.scrollTo(0,316)")
    # driver.execute_script("window.scrollTo(0,522)")
    # driver.find_element(By.CSS_SELECTOR,".c-button-primary").click()
    # element = driver.find_element(By.LINK_TEXT,"Go to Cart")
    # actions = ActionChains(driver)
    # actions.move_to_element(element).perform()
    # driver.find_element(By.LINK_TEXT,"Go to Cart").click()