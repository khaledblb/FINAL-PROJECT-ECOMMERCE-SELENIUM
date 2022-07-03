# Generated by Selenium IDE
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def test_testaddproducttocart(driver):
      driver.get("https://automationexercise.com/")
      driver.find_element(By.LINK_TEXT, "Signup / Login").click()
      time.sleep(3)
      driver.find_element(By.NAME, "email").click()
      driver.find_element(By.NAME, "email").send_keys("khaledblb@gmaill.com")
      driver.find_element(By.NAME, "password").click()
      element = driver.find_element(By.NAME, "password")
      actions = ActionChains(driver)
      actions.double_click(element).perform()
      driver.find_element(By.NAME, "password").send_keys("khaledd1")
      driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
      driver.implicitly_wait(10)
      time.sleep(10)

      driver.find_element(By.CSS_SELECTOR, "body > section:nth-child(3) > div > div > div.col-sm-9.padding-right > div > div:nth-child(3) > div > div.single-products > div.productinfo.text-center > a").click()
      time.sleep(10)

      driver.find_element(By.CSS_SELECTOR, ".close-modal").click()
      driver.implicitly_wait(10)
      driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .fa-shopping-cart").click()
      time.sleep(10)
      itemList = driver.find_element(By.XPATH, '//*[@id="cart_info_table"]/tbody/*')
      assert itemList.text != ''

      #TODO:assertion_the_exact_item_in_cart

def test_testbuyproductfeature(driver):
    driver.get("https://automationexercise.com/")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(10)
    driver.find_element(By.NAME, "email").click()
    driver.find_element(By.NAME, "email").send_keys("khaledblb@gmaill.com")
    driver.find_element(By.NAME, "password").click()
    driver.find_element(By.NAME, "password").send_keys("khaledd1")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR,"#header > div > div > div > div.col-sm-8 > div > ul > li:nth-child(3) > a > i").click()
    driver.implicitly_wait(20)
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a').click()
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="cart_items"]/div/div[7]/a').click()
    time.sleep(5)
    creditCardNumber = "3566000020000410"
    cvcNumber = "123"
    expDate = "02"
    expYear = "2023"

    driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(2) > div > input").send_keys("Adam Adams!")
    driver.find_element(By.XPATH, '//*[@id="payment-form"]/div[2]/div/input').send_keys(creditCardNumber)
    driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(4) > div.col-sm-4.form-group.cvc > input").send_keys(cvcNumber)
    driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(4) > div:nth-child(2) > input").send_keys(expDate)
    driver.find_element(By.CSS_SELECTOR, "#payment-form > div:nth-child(4) > div:nth-child(3) > input").send_keys(expYear)
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, "#submit").click()
    # driver.find_element(By.LINK_TEXT, "Proceed To Checkout").click()
    # driver.find_element(By.LINK_TEXT, "Place Order").click()
    time.sleep(10)
    buyingConfirmation = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > h2 > b")

    htmlEle = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div > h2 > b")

    assert "ORDER PLACED!" == htmlEle.text

def test_testpricereflectingafteraddproducttocart(driver):
    driver.get("https://automationexercise.com/")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(By.NAME, "email").click()
    driver.find_element(By.NAME, "email").send_keys("khaledblb@gmaill.com")
    driver.find_element(By.NAME, "password").click()
    element = driver.find_element(By.NAME, "password")
    actions = ActionChains(driver)
    actions.double_click(element).perform()
    driver.find_element(By.NAME, "password").send_keys("khaledd1")
    driver.find_element(By.NAME, "password").send_keys(Keys.ENTER)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "body > section:nth-child(3) > div > div > div.col-sm-9.padding-right > div.features_items > div:nth-child(3) > div > div.single-products > div.productinfo.text-center > a").click()
    time.sleep(10)
    price = 500
    driver.find_element(By.CSS_SELECTOR, "#cartModal > div > div > div.modal-body > p:nth-child(2) > a > u").click()
    driver.implicitly_wait(10)
    totalAmount = driver.find_element(By.XPATH, '//*[@id="product-1"]/td[5]/p').text


    assert float(totalAmount[4:]) == price
