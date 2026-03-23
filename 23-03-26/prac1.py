from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome()
# driver.get('https://demoqa.com/droppable')
# driver.maximize_window()
# sleep(3)
# driver.implicitly_wait(10)

# action=ActionChains(driver)
# source=driver.find_element(By.ID,'draggable')
# dest=driver.find_element(By.ID,'droppable')
#
# action.drag_and_drop(source,dest).perform()
# sleep(2)
#
# assert 'Dropped!' == dest.text, 'Didnt dropped'
# print('Success')

############ 2nd task ###############


opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach',True)
driver=webdriver.Chrome(options=opt)
driver.get('https://demoqa.com/droppable')
driver.maximize_window()

wait=WebDriverWait(driver,10)
btn=wait.until(EC.element_to_be_clickable((By.ID, "droppableExample-tab-preventPropogation")))
btn.click()
action=ActionChains(driver)
sleep(5)
source=wait.until(EC.presence_of_element_located((By.ID, 'dragBox')))
d1=wait.until(EC.presence_of_element_located((By.ID, 'notGreedyDropBox')))
d2=wait.until(EC.presence_of_element_located((By.ID, 'notGreedyInnerDropBox')))
sleep(2)
action.drag_and_drop(source,d1).perform()
sleep(2)
action.drag_and_drop(source,d2).perform()
sleep(2)
assert 'Dropped!' in d1.text, 'not working'
print("Success")
assert 'Dropped!' in d2.text, "not working"
print("Success2")