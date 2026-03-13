from selenium import webdriver
from time import sleep

for i in range(3):
    if i==1:
        driver = webdriver.Chrome()
        driver.get("https://supertails.com/")
        driver.maximize_window()
        sleep(4)
        driver.close()
    elif i==2:
        driver = webdriver.Edge()
        driver.get("https://www.geeksforgeeks.org/")
        driver.maximize_window()
        sleep(4)
        driver.close()
    else:
        driver = webdriver.Firefox()
        driver.get("https://github.com/sidhiBhagat/")
        driver.maximize_window()
        sleep(4)
        driver.close()



