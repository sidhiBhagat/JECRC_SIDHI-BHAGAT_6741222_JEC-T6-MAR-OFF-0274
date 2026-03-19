from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

driver.get("https://qavbox.github.io/demo/signup/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)
f_name=wait.until(EC.visibility_of_element_located((By.ID, "username")))
f_name.send_keys("Simran")
email=wait.until(EC.visibility_of_element_located((By.ID, "email")))
email.send_keys("abc12@gmail.com")
tel=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='tel']")))
tel.send_keys("123-456-7890")
file_up=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='datafile']")))
file_up.send_keys(R"C:\Users\siddh\PycharmProjects\PythonProject\abc.png")
gender=wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@name='sgender']")))
dd=Select(gender)
dd.select_by_value("female")
yoe=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@value='two']")))
yoe.click()
skills=wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//label[@for='skills']/following-sibling::input")))
for s in skills:
    if s.get_attribute("value") == "automationtesting":
        s.click()

at=wait.until(EC.visibility_of_element_located((By.XPATH, "//select[@id='tools']/descendant::option[5]")))
at.click()
submit=wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='submit']")))
submit.click()
driver.quit()