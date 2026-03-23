from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.iplt20.com/teams/rajasthan-royals')
driver.maximize_window()
sleep(3)
# IPL TEAM WEBsite
# scroll on to fav pic
# use for loop to go back up to 5-6 times

actions = ActionChains(driver)
sleep(3)
member=driver.find_element(By.XPATH, "//ul[@id='identifiercls2']//li[12]")
actions.scroll_to_element(member).perform()
sleep(3)
for i in range(5):
    actions.send_keys(Keys.PAGE_UP).perform()
    sleep(2)

# sleep()