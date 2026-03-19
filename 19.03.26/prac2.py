from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

driver.get("https://abc.com/")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

loading_circles= wait.until(EC.invisibility_of_element_located((By.ID, "preloader-animated_svg__svg3")))
title_abc=driver.find_element(By.XPATH, "//span[text()='ABC SHOWS, SPECIALS & MORE']")
assert 'SPECIALS' in title_abc.text, 'the text not present'
print(title_abc.text)
driver.quit()