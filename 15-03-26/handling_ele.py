from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# name.clear()
# name.send_keys("Arjun")
sleep(2)
# email=driver.find_element(By.XPATH, "//input[@placeholder='Enter EMail']")
# email.send_keys("simmran@123.com")
# sleep(5)
# print(name.get_attribute("placeholder"))
# print(name.get_attribute("value"))
# driver.find_element(By.ID, "male").click()
# driver.find_element(By.XPATH, "//label[text()='Monday']/preceding-sibling::input").click()
# mon_txt=driver.find_element(By.XPATH,"//input[@id='monday']/following-sibling::label")
# print(mon_txt.text)
###############################

genders=driver.find_elements(By.XPATH,"//input[@name='gender']")
for i in genders:
    i.click()
    sleep(5)
driver.quit()

# from selenium.webdriver.common.keys import Keys

# opts = webdriver.ChromeOptions()
# opts.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=opts)
#
# # driver.get("https://www.amazon.in/")
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
# sleep(5)
# #
# # search = driver.find_element(By.ID, "twotabsearchtextbox")
# # search.clear()
# # search.send_keys("sandals")
# sleep(2)
#
# # search_opt = driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon.in']")
# # search_opt.clear()
# # search_opt.send_keys("samsung TV",Keys.ENTER)
# # search_in =driver.find_element(By.XPATH,"//input[@title='Search for Products, Brands and More']")
# # search_in.send_keys('mobile', Keys.ENTER)
#
#
# sleep(2)
# driver.quit()