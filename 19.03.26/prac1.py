from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

# driver.get("https://abc.com/")
# driver.maximize_window()
#
# driver.implicitly_wait(5)
#
# ele = driver.find_element(By.XPATH, "(//a[@class='AnchorLink']/parent::li/descendant::img)[1]")
# print(ele.get_attribute("src"))

wait_obj = WebDriverWait(driver, timeout=10, poll_frequency=200)
submit_btn = wait_obj.until(EC.element_to_be_clickable(By.ID, 'button'))
submit_btn.click()
driver.quit()