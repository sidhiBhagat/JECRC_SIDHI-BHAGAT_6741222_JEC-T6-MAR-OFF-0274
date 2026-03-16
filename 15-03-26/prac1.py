from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()


# a=input("Enter your gender:")
# b=driver.find_element(By.ID, "male")
# g=driver.find_element(By.ID, "female")
#
# if a=="male":
#     b.click()
#
# else:
#     g.click()
#
# sleep(5)
# driver.quit()


#############################
#Toggle between checkbox
#############################

c = driver.find_elements(By.XPATH, "//input[@type='checkbox']")[:7]

for i in c:
    i.click()
    label = i.find_element(By.XPATH, "following-sibling::label").text
    print(label)
    sleep(2)
print("Unchecked sequence")
for i in c[::-1]:

    if i.is_selected():
        i.click()
        label = i.find_element(By.XPATH, "following-sibling::label").text
        print(label)
        sleep(1)

driver.quit()