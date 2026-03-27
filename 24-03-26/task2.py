from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/alerts")

wait = WebDriverWait(driver, 10)
# alert_btn = driver.find_element(By.ID, "alertButton")
# alert_btn.click()
# alert = wait.until(EC.alert_is_present())
# alert.accept()
# sleep(2)
#
# timer_btn = driver.find_element(By.ID, "timerAlertButton")
# timer_btn.click()
# alert = wait.until(EC.alert_is_present())
# alert.accept()
# sleep(2)
#
# confirm_btn = driver.find_element(By.ID, "confirmButton")
# confirm_btn.click()
# alert = wait.until(EC.alert_is_present())
# print("Confirm Alert text:", alert.text)
# alert.accept()
# result = driver.find_element(By.ID, "confirmResult").text
# print("Result:", result)
# assert "Ok" in result, "Confirm alert OK validation failed"

prompt_btn = driver.find_element(By.ID, "promtButton")
prompt_btn.click()
alert = wait.until(EC.alert_is_present())
print("Prompt Alert text:", alert.text)
alert.send_keys("Shruti")
alert.accept()
result = driver.find_element(By.ID, "promptResult").text
print("Result:", result)
assert "Shruti" in result, "Prompt alert validation failed"

driver.quit()