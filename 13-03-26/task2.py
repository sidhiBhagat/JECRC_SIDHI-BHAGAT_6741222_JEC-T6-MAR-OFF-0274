# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
#
# opt = webdriver.ChromeOptions()
# opt.add_experimental_option("detach", True)
# driver=webdriver.Chrome(options=opt)
#
# driver.get("https://www.cricbuzz.com/")
# #locator
# driver.maximize_window()
# a=driver.find_element(By.ID,'main-header')
# print('ID LOCATOR:')
# print(a)
# b=driver.find_element(By.TAG_NAME,'footer')
# print("TAG NAME LOCATOR:")
# print(b)
# # c=driver.find_element(By.CLASS_NAME,'mt-6')
# # print("CLASS NAME LOCATOR:")
# # print(c)
# d=driver.find_element(By.CSS_SELECTOR,'.shadow rounded-md overflow-hidden')
# print(d)
# print("working fine..SABASHHH BETE!")
#
# sleep(2)
# driver.quit()
#

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
sleep(2)

# 1. Locate username field (XPath using Tag + name attribute)
username = driver.find_element(By.XPATH, "//input[@name='username']")
print(username)
# 2. Locate password field (XPath using Tag + id attribute)
password = driver.find_element(By.XPATH, "//input[@id='password']")
print(password)
# 3. Locate Login button (XPath using Tag + type attribute)
login_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
print(login_btn)
# 4. Locate "Elemental Selenium" link (XPath using exact text)
elemental_link = driver.find_element(By.XPATH, "//a[text()='Elemental Selenium']")
print(elemental_link)
# 5. Locate main heading "Login Page" (XPath using contains() with text)
heading = driver.find_element(By.XPATH, "//h2[contains(text(),'Login Page')]")
print(heading)

print("All elements located successfully")

sleep(5)
driver.quit()