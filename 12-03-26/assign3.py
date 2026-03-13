
from selenium import webdriver
import time

browsers = ["chrome", "edge", "firefox"]

for b in browsers:

    if b == "chrome":
        driver = webdriver.Chrome()
    elif b == "edge":
        driver = webdriver.Edge()
    else:
        driver = webdriver.Firefox()

    driver.get("https://github.com/sidhiBhagat/")

    print("Current URL:", driver.current_url)
    print("Title:", driver.title)
    print("Browser:", driver.name)

    time.sleep(2)
    driver.quit()