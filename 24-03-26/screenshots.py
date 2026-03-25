import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

folder=os.path.join(os.getcwd(), "ss")
os.makedirs(folder, exist_ok=True)

driver=webdriver.Chrome()
driver.get("https://in.pinterest.com/")
driver.maximize_window()
sleep(2)

driver.save_screenshot(f"{folder}/full_pg.png")
sleep(3)

ele=driver.find_element(By.XPATH, '//img[contains(@alt, "Photo of a woman in a cherry-patterned")]')
action=ActionChains(driver)
action.scroll_to_element(ele).perform()
sleep(2)
ele.screenshot(f"{folder}/nature.png")