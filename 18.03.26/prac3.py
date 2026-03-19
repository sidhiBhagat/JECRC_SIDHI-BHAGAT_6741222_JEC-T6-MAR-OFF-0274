from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/upload")
# driver.maximize_window()
# upload = driver.find_element(By.ID, 'file-upload')
# upload.send_keys(R"C:\Users\siddh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-18 113611.png")
#
# submit = driver.find_element(By.ID, 'file-submit')
# submit.click()
# sleep(5)
driver.get("https://the-internet.herokuapp.com/download")
driver.maximize_window()
driver.find_element(By.XPATH,"//a[text()='Screenshot 2025-12-24 164603.png']").click()
sleep(2)
print('downloaded')
driver.quit()
