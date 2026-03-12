from selenium import webdriver


opt=webdriver.ChromeOptions()
opt.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=opt)

driver.get("https://www.amazon.in/")
print(f'Current_URL: {driver.current_url}')
print(f'Title: {driver.title}')
print(f'Author: {driver.name}')
# driver.back()
# driver.forward()
# driver.refresh()
# driver.close()

#use of different functi
# for loop different web browser
# for loop use krke different url