'''
Homework Assignment: Applying Conditions
Objective: Perform the same initial steps as the previous assignment to log into the application and navigate to the "Add User" page. Instead of listing input fields, you will find the user status option (which by default is set to "Enabled"). If the status is not set to "Disabled," change it to "Disabled." This task requires you to apply conditions to interact with web elements.

Steps:

Open the web application in a browser.
Log into the application with provided credentials.
From the side menu, navigate to the "HR Administration" section.
Click on the "Add User" button.
Locate the user status option on the "Add User" form.
Check the current status of the user. If it is not "Disabled," you need to select the "Disabled" option.
Ensure your script can handle both conditions: if the status is already "Disabled," it remains unchanged; otherwise, change it to "Disabled."
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

enabled_button = driver.find_element(By.XPATH, '//label[text()="Enabled"]/..')
disabled_button = driver.find_element(By.XPATH, '//label[text()="Disabled"]/..')

if 'selected-option' in enabled_button.get_attribute('class'):
    disabled_button.click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[contains(text(),"×")]').click()
    time.sleep(5)
elif 'selected-option' in disabled_button.get_attribute('class'):
    driver.find_element(By.XPATH,'//button[contains(text(),"×")]').click()
    time.sleep(5)


driver.quit()
