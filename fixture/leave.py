import time

from fixture.calendar import Calendar, CalendarType
from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class Leave:
    selector_example = "//div[@id='systemUserDiv'] //*[text()='add']"
    loading_spinner_bar = '.bar .peg'
    table_headers = 'table[class="highlight bordered"] th'
    from_calendar_button = '//label[@for="from"]/.. //i[text()="date_range"]'
    to_calendar_button = '//label[@for="to"]/.. //i[text()="date_range"]'
    search_button = '//button[text()="Search"]'
    result_message = '.toast-message'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.calendar = Calendar(self.step, CalendarType.DEFAULT)

    def wait_for_page_load(self):
        self.step.wait_for_element(self.loading_spinner_bar, 10)
        self.step.specified_element_is_not_present(self.loading_spinner_bar, 10)
        time.sleep(0.5)
        self.step.wait_for_element(self.table_headers, 10)

    def click_on_from_calendar_button(self):
        self.step.wait_for_element(self.from_calendar_button, 10)
        self.step.click_on_element(self.from_calendar_button, True, check_clickable=True)

    def click_on_to_calendar_button(self):
        self.step.wait_for_element(self.to_calendar_button, 10)
        self.step.click_on_element(self.to_calendar_button, True, check_clickable=True)

    def click_on_search_button(self):
        self.step.click_on_element(self.search_button)

    def get_result_message_text(self):
        self.step.wait_for_element(self.result_message, 10)
        return self.step.get_element_text(self.result_message)