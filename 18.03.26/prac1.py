from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://www.lenskart.com/lenskart-hustlr-la-e19034-black-eyeglasses.html")
driver.maximize_window()
sleep(1)

# eye=driver.find_element(By.ID, "lrd1")
# # print(eye.text)
#
# assert 'EYEGLASSES' == eye.text, 'didnt find'
# assert 'GLASSES' == eye.text, 'didnt find'
# print('success')
driver.find_element(By.XPATH, "//p[@title='Enter pincode']").click()
sleep(1)
# loc.click()
# loc.send_keys('302019')
# assert 'Enter pincode' == loc.text, 'didnt find'
# print('success')
driver.quit()
