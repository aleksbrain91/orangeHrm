from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.safari.service import Service as SafariService
from concurrent.futures import ThreadPoolExecutor
import traceback

def run_test_in_browser(browser_name):
    try:
        if browser_name == 'chrome':
            driver = webdriver.Chrome()
        elif browser_name == 'safari':
            # Enable detailed logging if needed
            service = SafariService(service_args=["--diagnose"])
            options = webdriver.SafariOptions()
            # Add any specific Safari options here
            driver = webdriver.Safari(options=options, service=service)
        else:
            print(f"Browser {browser_name} not supported.")
            return

        driver.get("https://portnov_administrator-trials712.orangehrmlive.com")

        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='txtUsername']"))
        )
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[id='txtPassword']"))
        )
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )

        username_input.send_keys("Admin")
        password_input.send_keys("qTJn5@5APu")
        submit_button.click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="widget-header-text"]'))
        )

        section_texts = [item.text for item in driver.find_elements(By.CSS_SELECTOR, 'span[class="widget-header-text"]')]
        print(f"Sections in {browser_name}: {section_texts}")

    except Exception as e:
        print(f"An error occurred in {browser_name}:")
        traceback.print_exc()
    finally:
        driver.quit()

# List of browsers to run the test on
browsers = ['chrome', 'safari']

# Using ThreadPoolExecutor to run tests in parallel
with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(run_test_in_browser, browsers)
