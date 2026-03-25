from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()
sleep(3)
# parent_window = driver.current_window_handle
# driver.find_element(By.XPATH, "//a[text()='Click Here']").click()
# sleep(3)
#
# all_windows = driver.window_handles
# print(len(all_windows))
# driver.switch_to.window(all_windows[-1])
#
# # print(driver.find_element(By.CLASS_NAME, 'example').text)
# assert "New Window" in driver.find_element(By.CLASS_NAME, 'example').text
# print("Hurray")
# driver.close()
# driver.switch_to.window(parent_window)

#### Opening a website in a new window

driver.switch_to.new_window('window')
sleep(3)
driver.get('https://www.cricbuzz.com/')
sleep(3)

driver.switch_to.new_window('tab')
sleep(3)
driver.get('https://in.pinterest.com')