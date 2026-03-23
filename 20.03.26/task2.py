
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)

driver.get(r"C:\Users\siddh\PycharmProjects\PythonProject\20.03.26\playlist.html")
driver.maximize_window()

song=driver.find_element(By.ID,"songs")
select=Select(song)
# opt=select.options
artist=driver.find_elements(By.XPATH,"//optgroup[@label='Dua Lipa']/descendant::option")
for a in artist:
    select.select_by_visible_text(a.text)
    print(a.text)
driver.find_element(By.XPATH, "//button[text()='Add to Playlist']").click()
sleep(2)
driver.quit()
