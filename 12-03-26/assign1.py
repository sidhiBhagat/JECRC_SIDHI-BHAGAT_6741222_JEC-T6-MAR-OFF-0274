#different functions
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
sleep(5)
driver.get('https://www.geeksforgeeks.org/software-engineering/software-engineering-selenium-an-automation-tool/')
driver.maximize_window()
sleep(2)
driver.minimize_window()
sleep(2)
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(2)
driver.close()

