#
# 1. Go to: https://demoqa.com/automation-practice-form
# 2. Handle every element in that form except the calendar
# `Note: Give fake names and emails`
# 3. Click on submit button
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
sleep(2)

f_name = driver.find_element(By.ID, "firstName")
f_name.send_keys("Simran")

l_name = driver.find_element(By.ID, "lastName")
l_name.send_keys("Ghosh")

email = driver.find_element(By.ID, "userEmail")
email.send_keys("sidhi123@gmail.com")

gender = driver.find_element(By.XPATH, "//label[text()='Female']")
gender.click()

mobile = driver.find_element(By.ID, "userNumber")
mobile.send_keys("9876543210")

subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Computer Science")
subjects.send_keys(Keys.ENTER)

sports = driver.find_element(By.XPATH, "//label[text()='Sports']")
reading = driver.find_element(By.XPATH, "//label[text()='Reading']")
sports.click()
reading.click()

address = driver.find_element(By.ID, "currentAddress")
address.send_keys("Jaipur, Rajasthan")

state=driver.find_element(By.ID,'react-select-3-input')
state.send_keys('Uttar Pradesh',Keys.ENTER)

city=driver.find_element(By.ID,'react-select-4-input')
city.send_keys('Lucknow',Keys.ENTER)

sleep(1)
submit_btn=driver.find_element(By.ID,'submit')
submit_btn.click()

print("Form submitted")

sleep(3)
driver.quit()



