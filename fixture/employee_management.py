import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class EmployeeManagement:
    home_button = '//i[text()="oxd_home_menu"]'
    widget_header = '.widget-header span:last-child'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd


    def click_on_home_button(self):
        self.step.click_on_element(self.home_button)

    def get_widget_names(self):
        return self.step.get_elements_texts(self.widget_header)

