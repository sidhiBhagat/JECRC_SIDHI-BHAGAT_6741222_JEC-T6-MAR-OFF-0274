
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

opts=webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# driver.maximize_window()
#
# multi_drop=driver.find_element(By.ID,'colors')
# select=Select(multi_drop)
#
# if select.is_multiple:
#     select.select_by_value('blue')
#     select.select_by_index(5)
#     select.select_by_visible_text('Red')
#
# list_of_colors=[i.text for i in select.all_selected_options]
# print(list_of_colors)
# select.deselect_by_value('blue')
# list_of_colors_2=[i.text for i in select.all_selected_options]
# print(list_of_colors_2).click()

#############################################################################################################
driver.get(r"C:\Users\siddh\PycharmProjects\PythonProject\20.03.26\playlist.html")
driver.maximize_window()

songs=driver.find_element(By.ID,'songs')
select=Select(songs)
if select.is_multiple:
    select.select_by_index(4)
    select.select_by_visible_text('Shape of You')
    select.select_by_visible_text('Animals')

print([i.text for i in select.options])

print([i.text for i in select.all_selected_options])
driver.find_element(By.XPATH, "//button[text()='Add to Playlist']").click()
sleep(2)
driver.quit()


# there are songs having girl and love keywords add these songs which is containg love or girl into playlist