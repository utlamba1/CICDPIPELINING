import time
from selenium import webdriver
import time
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
gridUrl = "https://hub.lambdatest.com/wd/hub"
def test_example_1():
    options1 = ChromeOptions()
    options1.browser_version = "112.0"
    options1.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = "utkarshs"
    lt_options["accessKey"] = "URepF67q3TohDB8lP8SrqlWGOPVyXbV2NBcx2nESEJj2S6hKC1"
    lt_options["visual"] = True
    lt_options["video"] = True
    lt_options["resolution"] = "1024x768"
    # lt_options["build"] = "Rishabh1st"
    # lt_options["project"] = "Untitled"
    lt_options["name"] = "1st"
    lt_options["console"] = "info"
    lt_options["selenium_version"] = "4.8.0"
    lt_options["w3c"] = True
    lt_options["plugin"] = "python-python"
    options1.set_capability('LT:Options', lt_options)
    driver = webdriver.Remote(command_executor=gridUrl, options=options1)
    driver.get("https://accounts.lambdatest.com/login")
    uname = driver.find_element(By.ID, "email")
    uname.send_keys("utkarshs@lambdatest.com")
    time.sleep(1)
    passs = driver.find_element(By.ID, "password")
    passs.send_keys("Utkarsh@12345678")
    time.sleep(1)
    login = driver.find_element(By.ID, "login-button")
    login.send_keys(Keys.ENTER)
    time.sleep(1)
def test_example_2():
    options2 = EdgeOptions()
    options2.browser_version = "111.0"
    options2.platform_name = "Windows 11"
    lt_options = {}
    lt_options["username"] = "utkarshs"
    lt_options["accessKey"] = "URepF67q3TohDB8lP8SrqlWGOPVyXbV2NBcx2nESEJj2S6hKC1"
    lt_options["visual"] = True
    lt_options["video"] = True
    lt_options["resolution"] = "1024x768"
    # lt_options["build"] = "Rishabh"
    # lt_options["project"] = "Untitled"
    lt_options["name"] = "2nd"
    lt_options["console"] = "info"
    lt_options["selenium_version"] = "4.8.0"
    lt_options["driver_version"] = "111.0"
    lt_options["w3c"] = True
    lt_options["plugin"] = "python-python"
    options2.set_capability('LT:Options', lt_options)
    driver = webdriver.Remote(command_executor=gridUrl, options=options2)
    driver.get("https://accounts.lambdatest.com/login")
    uname = driver.find_element(By.ID, "email")
    uname.send_keys("utkarshs@lambdatest.com")
    time.sleep(1)
    passs = driver.find_element(By.ID, "password")
    passs.send_keys("Utkarsh@12345678")
    time.sleep(1)
    login = driver.find_element(By.ID, "login-button")
    login.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.quit()












