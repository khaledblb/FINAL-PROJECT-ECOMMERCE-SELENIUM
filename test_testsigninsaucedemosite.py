from selenium.webdriver.common.by import By

def test_testsigninsaucedemosite(driver):
    driver.get("https://www.saucedemo.com/")
    userName = "standard_user"
    password = "secret_sauce"

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(userName)
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    loginWarning = driver.find_element(By.CSS_SELECTOR, "#login_button_container > div > form > div.error-message-container.error")

    assert loginWarning.is_displayed() == False


def test_testsigninsaucedemositewrongdetails(driver) :
    driver.get("https://www.saucedemo.com/")
    userName = "standard_user123"
    password = "secret_sauce000"

    driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys(userName)
    driver.implicitly_wait(5)
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR,"#login-button").click()

    loginWarning = driver.find_element(By.CSS_SELECTOR,
                                       "#login_button_container > div > form > div.error-message-container.error")

    assert loginWarning.is_displayed() == True

def test_testsigninsaucedemositeblankdetails(driver) :
  driver.get("https://www.saucedemo.com/")
  userName = ""
  password = ""

  driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys(userName)
  driver.implicitly_wait(5)
  driver.find_element(By.CSS_SELECTOR,"#password").send_keys(password)
  driver.implicitly_wait(10)
  driver.find_element(By.CSS_SELECTOR,"#login-button").click()

  loginWarning = driver.find_element(By.CSS_SELECTOR,
                                     "#login_button_container > div > form > div.error-message-container.error")

  assert loginWarning.is_displayed() == True
