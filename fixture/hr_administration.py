from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table


class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_users_button = '//a[@data-tooltip="Filter"]'
    filtered_usernames = 'tbody td:nth-child(2) span'
    filtered_user_roles = 'tbody td:nth-child(3) span'
    filter_no_records_message = '//div[text()="No Records Found"]'
    save_button = '#modal-save-button'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    first_table_row = '#systemUserDiv tbody tr:nth-child(1)'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#systemUserDiv tbody tr',
                           column_selectors={'check_box': 'td:nth-child(1)',
                                             'user_name': 'td:nth-child(2)',
                                             'user_role': 'td:nth-child(3)'})

    def wait_for_table(self):
        self.step.wait_for_element(self.first_table_row, 40)

    def click_add_user(self):
        self.step.specified_element_is_present(self.add_user_button,30)
        self.step.click_on_element(self.add_user_button)
        self.step.wait_for_element(self.save_button)

    def click_filter_button(self):
        self.step.specified_element_is_present(self.filtered_usernames,30)
        self.step.click_on_element(self.filter_users_button)

    def get_filtered_usernames(self):
        self.step.wait_for_element(self.filtered_usernames)
        return self.step.get_elements_texts(self.filtered_usernames)

    def get_filtered_user_roles(self):
        self.step.wait_for_element(self.filtered_user_roles)
        return self.step.get_elements_texts(self.filtered_user_roles)

    def get_filter_no_record_message(self):
        self.step.specified_element_is_present(self.filter_no_records_message, 2)
        return self.step.get_element_text(self.filter_no_records_message)

    def make_sure_that_user_not_found(self):
        self.step.specified_element_is_not_present(self.filter_no_records_message, 5)
        return self.step.specified_element_is_present(self.filtered_usernames)