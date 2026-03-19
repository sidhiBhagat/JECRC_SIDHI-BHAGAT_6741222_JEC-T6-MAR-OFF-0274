
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.lenskart.com/")
driver.maximize_window()
eye=driver.find_element(By.XPATH,"//a[text()='EYEGLASSES']")
eye.click()
sleep(2)
s_dd=driver.find_element(By.ID, "sortByDropdown")
dd=Select(s_dd)
dd.select_by_value('high_price')
sleep(2)
section=driver.find_element(By.XPATH, "//div[@class='sc-bf32d8a7-0 gOVKHN']/descendant::div/p")
print(section.text)
sleep(5)
driver.quit()

