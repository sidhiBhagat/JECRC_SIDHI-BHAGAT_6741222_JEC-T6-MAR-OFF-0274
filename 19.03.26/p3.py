from time import sleep
from tkinter.tix import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=opt)

# driver.get("https://demoqa.com/dynamic-properties")
# driver.maximize_window()

# wait = WebDriverWait(driver, 6)
#
# enable_before=driver.find_element(By.ID, 'enableAfter')
# print(enable_before.is_enabled())
#
# enable_btn=wait.until(EC.element_to_be_clickable((By.ID, 'enableAfter')))
# if enable_btn.is_enabled():
#     enable_btn.click()
#     print(enable_btn.text)
#
# vis_ele=wait.until(EC.visibility_of_element_located((By.ID, 'visibleAfter')))
# vis_ele.click()
#
# driver.quit()

### fetch all the image  links from banners

driver.get("https://demo.mobiscroll.com/select/multiple-select")
driver.maximize_window()

multi_drop=driver.find_element(By.XPATH, '//select[@id="multiple-select-"]')
select=Select(multi_drop)
if select.is_multiple:
    select.select_by_value("1")
    select.select_by_index(2)
    select.select_by_visible_text("Movies, Music & Games")
sleep(3)
select.deselect_by_index(6)
select.deselect_all()
print(select.first_selected_option)
print(select.all_selected_options)
driver.quit()
