from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://in.pinterest.com/')
driver.maximize_window()
sleep(3)

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# sleep(5)
#
# driver.execute_script("window.scrollTo(0,0);")
# sleep(3)

#using scrollBy
driver.execute_script("window.scrollBy(0,500);")
sleep(5)
driver.execute_script("window.scrollBy(0,-200);")
sleep(5)

#scrolling to element
ele=driver.find_element(By.XPATH, '//img[contains(@alt, "Photo of a woman in a cherry-patterned")]')
driver.execute_script('arguments[0].scrollIntoView();', ele)
sleep(3)

driver.execute_script("arguments[0].click();", ele)
sleep(3)

click_ele=driver.find_element(By.XPATH, '(//div[text()="Join Pinterest"])[1]')

driver.execute_script("arguments[0].click();", click_ele)
sleep(3)
