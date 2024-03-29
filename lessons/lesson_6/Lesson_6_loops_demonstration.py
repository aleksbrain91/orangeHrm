from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://portnov_administrator-trials712.orangehrmlive.com")

driver.find_element(By.CSS_SELECTOR, "input[id='txtUsername']").send_keys("Admin")
driver.find_element(By.CSS_SELECTOR, "input[id='txtPassword']").send_keys("qTJn5@5APu")
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(5)
section_texts = []
menu_items = driver.find_elements(By.CSS_SELECTOR, 'span[class="widget-header-text"]')

for item in menu_items:
    section_texts.append(item.text)

print(section_texts)

# Close the browser
driver.quit()
