import time

from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


class StepHelper:

    def __init__(self, app):
        # Initializes an instance of the StepHelper class with the application context.
        self.app = app
        self.wd = self.app.wd

    def get_how(self, locator):
        # Determines how to locate an element based on the given locator string.
        if locator.startswith("//") or locator.startswith("(//"):
            how = By.XPATH
        else:
            how = By.CSS_SELECTOR
        return how

    def specified_element_is_present(self, locator, time=3):
        # Checks if a specified element is present on the page within a given timeframe.
        try:
            WebDriverWait(self.wd, time).until(
                EC.presence_of_element_located((self.get_how(locator), locator)))
        except NoSuchElementException:
            return False
        except TimeoutException:
            return False
        return True

    def click_on_element(self, locator, pause_before_click=0.5, scrollInToView=False):
        # Clicks on a specified element, optionally scrolling into view and pausing before clicking.
        WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        element = WebDriverWait(self.wd, 10).until(
            EC.element_to_be_clickable((self.get_how(locator), locator))
        )
        if scrollInToView:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            time.sleep(2)
        ActionChains(self.wd).move_to_element(element).pause(pause_before_click).click().perform()

    def input_text(self, locator, text):
        # Enters text into a specified input field.
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        element.click()
        element.clear()
        element.send_keys(text)

    def get_list_of_elements(self, locator):
        # Returns a list of elements matching the specified locator.
        by = self.get_how(locator)
        WebDriverWait(self.wd, 10).until(
            EC.presence_of_all_elements_located((self.get_how(locator), locator)))
        return self.wd.find_elements(by=by, value=locator)

    def get_element_text(self, locator, scrollInToView=False):
        # Retrieves the text from a specified element, optionally scrolling it into view.
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        if scrollInToView:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            time.sleep(2)
        return element.text

    def get_element_attribute_value(self, locator, attribute, scrollInToView=False):
        # Retrieves the value of a specified attribute from an element, optionally scrolling it into view.
        element = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        if scrollInToView:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            time.sleep(2)
        return element.get_attribute(attribute)

    def specified_element_is_not_present(self, locator, waitingTime=3):
        # Waits to ensure a specified element is not present or becomes invisible.
        time.sleep(1)
        WebDriverWait(self.wd, waitingTime).until(
            EC.invisibility_of_element_located((self.get_how(locator), locator)))

    def wait_for_element(self, locator, wait_time=10):
        # Waits for a specified element to be visible.
        element = WebDriverWait(self.wd, wait_time).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        return element

    def jsXpathClick(self, locator):
        # Performs a click on an element using JavaScript, specifically for XPATH locators.
        time.sleep(2)
        b = self.wd.find_element(By.XPATH, locator)
        self.wd.execute_script("arguments[0].click();", b)

    def select_dropdown_by_value(self, locator, value):
        # Selects an option from a dropdown element by its value.
        dropdown = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        Select(dropdown).select_by_value(value)

    def select_dropdown_by_text(self, locator, text):
        # Selects an option from a dropdown element by the visible text.
        dropdown = WebDriverWait(self.wd, 10).until(
            EC.visibility_of_element_located((self.get_how(locator), locator)))
        Select(dropdown).select_by_visible_text(text)

    def get_elements_texts(self, locator):
        # Retrieves texts from all elements matching the specified locator and returns them as a list.
        WebDriverWait(self.wd, 10).until(
            EC.presence_of_all_elements_located((self.get_how(locator), locator)))
        elements = self.wd.find_elements(self.get_how(locator), locator)
        texts = []
        for element in elements:
            self.wd.execute_script(
                "arguments[0].scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'start' });", element)
            text = element.text.strip()
            texts.append(text)
        return texts

    def click_element_by_text(self, locator, text):
        # Clicks on an element within a list that matches the specified text.
        elements = self.get_list_of_elements(locator)
        for element in elements:
            if element.text == text:
                element.click()
                break