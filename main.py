from select import select
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
url = "https://accounts.lambdatest.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)
uname = driver.find_element("id","email")
uname.send_keys("shubhamr@lambdatest.com")
# driver.find_element()
# time.sleep(2)
pswd = driver.find_element("id","password")
pswd.send_keys("Gmail@123")
# time.sleep(2)
submit = driver.find_element("id","login-button")
submit.send_keys(Keys.ENTER)
time.sleep(5)

# driver.find_element("id",).click();
# driver.find_element("id","item__manage__team").click();
# driver.find_element("id","profile__")
driver.find_element(By.XPATH,"//*[@id='profile__dropdown__parent']").click()
driver.find_element(By.XPATH,"//*[@id='item__manage__team']").click()
driver.find_element(By.XPATH,"//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[1]").click()
# driver.find_element(By.XPATH,"//*[@id='app']/section/div/div/div[2]/div[2]/div[1]/div[2]/div/div[2]/div[2]").click()
driver.get("https://cgi-lib.berkeley.edu/ex/perl5/fup.html")
time.sleep(2)
upload=driver.find_element(By.XPATH,"/html/body/form/input[1]")
# upload=driver.find_element(By.XPATH,"//input[@type='file']").click()
upload.send_keys("C:\\Users\\rakeshs\\Downloads\\Invited Users.csv")
save=driver.find_element(By.XPATH,"/html/body/form/input[3]")
save.click()


print("hello")

# dropdown=select(driver.find_element(By.ID,"profile__dropdown__parent"))
# dropdown.select_by_index(2).click();

# driver.find_element(By.ID,"item__manage__team").click()


time.sleep(30)