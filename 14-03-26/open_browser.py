from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("https://www.amazon.in/")
driver.get('https://testautomationpractice.blogspot.com/')
sleep(3)
# driver.get("https://www.cricbuzz.com/")
# sleep(3)
# driver.get("https://www.myntra.com/ ")
# sleep(3)

# x=driver.find_element(By.XPATH, "//span[text()='All']/ancestor::div[@id='nav-main']")
# print(x)
#
# y=driver.find_element(By.XPATH, "//div[@id='nav-main']/descendant::span[text()='All']")
# print(y)
#
# z=driver.find_element(By.XPATH,"//a[text()='Fresh']/ancestor::ul/following-sibling::li[1]")
# print(z)
# print("working fine.")

# //span[text()='All']/ancestor::div[@id='nav-main']
#//a[text()='Fresh']/ancestor::li/following-sibling::li[1]

# a=driver.find_element(By.LINK_TEXT, "Udemy Courses")
# print("Found the Element using link text.")
# b=driver.find_element(By.PARTIAL_LINK_TEXT, "Udemy")
# print("Found the Partial Link Text.")

# f_price=driver.find_element(By.XPATH,"//td[text()='Learn Java']/following-sibling::td[3]")
# print(f_price)

# sel=driver.find_element(By.XPATH,"//td[text()='Amod']/ancestor::tr[1]/preceding-sibling::tr[4]/td[3]")
pp=driver.find_elements(By.XPATH, "//td[text()='300']/preceding-sibling::td[3]")
print(len(pp))
for i in pp:
    print(i.text)


name
