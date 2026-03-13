from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
sleep(3)

# 2. Locate main search bar using ID with CSS Selector
search_bar = driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox")
print(search_bar)
# 3. Locate Amazon logo using CSS Selector
amazon_logo = driver.find_element(By.CSS_SELECTOR, "#nav-logo-sprites")
print(amazon_logo)
# 4. Locate Cart icon/link using CSS Selector
cart = driver.find_element(By.CSS_SELECTOR, "#nav-cart")
print(cart)
# 5. Locate Sign in link using descendant selector
signin = driver.find_element(By.CSS_SELECTOR, "#nav-tools a")
print(signin)
# 6. Locate all category links under "All"
categories = driver.find_elements(By.CSS_SELECTOR, "#nav-xshop a")

print("Total categories:", len(categories))

for c in categories:
    print(c.text)

sleep(5)
driver.quit()