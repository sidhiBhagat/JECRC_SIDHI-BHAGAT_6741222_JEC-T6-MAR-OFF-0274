from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)

# opt.add_argument('--headless')

driver = webdriver.Chrome(options=opt)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
sleep(4)
# name=driver.find_element(By.ID,'name') #NoSuchElementException if not found
# phone=driver.find_element(By.ID,'phone')
# # nav_bar=driver.find_element(By.ID,'Navbar')
# radio_btn=driver.find_elements(By.CLASS_NAME,'form-check-input')
# inp=driver.find_elements(By.TAG_NAME,'input')
# print(name)
# print(phone)
# # print(nav_bar)
# print(len(radio_btn))
# print(len(inp))
# print('name and phone textfield found')
# print('navbar found')

# name=driver.find_element(By.CSS_SELECTOR, 'select[id="animals"]').text
# print('name is working fine')
# ani=driver.find_element(By.CSS_SELECTOR, '#animals ')
# print(ani)
# print("animal is working")
# ani = driver.find_element(By.CSS_SELECTOR,'a[href*="testautomationpractice"]')
# a=driver.find_element(By.XPATH, '//input[@placeholder="Enter EMail"]')
# b=driver.find_element(By.XPATH, '(//input[@class="form-control"])[1]')
# c=driver.find_element(By.XPATH, '(//input[@class="form-control"][2])')

x=driver.find_element(By.XPATH,'//a[text()="Home"]')
y=driver.find_element(By.XPATH,'//h2[text()="Tabs"]')
z=driver.find_element(By.XPATH,'//h1[contains(text(),"Automation Testing Practice")]')
print(x)
print(y)
print(z)
print('working fine')
sleep(2)
driver.quit()