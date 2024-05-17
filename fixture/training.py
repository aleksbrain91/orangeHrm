from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver
from fixture.table import Table


class Training:
    filter_button = "a[id=searchModal]"
    add_course_button = "//i[text()='add']"
    iframe = "#noncoreIframe"
    loading_spinner = 'div[class="center-align loading"]'
    title_input_field = '#addCourse_title'
    coordinator_input_field = '#addCourse_coordinator_empName'
    coordinator_input_field_autocomplete_dropdowns = '.autoComplete-title'
    coordinator_input_field_warning = '#addCourse_coordinator_empName-error'
    save_button = '#btnSaveCourse'
    save_confirmation_message = '.toast-message'
    go_to_courses_button = 'a[data-tooltip="Courses"]'
    table_filter_spinner = '#preloader .gap-patch'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#resultTable tbody tr',
                           column_selectors={'check_box_list': '#resultTable td:nth-child(1)',
                                             'title': '#resultTable td:nth-child(2) a',
                                             'subunit': '#resultTable td:nth-child(3) a',
                                             'coordinator': '#resultTable td:nth-child(4) a',
                                             'company': '#resultTable td:nth-child(5) a',
                                             'status': '#resultTable td:nth-child(6) a'})

    def click_on_filter_button(self):
        self.step.click_on_element(self.filter_button)

    def click_on_add_course_button(self):
        self.step.click_on_element(self.add_course_button)

    def wait_for_page_loading(self):
        self.step.specified_element_is_not_present(self.loading_spinner, 30)

    def set_course_title(self, text):
        self.step.input_text(self.title_input_field, text)

    def set_course_coordinator(self, text):
        self.step.input_text(self.coordinator_input_field, text)
        self.step.wait_for_element(self.coordinator_input_field_autocomplete_dropdowns, 5)
        if self.step.specified_element_is_present(self.coordinator_input_field_warning, 5) == False:
            self.step.click_element_containing_text(self.coordinator_input_field_autocomplete_dropdowns, text)

    def click_on_save_button(self):
        self.step.click_on_element(self.save_button)

    def get_save_confirmation_message_text(self):
        self.step.wait_for_element(self.save_confirmation_message, 5)
        return self.step.get_element_text(self.save_confirmation_message)

    def click_on_go_to_courses_button(self):
        self.step.click_on_element(self.go_to_courses_button)

    def wait_for_filtered_table(self):
        self.step.specified_element_is_not_present(self.table_filter_spinner,20)