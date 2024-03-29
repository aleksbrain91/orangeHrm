from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://portnov_administrator-trials712.orangehrmlive.com")

driver.find_element(By.CSS_SELECTOR, "input[id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[id='txtPassword']").send_keys("qTJn5@5APu")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)
driver.find_element(By.CSS_SELECTOR, 'div[class="dashboard-widget-config-button"]').click()
time.sleep(5)
buttons = driver.find_elements(By.CSS_SELECTOR, 'div[class="configuration-tabs"] input[id*="adminWidgetSwitch"]')

for item in buttons:
    attribute_value = item.get_attribute('class')
    if 'ng-not-empty' in attribute_value:
        parent_div = item.find_element(By.XPATH, "..")
        parent_div.click()


driver.quit()
