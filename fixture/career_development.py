import time

from selenium.webdriver.remote.webdriver import WebDriver
from fixture.step import StepHelper
from fixture.table import Table


class CareerDevelopment:
    table_headers = 'thead th'
    table_first_header_dropdown = 'thead th a i'
    add_button = '.btn-floating'
    select_all_dropdown_option = 'li[id*="select"]'
    deselect_all_dropdown_option = 'li[id*="deselect"]'
    delete_selected_dropdown_option = 'li[id*="deleteSelection"]'
    delete_confirmation_button = '.btn-text-danger'
    add_idp_header = 'a[class="top-level-menu-item active un-clickable"]'
    employee_input_field = '#owner_value'
    idp_name_input_field = '#name'
    coach_input_field = '#coach_value'
    employee_input_field_searching_spinner = '//div[text()="Searching..."][@class="angucomplete-searching"]'
    employee_input_field_dropdowns = '.angucomplete-row '
    save_button = 'button[type="submit"]'
    success_message = '.toast-message'
    back_button = '//button[text()="Back"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='.highlight tbody  tr',
                           column_selectors={'checkboxes': '.highlight td:nth-child(1)',
                                             'employee_id': '.highlight td:nth-child(2)',
                                             'employee_name': '.highlight td:nth-child(3)',
                                             'idp_name': '.highlight td:nth-child(4)',
                                             'coach': '.highlight td:nth-child(5)',
                                             'invited_on': '.highlight td:nth-child(6)',
                                             'closed_on': '.highlight td:nth-child(7)',
                                             'status': '.highlight td:nth-child(8)'})


    def wait_for_table_loading(self):
        self.step.wait_for_element(self.table_headers, 40)

    def get_table_headers_names(self):
        return self.step.get_elements_texts(self.table_headers)

    def get_checkboxes_status(self):
        checkboxes = self.step.get_list_of_elements(self.table.column_selectors['checkboxes'])
        statuses = []
        for checkbox in checkboxes:
            input_element = checkbox.find_element(self.step.get_how("input"), "input")
            statuses.append(input_element.get_attribute('class'))
        return statuses

    def click_on_first_table_header(self):
        self.step.click_on_element(self.table_first_header_dropdown)

    def click_on_select_all_option(self):
        self.step.click_on_element(self.select_all_dropdown_option, True)

    def click_on_deselect_all_option(self):
        self.step.click_on_element(self.deselect_all_dropdown_option, True)

    def click_delete_selected_dropdown_option(self):
        self.step.click_on_element(self.delete_selected_dropdown_option, True)

    def click_confirm_delete(self):
        self.step.wait_for_element(self.delete_confirmation_button, 10)
        self.step.click_on_element(self.delete_confirmation_button, True)

    def click_on_add_button(self):
        self.step.click_on_element(self.add_button)

    def get_add_idp_header_text(self):
        self.step.wait_for_element(self.save_button, 10)
        # self.step.wait_for_element(self.add_idp_header, 20)
        return self.step.get_element_text(self.add_idp_header)

    def set_employee_name(self, text):
        self.step.input_text(self.employee_input_field, text)
        self.step.wait_for_element(self.employee_input_field_searching_spinner, 5)
        if self.step.specified_element_is_not_present(self.employee_input_field_searching_spinner, 5):
            self.step.click_element_containing_text(self.employee_input_field_dropdowns, text)

    def get_idp_name_input_field_text(self):
        self.step.wait_for_non_empty_attribute(self.idp_name_input_field, "value")
        input_element = self.wd.find_element(self.step.get_how(self.idp_name_input_field), self.idp_name_input_field)
        return input_element.get_attribute("value")

    def get_coach_input_field_text(self):
        self.step.wait_for_non_empty_attribute(self.coach_input_field, "value")
        input_element = self.wd.find_element(self.step.get_how(self.coach_input_field), self.coach_input_field)
        return input_element.get_attribute("value")

    def click_save_button(self):
        self.step.click_on_element(self.save_button, True)

    def get_success_message_text(self):
        self.step.wait_for_element(self.success_message, 10)
        return self.step.get_element_text(self.success_message)

    def click_back_button(self):
        self.step.wait_for_element(self.back_button, 10)
        self.step.click_on_element(self.back_button, True)

    # def find_and_click_added_employee_checkbox(self, text):
    #     employees = self.step.get_list_of_elements(self.table.column_selectors['employee_name'])
    #     for index, employee in enumerate(employees):
    #         if employee.text == text:
    #             checkboxes = self.step.get_list_of_elements(self.table.column_selectors['checkboxes'])
    #             checkbox = checkboxes[index]
    #             checkbox.click()
    #             break

    def find_and_click_added_employee_checkbox(self, text):
        self.step.find_and_click_element_in_same_row(self.table, text, 'employee_name', 'checkboxes')