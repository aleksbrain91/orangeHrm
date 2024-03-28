import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class HrAdministration:
    add_user_button = "//div[@id='systemUserDiv'] //*[text()='add']"
    filter_users_button = '//a[@data-tooltip="Filter"]'
    filtered_usernames = 'tbody td:nth-child(2) span'
    filtered_user_roles = 'tbody td:nth-child(3) span'
    filter_no_records_message = '//div[text()="No Records Found"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd


    def click_add_user(self):
        self.step.specified_element_is_present(self.add_user_button, 20)
        self.step.click_on_element(self.add_user_button)

    def click_filter_button(self):
        self.step.specified_element_is_present(self.filtered_usernames,30)
        self.step.click_on_element(self.filter_users_button)

    def get_filtered_usernames(self):
        # self.step.specified_element_is_present(self.filtered_usernames, 30)
        # ^methods above not worked for me, alswys getting StaleElementReferenceException
        time.sleep(2)
        return self.step.get_elements_texts(self.filtered_usernames)

    def get_filtered_user_roles(self):
        # self.step.specified_element_is_present(self.filtered_user_roles, 30)
        # ^ same here, only sleep works
        time.sleep(2)
        return self.step.get_elements_texts(self.filtered_user_roles)

    def get_filter_no_record_message(self):
        self.step.specified_element_is_present(self.filter_no_records_message, 2)
        return self.step.get_element_text(self.filter_no_records_message)

    def make_sure_that_user_not_found(self):
        self.step.specified_element_is_not_present(self.filter_no_records_message, 5)
        return self.step.specified_element_is_present(self.filtered_usernames)