from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/javascript_alerts')
driver.maximize_window()
sleep(3)

#simple alerts
# driver.find_element(By.XPATH, '//button[@onclick="jsAlert()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.accept()
# sleep(3)

#confirmation alert
# driver.find_element(By.XPATH, '//button[@onclick="jsConfirm()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# # alert.accept()
# alert.dismiss()
# sleep(3)

# driver.find_element(By.XPATH, '//button[@onclick="jsPrompt()"]').click()
# sleep(3)
# alert = driver.switch_to.alert
# alert.send_keys("Batman")
# sleep(3)
# alert.accept()
# # alert.dismiss()
# sleep(3)

wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
alert=wait.until(EC.alert_is_present())
sleep(3)
alert.accept()
sleep(2)