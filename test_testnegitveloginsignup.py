from telnetlib import EC
import pytest
import time
from selenium.webdriver.common.by import By

def test_testfailedsignupwithincorrectvaluesinfields(driver):
    driver.get("https://automationexercise.com/")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(5)
    driver.find_element(By.NAME, "name").click()
    driver.find_element(By.NAME, "name").send_keys("032094")
    driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(3)").send_keys("XYZ")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
    time.sleep(8)
    alert = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)").get_attribute("validationMessage")
    if driver.name == 'chrome':
        assert "Please include an '@' in the email address. 'XYZ' is missing an '@'." == alert
    elif driver.name == 'Firefox':
        assert "أدخِل رجاءً البريد الإلكتروني." == alert
    elif driver.name == 'Safari':
        assert "Enter an email address" == alert
    else:
        raise "Browser Not Supported!"

def test_testfailedsignupwithblankfields(driver):
    driver.get("https://automationexercise.com/")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()
    driver.implicitly_wait(10)

    alert = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=text]:nth-child(2)").get_attribute("validationMessage")

    if driver.name == 'chrome':
        assert "Please fill out this field." == alert
    elif driver.name == 'Safari':
        assert "Fill out this field" == alert
    elif driver.name == 'firefox':
        assert "رجاءً املأ هذا الحقل." == alert
    else:
        raise "Browser Not Supported!"

def test_testfailedsignupwithinvalidemail(driver):
    driver.get("https://automationexercise.com/")
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    time.sleep(17)
    # driver.find_element(By.NAME, "name").click()
    driver.find_element(By.XPATH, '//*[@id="form"]/div/div/div[3]/div/form/input[2]').click()
    driver.find_element(By.NAME, "name").send_keys("Khaled Blbesie")
    time.sleep(10)
    driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(3)").click()
    driver.find_element(By.CSS_SELECTOR, ".signup-form input:nth-child(3)").send_keys("asd@.com")
    driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(5)").click()

    alert = driver.find_element(By.CSS_SELECTOR, "#form > div > div > div:nth-child(3) > div > form > input[type=email]:nth-child(3)").get_attribute("validationMessage")

    if driver.name == 'chrome':
        assert "'.' is used at a wrong position in '.com'." == alert
    elif driver.name == 'Safari':
        assert 'Enter an email address' == alert
    elif driver.name == 'firefox':
        assert "رجاءً املأ هذا الحقل." == alert
    else:
        raise "Browser Not Supported!"