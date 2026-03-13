from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt = webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opt)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

fname = driver.find_element(By.ID, 'firstName')
print(fname)
print('first name id found')
gender = driver.find_element(By.CLASS_NAME, 'form-check-input')
print(gender)
print('gender classname found')
foot=driver.find_element(By.TAG_NAME, 'footer')
print(foot)
print('footer tag-name found')
sleep(2)
DOB = driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput')
print(DOB)
print('date of birth cssSelector found')

driver.quit()
