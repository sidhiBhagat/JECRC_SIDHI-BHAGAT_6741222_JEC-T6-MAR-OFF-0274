from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
c_dd=driver.find_element(By.ID, "country")
dd=Select(c_dd)
dd.select_by_value("usa")
sleep(2)
dd.select_by_index(2)
sleep(2)
dd.select_by_visible_text(
    'Japan'
)
sleep(5)
driver.quit()