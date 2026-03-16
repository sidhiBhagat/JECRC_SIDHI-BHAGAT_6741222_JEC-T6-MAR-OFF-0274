from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=opts)

driver.get("https://www.flipkart.com/")
driver.maximize_window()

prod = driver.find_element(By.XPATH, "//input[@title='Search for Products, Brands and More']")
prod.send_keys("shoes", Keys.ENTER)

sleep(2)

c = driver.find_elements(By.XPATH, "//input[@class='ybaCDx']")

count = 0

for i in c:
    i.click()
    label = i.find_element(By.XPATH, "following-sibling::div").text
    print(label)

    sleep(2)

    count += 1

    if count == 2:
        break

driver.quit()