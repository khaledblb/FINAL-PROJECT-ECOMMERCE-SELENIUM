import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import random
import string

def test_title(driver):
    driver.get("https://www.google.com/")
    title = driver.title
    driver.save_screenshot("testgooletitle.png")
    assert title == "Google"