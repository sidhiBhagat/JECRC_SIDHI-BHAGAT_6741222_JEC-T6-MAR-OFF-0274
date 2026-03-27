from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Navigate to URL
driver.get("https://codepen.io/gdw96/pen/jOypoYL")
sleep(3)

# ⚠️ CodePen runs inside an iframe → switch required
iframe = driver.find_element(By.XPATH, "//iframe[contains(@id,'result')]")
driver.switch_to.frame(iframe)

username = driver.find_element(By.ID, "username")
username.clear()
username.send_keys("testuser")
password = driver.find_element(By.ID, "password")
password.clear()
password.send_keys("mypassword123")
sleep(3)
eye_icon = driver.find_element(By.XPATH, "//i[contains(@class,'fa-eye')]")

actions = ActionChains(driver)
actions.click_and_hold(eye_icon).perform()
#
sleep(2)

actions.release().perform()
register_btn = driver.find_element(By.XPATH, "//input[@class='submit']")
register_btn.click()
sleep(5)
driver.refresh()

page_src = driver.page_source
assert "Registration" in page_src, "Registration text not found"
print("Successful Registration")

driver.quit()