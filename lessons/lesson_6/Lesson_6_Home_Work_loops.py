'''
Homework Assignment: Using Loops
Objective: Open the web application, log in, navigate to the "HR Administration" section via the side menu, and click on the "Add User" button. Once on the "Add User" page, your task is to retrieve and list all the names of input fields relevant to user information, such as employee name, username, etc. Use loops to iterate over elements and gather this information.

Steps:

Open the web application in a browser.
Log into the application with provided credentials.
From the side menu, navigate to the "HR Administration" section.
Click on the "Add User" button, usually represented by a big green button.
On the "Add User" form, identify all input fields related to user information.
Use a loop to iterate over these input fields and collect their names.
Print the list of field names you have collected.
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://portnov_administrator-trials712.orangehrmlive.com")

driver.find_element(By.CSS_SELECTOR, "input[id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[id='txtPassword']").send_keys("qTJn5@5APu")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)

sidebar_toggle = driver.find_element(By.CSS_SELECTOR, '#sidebar-toggle[class="circle"]')
sidebar_menu = driver.find_element(By.CSS_SELECTOR, '#left-menu[class="sidebar menu-visible"]')
if not sidebar_menu.is_displayed():
    sidebar_toggle.click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//a/span[text()="HR Administration"][1]').click()
else:
    driver.find_element(By.XPATH, '//a/span[text()="HR Administration"][1]').click()
time.sleep(3)

driver.find_element(By.XPATH, '//i[text()="add"]').click()
time.sleep(2)
label_elements = driver.find_elements(By.XPATH, '//form[@name="oxdModalForm"]//label')
field_names = []
for label_element in label_elements:
    field_name = label_element.text
    if field_name not in field_names:
        field_names.append(field_name)

print(field_names)
driver.quit()


