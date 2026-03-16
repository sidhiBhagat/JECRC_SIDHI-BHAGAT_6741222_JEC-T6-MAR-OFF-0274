from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
# Automate the login flow in OrangeHRM and verify that the user successfully reaches the dashboard:
#
# 1. Open the OrangeHRM demo website. `https://opensource-demo.orangehrmlive.com/`
# 2. Get and print the title of the page.
# 3. Locate the username input field and use clear() if needed.
# 4. Enter the username using send_keys().
# 5. Locate the password input field and enter the password using send_keys().
# 6. Submit the login form using either: click() on the Login button, or Keys.ENTER
# 7. After login, print the current URL.
# 8. Check if dashboard is present in that url using `in`
# 9. Print 'successful login'
#
# Test Data:
#
# Username: `Admin`
# Password: `admin123`

opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opts)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
sleep(2)

print("Title:", driver.title)
uname = driver.find_element(By.XPATH, "//input[@name='username']")
uname.clear()
uname.send_keys("Admin")

passwd = driver.find_element(By.XPATH, "//input[@type='password']")
passwd.send_keys("admin123")
passwd.send_keys(Keys.ENTER)
sleep(2)
current_url = driver.current_url
print("Current URL:", current_url)

if "dashboard" in current_url.lower():
    print("successful login")
driver.quit()
