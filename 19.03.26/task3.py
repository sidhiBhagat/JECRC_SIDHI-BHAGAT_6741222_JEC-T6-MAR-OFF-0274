from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

# 1. navigate to amazon
# 2. search a product through send_keys
# BUT dont click on search or keys.enter
# 3. Wait for the suggestions to appear
# 4. Click on 4th suggestion
# 5. Click on Sort By and click on newest
# 6. Click on free shipping check box
# 7. wait for first product and return me the name=price
# (without using inner text)
driver.get("https://www.amazon.in/")
driver.maximize_window()
wait = WebDriverWait(driver, 10)
searching=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='twotabsearchtextbox']")))
searching.send_keys("laptop")
# sug=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='left-pane-results-container']/descendant::div[1]/following-sibling::div[5]")))
# sug=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='sac-suggestion-row-1']/following-sibling::div[5]")))
# sug.click()
suggestions = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "//div[@role='row']/following-sibling::div[3]")
))
suggestions[3].click()

sort=wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='s-result-sort-select']/descendant::option[5]")))
sort.click()
free_ship=wait.until(EC.visibility_of_element_located((By.XPATH, "//li[@id='p_n_free_shipping_eligible/205563695031']/descendant::div/descendant::i")))
free_ship.click()

title=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='puisg-row']/descendant::h2")))
print(title.text)
price=wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='a-price-whole']")))
print(price.text)

# driver.quit()