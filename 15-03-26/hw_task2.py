# Automate interaction with radio buttons `https://demoqa.com/radio-button`
#
# 1. Open the radio button page.
# 2. Print the **title** of the page.
# 3. Locate the **"Yes" radio button**.
# 4. Click the radio button using `click()`.
# 5. Capture and print the **result message** using `.text`.
# 6. Use `get_attribute()` to fetch attributes like:
#    - `class`
#    - `id`
# 7. Print the **current URL**.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://demoqa.com/radio-button")
driver.maximize_window()
sleep(2)
print("Title:", driver.title)
yes_btn=driver.find_element(By.XPATH, "//input[@id='yesRadio']")
yes_btn.click()
sleep(2)
result = driver.find_element(By.CLASS_NAME, "text-success")
print("Result:", result.text)

print("CLass:", yes_btn.get_attribute("class"))
print("ID:", yes_btn.get_attribute("id"))

print("Current URL:", driver.current_url)

driver.quit()