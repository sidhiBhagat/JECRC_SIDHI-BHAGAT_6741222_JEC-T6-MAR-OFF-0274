
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

# opts=webdriver.ChromeOptions()
# opts.add_experimental_option('detach',True)

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.find_element(By.ID, "datepicker").send_keys("03/20/2026",Keys.ENTER)
sleep(2)
month="May"
date="2"

driver.find_element(By.ID, "txtDate").click()
sleep(3)
select=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
select.select_by_visible_text(month)
driver.find_element(By.XPATH, f'//a[text()={date}]/parent::td').click()
sleep(2)