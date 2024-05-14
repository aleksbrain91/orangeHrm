from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table


class RecruitmentAts:
    add_candidate_button = 'button[tooltip="Add Candidate"]'
    page_loading_animation = 'div[class="oxd-skeleton --animate"]'
    message_of_successful_action = '//div[contains(@class, "oxd-toast-content")]//p[2]'
    search_input_field = '//input[@placeholder="Search"][@data-test="autocompleteSelect"]'
    search_field_spinner = '//div[text()="Searching..."]'
    search_autocomplete_dropdowns = '.oxd-autocomplete-option span'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='.oxd-table-body .oxd-table-card',
                           column_selectors={'checkbox': 'div[role="cell"]:nth-child(1)',
                                             'name': 'div[role="cell"]:nth-child(3) a',
                                             'vacancy': 'div[role="cell"]:nth-child(3) .oxd-table-cell-pill',
                                             'email': 'div[role="cell"]:nth-child(4) div',
                                             'contact': 'div[role="cell"]:nth-child(5) div',
                                             'date_applied': 'div[role="cell"]:nth-child(6) div',
                                             'stage': 'div[role="cell"]:nth-child(7) div'})

    def wait_for_page_load(self):
        self.step.specified_element_is_not_present(self.page_loading_animation, 20)

    def click_on_add_candidate_button(self):
        self.step.click_on_element(self.add_candidate_button)

    def get_action_message_text(self):
        self.step.wait_for_element(self.message_of_successful_action, 10)
        return self.step.get_element_text(self.message_of_successful_action)

    def set_search(self, text):
        self.step.input_text(self.search_input_field, text)
        self.step.wait_for_element(self.search_field_spinner, 5)
        self.step.specified_element_is_not_present(self.search_field_spinner, 15)
        self.step.click_element_containing_text(self.search_autocomplete_dropdowns, text)
