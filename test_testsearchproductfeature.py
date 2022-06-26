import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_testsearchproductfeature(driver):
    driver.find_element(By.ID, "gh-search-input").send_keys("LG - 55” Class UP7000 Series LED 4K UHD Smart webOS TV")
    driver.find_element(By.ID, "gh-search-input").send_keys(Keys.ENTER)
    time.sleep(10)
    res = driver.find_element(By.LINK_TEXT, "LG - 55” Class UP7000 Series LED 4K UHD Smart webOS TV")
    assert res.is_displayed()
