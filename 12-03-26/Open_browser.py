# import driver
from selenium import webdriver
# from time import sleep

opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opt)
driver.get("https://supertails.com/")

# driver = webdriver.Chrome()
# sleep(5)

# driver = webdriver.FireFox()
# driver = webdriver.Edge()
# driver.get("https://supertails.com/")
# sleep(2)
driver.maximize_window()
# sleep(10)
driver.minimize_window()
# sleep(2)
driver.back()
# sleep(2)
driver.forward()
# sleep(2)
driver.refresh()
# sleep(2)
# driver.close()
# sleep(2)
# driver.quit()




