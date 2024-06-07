import logging
import os
import time

from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver
from fixture.table import Table
from helpers.utils import Utils


class Attendance:
    circle_spinner = '.oxd-circle-loader'
    table_headers = '.visible-report-table-header span'
    pay_period_button = '//label[text()="Pay Period"]/../div//button/i'
    data_format_button = '//label[text()="Data Format"]/../div//button/i'
    include_button = '//label[text()="Include"]/../div//button/i'
    arrow_dropdowns = '//div[@class="dropdown-menu show"]//span'
    input_dropdowns = '.multi-select-container span:nth-child(1)'
    employee_name_input_field = '//label[text()="Employee Name"]/..//input'
    supervisor_name_input_field = '//label[text()="Supervisor Name"]/..//input'
    job_title_input_field = '//label[text()="Job Title"]/..//input'
    export_csv_button = 'button[ng-click*="CsvExport"]'
    info_message = '.toast-message'
    leave_checkbox = '.custom-control-label'  # "#report_boolean_filter_show_leave_type_breakdown"

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#pim_report_table tbody tr',
                           column_selectors={'employee_id': '#pim_report_table tbody tr td:nth-child(1)',
                                             'employee_name': '#pim_report_table tbody tr td:nth-child(2)',
                                             'supervisors': '#pim_report_table tbody tr td:nth-child(3)',
                                             'regular_time': '#pim_report_table tbody tr td:nth-child(4)',
                                             'extra_time': '#pim_report_table tbody tr td:nth-child(5)',
                                             'total_leave_time': '#pim_report_table tbody tr td:nth-child(6)',
                                             'total_time': '#pim_report_table tbody tr td:nth-child(7)',
                                             'status': '#pim_report_table tbody tr td:nth-child(8)'})

    def wait_for_page_load(self):
        self.step.wait_for_element(self.circle_spinner, 10)
        self.step.specified_element_is_not_present(self.circle_spinner, 30)
        self.step.specified_element_is_present(self.table_headers, 10)

    def get_table_headers_text(self):
        return self.step.get_elements_texts(self.table_headers)

    def set_pay_period(self,text):
        self.step.click_on_element(self.pay_period_button, True)
        self.step.click_element_by_text(self.arrow_dropdowns, text, True)

    def set_data_format(self, text):
        self.step.click_on_element(self.data_format_button, True, True)
        self.step.click_element_by_text(self.arrow_dropdowns, text)

    def set_include(self, text):
        self.step.click_on_element(self.include_button, True)
        self.step.click_element_by_text(self.arrow_dropdowns, text, smartScroll=True)

    def set_employee_name(self, text):
        self.step.click_on_element(self.employee_name_input_field, True)
        self.step.input_text(self.employee_name_input_field, text)
        self.step.wait_for_element(self.input_dropdowns)
        time.sleep(1)
        self.step.click_element_containing_text(self.input_dropdowns, text)

    def set_supervisor_name(self, text):
        self.step.click_on_element(self.supervisor_name_input_field, True)
        self.step.input_text(self.supervisor_name_input_field, text)
        self.step.wait_for_element(self.input_dropdowns)
        time.sleep(1)
        self.step.click_element_containing_text(self.input_dropdowns, text)

    def set_job_title(self, text):
        self.step.click_on_element(self.job_title_input_field, True)
        self.step.input_text(self.job_title_input_field, text)
        self.step.wait_for_element(self.input_dropdowns)
        time.sleep(1)
        self.step.click_element_containing_text(self.input_dropdowns, text)

    def export_to_csv(self):
        self.step.click_on_element(self.export_csv_button)
        time.sleep(3)
        download_path = os.path.join(Utils.get_project_root(), 'files', 'download')
        if not os.path.exists(download_path):
            logging.info(f"Creating download directory: {download_path}")
            os.makedirs(download_path)
        logging.info(f"Download path: {download_path}")
        downloaded_files = os.listdir(download_path)
        logging.info(f"Downloaded files: {downloaded_files}")
        if len(downloaded_files) == 0:
            raise Exception("No files were downloaded.")

    def scroll_to_table_headers(self):
        self.step.scroll_element_into_center(self.table_headers)

    def get_info_message_text(self):
        self.step.wait_for_element(self.info_message, 10)
        return self.step.get_element_text(self.info_message)

    def click_on_leave_checkbox(self):
        self.step.click_on_element(self.leave_checkbox)