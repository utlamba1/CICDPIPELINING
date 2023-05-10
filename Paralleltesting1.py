import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
username = "utkarshs"
access_key = "URepF67q3TohDB8lP8SrqlWGOPVyXbV2NBcx2nESEJj2S6hKC1"
grid_Url = "hub.lambdatest.com/wd/hub"


options = webdriver.ChromeOptions()
options.browser_version = ""
options.platform_name = "Windows 11"
lt_options = {}
lt_options["username"] = "utkarshs"
lt_options["accessKey"] = "URepF67q3TohDB8lP8SrqlWGOPVyXbV2NBcx2nESEJj2S6hKC1"
lt_options["project"] = "Parallel"
lt_options["selenium_version"] = "4.0.0"
lt_options["w3c"] = True
options.set_capability('LT:Options', lt_options)


options2 = webdriver.EdgeOptions()
options2.browser_version = ""
options2.platform_name = "Windows 11"
# lt_options = {}
# lt_options["username"] = "utkarshs"
# lt_options["accessKey"] = "URepF67q3TohDB8lP8SrqlWGOPVyXbV2NBcx2nESEJj2S6hKC1"
lt_options["project"] = "Parallel"
lt_options["selenium_version"] = "4.0.0"
lt_options["w3c"] = True
options2.set_capability('LT:Options', lt_options)

url = "https://"+username+":"+access_key+"@"+grid_Url
driver = webdriver.Remote(
    command_executor=url,
    options=options
    )
driver1 = webdriver.Remote(
    command_executor=url,
    options=options2
    )
driver.get("https://accounts.lambdatest.com/")
# driver.get("https://accounts.lambdatest.com/")
u_name = driver.find_element("id", "email")
u_name.send_keys("utkarshs@lambdatest.com")
# uname.send_keys("gauravp@lambdatest.com")
# for  password
p_word = driver.find_element("id", "password")
p_word.send_keys("Utkarsh@12345678")
# for login
login = driver.find_element("id", "login-button")
login.send_keys(Keys.ENTER)
time.sleep(10)
# for dropdown
print("Test completed")
time.sleep(10)
driver.quit()












