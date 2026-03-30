from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()

wait = WebDriverWait(driver, 15)

# 1. Verify homepage title & URL
# assert "Amazon" in driver.title
assert "amazon.in" in driver.current_url
print("Homepage verified ✅")

# 2. Search for "Headphones"
search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
search_box.send_keys("Headphones")
search_box.send_keys(Keys.ENTER)

driver.find_element(By.XPATH,"//span[text()='boAt']/preceding-sibling::div").click()
sleep(3)
driver.find_element(By.XPATH,"//div[@id='priceRefinements']//ul//li[1]").click()

product = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@role='listitem']/descendant::h2/span")))
product_name = product.text
print("Selected Product:", product_name)

product.click()

driver.switch_to.window(driver.window_handles[1])

title = wait.until(EC.presence_of_element_located((By.ID, "productTitle"))).text

price = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@class='a-price-whole']"))).text
print("Product Price:", price)

# 8. Add to cart
add_to_cart = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-button")))
driver.execute_script("arguments[0].scrollIntoView();", add_to_cart)
add_to_cart.click()
warranty = wait.until(EC.presence_of_element_located((
    By.XPATH, "//span[contains(text(),'No thanks')]"
)))
driver.execute_script("arguments[0].click();", warranty)

wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class,'attach-accessory-pane')]")))

# Click cart (use JS to avoid overlay issues)
# cart_btn = wait.until(EC.presence_of_element_located((By.ID, "nav-cart")))
# driver.execute_script("arguments[0].click();", cart_btn)


cart_product = wait.until(EC.presence_of_element_located((
    By.XPATH, "//span[@class='a-truncate-cut']"
))).text

assert product_name in wait.until(EC.presence_of_element_located(
    (By.XPATH,'//span[@class="a-truncate-cut"]/ancestor::ul'
              ''))
).get_attribute('textContent'), 'Wrong Product'

assert price in wait.until(EC.presence_of_element_located(
    (By.XPATH,'//div[@class="sc-badge-price sc-apex-cart-price"]/descendant::span[@class="a-offscreen"]'))
).text, 'Wrong product'

print("Product successfully added to cart")

# Close browser
driver.quit()