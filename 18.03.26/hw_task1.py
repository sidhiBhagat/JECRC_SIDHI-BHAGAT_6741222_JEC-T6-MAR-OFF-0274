# ### Link Text & Partial Link Text
#
#
# 1. Go to https://the-internet.herokuapp.com/
# 2. Find the "Checkboxes" link using LINK_TEXT
# 3. Find the "Drag and Drop" link using PARTIAL_LINK_TEXT
# 4. Find how many <li> (list item) elements are on the page using find_elements and TAG_NAME. Print the count.
# 5. Navigate to https://the-internet.herokuapp.com/tables
# 6. Write an XPath to find the "Web Site" (td) for the person with email "jdoe@hotmail.com" in table 1 (Hint: Use text() and ancestor/following sibling or preceding-sibling).
# 7. Write an XPath to find the Delete link (a) for the person with Last Name "Bach" in table 1.
# 8. Write an XPath to find the second table `(<table>)` on the page using indexing.
# 9. Write an XPath to find the cell containing "$100.00" in table 2. Find its parent <tr> element.

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/')
sleep(2)
check=driver.find_element(By.LINK_TEXT,"Checkboxes")
print(check.text)

dd=driver.find_element(By.PARTIAL_LINK_TEXT,"Drop")
print(dd.text)
listt=driver.find_elements(By.TAG_NAME,"li")
print(len(listt))
tab=driver.find_element(By.LINK_TEXT,"Sortable Data Tables")
tab.click()
website = driver.find_element(
    By.XPATH,
    "//td[text()='jdoe@hotmail.com']/following-sibling::td[1]"
)
print("Website (jdoe):", website.text)

del_link = driver.find_element(By.XPATH,"//td[text()='Bach']/following-sibling::td/a[text()='delete']")
print("Delete link (Bach):", del_link.text)
sleep(2)
sec_table = driver.find_element(By.XPATH, "//table[@id='table2']")
print("Second table found")

cell = driver.find_element(By.XPATH, "//table[@id='table2']/tbody/tr/td[text()='$100.00']")
parent = cell.find_element(By.XPATH, "//table[@id='table2']/tbody/tr[td[text()='$100.00']]")

print("Cell value:", cell.text)
print(parent.text)
sleep(2)
driver.quit()