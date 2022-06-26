import time
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

userNames = {'test1','2test','123','00011a','a11233','%$#test',' '}
passwords = {'Password123','1assword','3f20','@#!!dwqod','p123321',')@!SSword',' '}
emails = {'email@dom.com', '1ema!l@d0m.com', 'emaildom.com', 'email', ' '}
pNumbers = {'123‑456‑7890','000-000-0000','111-111-1111','ABC-DEF-AAAA','#########',' '}

def test_testsignup(driver):
    # time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR,".v-p-right-xxs:nth-child(2)")
    # time.sleep(1)
    actions = ActionChains(driver)
    time.sleep(1)
    actions.move_to_element(element).perform()
    time.sleep(1)
    # driver.find_element(By.XPATH,'//*[@id="shop-account-menu-064dc78b-67e6-4ead-8ef2-32adac713deb"]')
    driver.find_element(By.CSS_SELECTOR,".v-p-right-xxs:nth-child(2)").click()
    time.sleep(1)
    element = driver.find_element(By.CSS_SELECTOR,"body")
    time.sleep(1)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,".c-button-secondary").click()
    time.sleep(10)
    driver.find_element(By.ID,"#firstName").click()
    time.sleep(3)
    driver.find_element(By.ID,"firstName").send_keys("Khaled")
    driver.find_element(By.ID,"lastName").send_keys("Blbesie")
    driver.find_element(By.ID,"email").send_keys("Test@gmail.com")
    driver.find_element(By.ID,"fld-p1").send_keys("Kh123123!@##")
    driver.find_element(By.ID,"reenterPassword").send_keys("Kh123123!@##")
    time.sleep(1)
    driver.find_element(By.ID,"phone").click()
    time.sleep(1)
    driver.find_element(By.ID,"phone").send_keys("646‑348‑4474")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,".c-button-secondary").click()
    alertAlreadyUserRegisterd = driver.find_element(By.CSS_SELECTOR, "body > div.cia-app-container > div > section >"
                                 " main > div.cia-wrapper__main > div.cia-content.js-cia-content > div > div > div >"
                                 " div.c-alert.c-alert-v2.flex.rounded-100.v-bg-pure-white.w-full.border-solid.body-copy-lg.c-alert-error.border-error.cia-alert")
    assert (alertAlreadyUserRegisterd.is_displayed() == True)

@pytest.mark.slow
def test_testsignupwithblankmandatoryfield(driver):
    time.sleep(3)
    element = driver.find_element(By.CSS_SELECTOR,".v-p-right-xxs:nth-child(2)")
    time.sleep(1)
    actions = ActionChains(driver)
    time.sleep(1)
    actions.move_to_element(element).perform()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,".v-p-right-xxs:nth-child(2)").click()
    time.sleep(1)
    element = driver.find_element(By.CSS_SELECTOR,"body")
    time.sleep(1)
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,"Create Account").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR,".c-button-secondary").click()
    element = driver.find_element(By.CSS_SELECTOR,".c-button-secondary")
    time.sleep(1)
    actions = ActionChains(driver)
    time.sleep(1)
    actions.move_to_element(element).perform()
    time.sleep(1)
    element = driver.find_element(By.CSS_SELECTOR,"body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    validationElement = driver.find_element(By.CSS_SELECTOR, "#email-text")
    assert validationElement.is_displayed()

@pytest.mark.parametrize('userName', userNames)
def test_testsignupwithincorrectvalues(driver, userName):
    time.sleep(3)
    driver.set_window_size(1440,900)
    driver.find_element(By.CSS_SELECTOR,".v-p-right-xxs:nth-child(2)").click()
    time.sleep(1)
    driver.find_element(By.LINK_TEXT,"Create Account").click()
    time.sleep(1)
    driver.find_element(By.ID,"firstName").click()
    time.sleep(1)
    driver.find_element(By.ID,"firstName").send_keys(userName)
    element = driver.find_element(By.ID,"lastName")
    actions = ActionChains(driver)
    time.sleep(1)
    actions.move_to_element(element).click_and_hold().perform()
    time.sleep(1)
    element = driver.find_element(By.CSS_SELECTOR,".cia-form")
    time.sleep(1)
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()

    driver.find_element(By.CSS_SELECTOR,".cia-form").click()
    time.sleep(1)

    driver.find_element(By.ID,"lastName").send_keys("22")
    time.sleep(1)
    element = driver.find_element(By.ID,"email")
    time.sleep(1)

    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = driver.find_element(By.CSS_SELECTOR,".cia-form")
    actions = ActionChains(driver)
    time.sleep(1)

    actions.move_to_element(element).release().perform()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR,".cia-form").click()
    driver.find_element(By.ID,"email").send_keys("00")
    element = driver.find_element(By.ID,"fld-p1")
    actions = ActionChains(driver)
    time.sleep(1)

    actions.move_to_element(element).click_and_hold().perform()
    time.sleep(1)

    element = driver.find_element(By.CSS_SELECTOR,".c-overlay-wrapper:nth-child(3) > .overlayTrigger")
    actions = ActionChains(driver)
    time.sleep(1)
    actions.move_to_element(element).release().perform()
    driver.find_element(By.CSS_SELECTOR,".c-overlay-wrapper:nth-child(3) > .overlayTrigger").click()

    driver.find_element(By.ID,"fld-p1").click()
    time.sleep(1)

    driver.find_element(By.ID,"fld-p1").click()
    time.sleep(1)

    driver.find_element(By.ID,"fld-p1").send_keys("231")
    time.sleep(1)

    driver.find_element(By.ID,"reenterPassword").click()
    driver.find_element(By.ID,"reenterPassword").send_keys("123")
    driver.find_element(By.ID,"phone").click()
    element = driver.find_element(By.CSS_SELECTOR,".c-button-secondary")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR,"body")
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    element = driver.find_element(By.CSS_SELECTOR,".c-button-secondary")
    actions = ActionChains(driver)
    actions.move_to_element(element).click_and_hold().perform()
    time.sleep(1)

    element = driver.find_element(By.CSS_SELECTOR,".cia-form")
    actions = ActionChains(driver)
    actions.move_to_element(element).release().perform()
    time.sleep(1)
    fNameValidation = driver.find_element(By.CSS_SELECTOR,"#firstName-text")
    lNameValidation = driver.find_element(By.CSS_SELECTOR,"##lastName-text")
    emaiValidation = driver.find_element(By.CSS_SELECTOR,"#email-text")
    pNumberValidation = driver.find_element(By.CSS_SELECTOR,"#phone-text")
    driver.find_element(By.CSS_SELECTOR,".cia-form").click()
    time.sleep(5)
    assert (fNameValidation.is_displayed() &lNameValidation.is_displayed() &emaiValidation.is_displayed() &pNumberValidation.is_displayed())