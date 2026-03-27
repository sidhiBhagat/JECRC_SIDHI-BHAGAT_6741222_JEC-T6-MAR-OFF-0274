from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demoqa.com/browser-windows")

wait = WebDriverWait(driver, 10)

main = driver.current_window_handle

#tab
driver.find_element(By.ID, "tabButton").click()
wait.until(EC.number_of_windows_to_be(2))
for w in driver.window_handles:
    if w != main:
        driver.switch_to.window(w)
        break
text = wait.until(EC.presence_of_element_located((By.ID, "sampleHeading"))).text
print("New Tab:", text)
assert text == "This is a sample page"

driver.close()
driver.switch_to.window(main)

#window

driver.find_element(By.ID, "windowButton").click()
wait.until(EC.number_of_windows_to_be(2))
for w in driver.window_handles:
    if w != main:
        driver.switch_to.window(w)
        break

text = wait.until(EC.presence_of_element_located((By.ID, "sampleHeading"))).text
print("New Window:", text)
assert text == "This is a sample page", "New Window validation failed"

driver.close()
driver.switch_to.window(main)


# driver.find_element(By.ID, "messageWindowButton").click()
# wait.until(EC.number_of_windows_to_be(2))
#
# b_text = driver.find_element(By.TAG_NAME, "body").text
# print("Message Window:", b_text)
#
# assert "Knowledge increases" in b_text, "validation failed"
#
# driver.close()
# driver.switch_to.window(main)

driver.quit()