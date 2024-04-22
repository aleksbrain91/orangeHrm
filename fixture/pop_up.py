import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver


class PopUp:
    password_field = '#password'
    confirm_password_field = '#confirmpassword'
    save_button = '#modal-save-button'
    user_exists_error_massage = "//span[text()='Already exists']"
    user_name_filter_field = '#systemuser_uname_filter'
    employee_name_filter_field = '#employee_name_filter_value'
    filter_popup_table = '//div[@class="modal modal-fixed-footer open"]//h4[text()="Filter Users"]'
    filter_search_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Search"]'
    pass_required_message = '//input[@id="password"]/following-sibling::span'
    confirm_pass_required_message = '//input[@id="confirmpassword"]/following-sibling::span'
    pass_strength_message = '.password-strength-check'
    empty_space = '.password-help-text-container small'
    employee_name_filter_dropdown = '.angucomplete-title'
    employee_name_filter_dropdown_warnings = '//div[@id="employee_name_filter_dropdown" and @class="angucomplete-dropdown"]/div[2]'
    ess_role_input_field = '#essroles_inputfileddiv input'
    ess_role_dropdown = '#essroles_inputfileddiv li'
    supervisor_role_input_field = '#supervisorroles_inputfileddiv input'
    supervisor_role_dropdown = '#supervisorroles_inputfileddiv li'
    location_input_field = '#location_inputfileddiv input'
    location_dropdown = '#location_inputfileddiv li'
    admin_role_input_field = '#adminroles_inputfileddiv input'
    admin_role_dropdown = '#adminroles_inputfileddiv li'
    status_input_field = '#status_inputfileddiv input'
    status_dropdown = '#status_inputfileddiv li'
    filter_reset_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Reset"]'
    filter_cancel_button = '//div[@class="modal modal-fixed-footer open"]//a[text()="Cancel"]'
    searching_text = '//div[@id="employee_name_filter_dropdown"]/div[text()="Searching..."]'
    employee_filter_table_header = "//h4[text()='Filter Employees By']"
    employee_filter_list_of_drop_down_values = 'ul[id^="select-options"][style*="display: block"] li span'
    employee_filter_location_input_field = '//label[text()="Location"]/preceding-sibling::div//input'
    employee_filter_employment_status_input_field = '//label[text()="Employment Status"]/preceding-sibling::div//input'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def set_username(self, text):
        self.step.input_text(self.user_name_filter_field, text)

    def set_employee_name_filter(self, text):
        self.step.input_text(self.employee_name_filter_field, text)
        self.step.specified_element_is_not_present(self.searching_text, 6)
        if self.step.specified_element_is_present(self.employee_name_filter_dropdown_warnings, 3) == False:
            self.step.click_element_containing_text(self.employee_name_filter_dropdown, text)

    def set_password(self, text):
        self.step.click_on_element(self.password_field)
        self.step.input_text(self.password_field, text)

    def set_confirm_password(self, text):
        self.step.input_text(self.confirm_password_field, text)

    def click_on_save(self):
        self.step.click_on_element(self.save_button)

    def click_on_empty(self):
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

    def get_pass_strength_message(self):
        self.step.specified_element_is_present(self.pass_strength_message, 30)
        return self.step.get_element_text(self.pass_strength_message)

    def click_on_user_name_filter(self):
        self.step.specified_element_is_present(self.user_name_filter_field, 10)
        self.step.click_on_element(self.user_name_filter_field)

    def set_user_name_filter(self, text):
        self.step.input_text(self.user_name_filter_field, text)

    def get_filter_table_name(self):
        self.step.specified_element_is_present(self.filter_popup_table, 20)
        return self.step.get_element_text(self.filter_popup_table)

    def click_filter_search_button(self):
        self.step.click_on_element(self.filter_search_button)
        self.step.specified_element_is_not_present(self.filter_popup_table)

    def click_on_employee_name_filter(self):
        self.step.specified_element_is_present(self.employee_name_filter_field, 20)
        self.step.click_on_element(self.employee_name_filter_field)

    def get_employee_name_dropdown_text(self):
        self.step.specified_element_is_present(self.employee_name_filter_dropdown, 10)
        return self.step.get_elements_texts(self.employee_name_filter_dropdown)

    def get_employee_name_dropdown_warning_text(self):
        self.step.specified_element_is_present(self.employee_name_filter_dropdown_warnings, 10)
        return self.step.get_element_text(self.employee_name_filter_dropdown_warnings)

    def get_ess_role_dropdown_values(self):
        return self.step.get_elements_texts(self.ess_role_dropdown)

    def get_admin_role_dropdown_values(self):
        return self.step.get_elements_texts(self.admin_role_dropdown)

    def get_supervisor_role_dropdown_values(self):
        return self.step.get_elements_texts(self.supervisor_role_dropdown)

    def get_status_dropdown_values(self):
        return self.step.get_elements_texts(self.status_dropdown)

    def get_location_dropdown_values(self):
        return self.step.get_elements_texts(self.location_dropdown)

    def set_ess_role_dropdown(self,text):
        self.step.click_on_element(self.ess_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.ess_role_dropdown,text)

    def set_admin_role_dropdown(self,text):
        self.step.click_on_element(self.admin_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.admin_role_dropdown,text)

    def set_supervisor_role_dropdown(self,text):
        self.step.click_on_element(self.supervisor_role_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.supervisor_role_dropdown,text)

    def set_status_dropdown(self,text):
        self.step.click_on_element(self.status_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.status_dropdown,text)

    def set_location_dropdown(self,text):
        self.step.click_on_element(self.location_input_field)
        time.sleep(0.5)
        self.step.click_element_by_text(self.location_dropdown,text)

    def click_on_filter_reset_button(self):
        self.step.click_on_element(self.filter_reset_button)

    def get_value_from_user_name_filter_field(self):
        return self.step.get_element_attribute_value(self.user_name_filter_field,"class")

    def get_value_from_employee_name_filter_field(self):
        return self.step.get_element_attribute_value(self.employee_name_filter_field,"class")

    def get_value_from_ess_role_input_field(self):
        return self.step.get_element_attribute_value(self.ess_role_input_field, "value")

    def get_value_from_admin_role_input_field(self):
        return self.step.get_element_attribute_value(self.admin_role_input_field, "value")

    def get_value_from_supervisor_role_input_field(self):
        return self.step.get_element_attribute_value(self.supervisor_role_input_field, "value")

    def get_value_from_status_input_field(self):
        return self.step.get_element_attribute_value(self.status_input_field, "value")

    def get_value_from_location_input_field(self):
        return self.step.get_element_attribute_value(self.location_input_field, "value")

    def click_on_filter_cancel_button(self):
        self.step.click_on_element(self.filter_cancel_button)

    def get_filter_employee_table_header(self):
        self.step.wait_for_element(self.employee_filter_table_header)
        return self.step.get_element_text(self.employee_filter_table_header)

    def set_employee_filter_table_location_dropdown(self,text):
        self.step.click_on_element(self.employee_filter_location_input_field, True, True)
        time.sleep(0.5)
        self.step.click_element_containing_text(self.employee_filter_list_of_drop_down_values,text)

    def set_employee_filter_table_employment_status_dropdown(self,text):
        self.step.click_on_element(self.employee_filter_employment_status_input_field,True)
        time.sleep(0.5)
        self.step.click_element_by_text(self.employee_filter_list_of_drop_down_values,text)