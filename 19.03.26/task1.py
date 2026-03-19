from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v143.dom import get_attributes
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

driver.get("https://abc.com/")
driver.maximize_window()
# //figure[@class='Image aspect-ratio--parent tile__imagecontainer']/descendant::img
wait = WebDriverWait(driver, 10)
banner=wait.until(EC.presence_of_all_elements_located((By.XPATH, "//figure[@class='Image aspect-ratio--parent tile__imagecontainer']/descendant::img")))

for b in banner:
    print(b.get_attribute('src'))

driver.quit()