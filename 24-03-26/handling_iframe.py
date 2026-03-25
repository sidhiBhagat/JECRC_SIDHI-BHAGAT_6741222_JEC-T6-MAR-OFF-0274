from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
sleep(3)
#single iframe

# iframe=driver.find_element(By.ID, 'singleframe')
# driver.switch_to.frame(iframe)
# sleep(3)
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys('Hello World')
# sleep(3)

#nested iframe

driver.find_element(By.XPATH, '//a[text()="Iframe with in an Iframe"]').click()

nes_frame=driver.find_element(By.XPATH, '//iframe[@src="MultipleFrames.html"]')
driver.switch_to.frame(nes_frame)

sin_frame=driver.find_element(By.XPATH, '//iframe[@src="SingleFrame.html"]')
driver.switch_to.frame(sin_frame)

driver.find_element(By.XPATH, '//input[@type="text"]').send_keys('Hello World')
sleep(3)

# driver.switch_to.parent_frame()
# driver.switch_to.default_content()

