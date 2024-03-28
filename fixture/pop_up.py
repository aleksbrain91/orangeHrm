import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class PopUp:
    user_name_field = '#user_name'
    employee_name_field = '#selectedEmployee_value'
    password_field = '#password'
    confirm_password_field = '#confirmpassword'
    save_button = '#modal-save-button'
    user_exists_error_massage = "//span[text()='Already exists']"
    user_name_filter_field = "#systemuser_uname_filter"
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    filter_search_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Search"]'
    pass_required_message = '//input[@id="password"]/following::span[text()="Required"]'
    confirm_pass_required_message = '//input[@id="confirmpassword"]/following::span[text()="Required"]'
    pass_length_message = '//input[@id="password"]/following::span[text()="Your password should have at least 8 characters."]'
    pass_strength_message = '.password-strength-check'
    empty_space = '.password-help-text-container small'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_username(self, text):
        self.step.input_text(self.user_name_field, text)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_name_field, text)

    def set_password(self, text):
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def click_on_empty(self):
        time.sleep(2)
        # ^ add this "sleep" because without it test cases 8,9,10,11 fails on last step
        self.step.click_on_element(self.empty_space)

    def get_user_exist_error(self):
        return self.step.get_element_text(self.user_exists_error_massage)

    def click_on_password_field(self):
        self.step.click_on_element(self.password_field)

    def get_pass_required_message(self):
        return self.step.get_element_text(self.pass_required_message)

    def get_confirm_pass_required_message(self):
        return self.step.get_element_text(self.confirm_pass_required_message)

    def input_in_pass_field(self,text):
        self.step.input_text(self.password_field, text)

    def get_pass_field_length_message(self):
        return self.step.get_element_text(self.pass_length_message)

    def get_pass_strength_message(self):
        self.step.specified_element_is_present(self.pass_strength_message, 30)
        return self.step.get_element_text(self.pass_strength_message)



    def set_user_name_filter(self, text):
        self.step.input_text(self.user_name_filter_field, text)

    def get_filter_table_name(self):
        return self.step.get_element_text(self.filter_popup_table)

    def click_filter_search_button(self):
        self.step.click_on_element(self.filter_search_button)
