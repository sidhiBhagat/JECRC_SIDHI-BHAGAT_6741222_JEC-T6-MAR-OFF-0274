from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
# driver.get('https://the-internet.herokuapp.com/drag_and_drop')
# driver.maximize_window()
# sleep(3)
#
# actions = ActionChains(driver)
# original=driver.find_element(By.ID, "column-a")
# target=driver.find_element(By.ID, "column-b")
#
# actions.drag_and_drop(original,target).perform()
# sleep(5)
################# MOUSE HOVER ###########################

# driver = webdriver.Chrome()
# driver.get('https://supertails.com')
# driver.maximize_window()
# actions = ActionChains(driver)
#
# dog=driver.find_element(By.XPATH, '(//span[contains(text(),"Dogs")])[1]')
# sleep(2)
# actions.move_to_element(dog).perform()
# sleep(3)

############## Scroll ################
# driver = webdriver.Chrome()
# driver.get('https://supertails.com')
# driver.maximize_window()
# actions = ActionChains(driver)
#
# sleep(2)
# cat=driver.find_element(By.XPATH, "//div[@data-ganame='Breed 5']")
# actions.scroll_to_element(cat).perform()
# sleep(5)

############## Keyboard Actions ############

# driver = webdriver.Chrome()
# driver.get('https://supertails.com')
# driver.maximize_window()
# actions = ActionChains(driver)
# sleep(2)
# # actions.send_keys(Keys.PAGE_DOWN).perform()
# # sleep(2)
# # actions.send_keys(Keys.PAGE_UP).perform()
# # sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('a').perform()
# sleep(2)
# actions.key_up(Keys.CONTROL).perform()


# copying and pasting address

# driver = webdriver.Chrome()
# driver.get(r'C:\Users\siddh\PycharmProjects\PythonProject\23-03-26\adress.html')
# driver.maximize_window()
# actions = ActionChains(driver)
#
# present=driver.find_element(By.ID, 'presentAddress')
# permanent=driver.find_element(By.ID, 'permanentAddress')
# present.send_keys('JECRC, JAIPUR, RJ')
# sleep(2)
# present.click()
# actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# permanent.click()
# sleep(2)
# actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# sleep(5)


####### Password Visibility ###########

driver = webdriver.Chrome()
driver.get(r"C:\Users\siddh\PycharmProjects\PythonProject\23-03-26\index1.html")
driver.maximize_window()
actions = ActionChains(driver)

driver.find_element(By.ID, 'password').send_keys("sick")
sleep(3)
show_pwd=driver.find_element(By.ID, 'eyeBtn')
actions.click_and_hold(show_pwd).perform()
sleep(3)
actions.release().perform()
sleep(3)

# //IPL TEAM WEBsite
# scroll on to fav pic
# use for loop to go back up to 5-6 times