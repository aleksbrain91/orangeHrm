
from fixture.calendar import Calendar, CalendarType
from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class Leave:
    selector_example = "//div[@id='systemUserDiv'] //*[text()='add']"
    loading_spinner_bar = '.bar .peg'
    from_calendar_button = '//label[@for="from"]/.. //i[text()="date_range"]'
    to_calendar_button = '//label[@for="to"]/.. //i[text()="date_range"]'
    search_button = '//button[text()="Search"]'
    result_message = '.toast-message'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.calendar = Calendar(self.step, CalendarType.DEFAULT)

    def wait_for_page_load(self):
        self.step.specified_element_is_not_present(self.loading_spinner_bar, 10)

    def click_on_from_calendar_button(self):
        self.step.click_on_element(self.from_calendar_button)

    def click_on_to_calendar_button(self):
        self.step.click_on_element(self.to_calendar_button)

    def click_on_search_button(self):
        self.step.click_on_element(self.search_button)

    def get_result_message_text(self):
        self.step.wait_for_element(self.result_message, 10)
        return self.step.get_element_text(self.result_message)