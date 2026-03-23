from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.myntra.com/')
driver.maximize_window()
sleep(3)
wait=WebDriverWait(driver,10)
action=ActionChains(driver)
stree=wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Women']")))
sleep(3)
action.move_to_element(stree).perform()
sleep(3)
shirt=wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-reactid='223']")))
shirt.click()
sleep(2)
products=wait.until(EC.presence_of_element_located((By.XPATH,"//ul[@class='results-base']//li[16]")))
action.scroll_to_element(products).perform()

