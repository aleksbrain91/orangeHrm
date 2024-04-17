from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver
from fixture.table import Table

class EmployeeManagement:
    home_button = '//i[text()="oxd_home_menu"]'
    widget_header = '.widget-header span:last-child'
    widget_config_button = '.dashboard-widget-config-button'
    widget_config_panel =  '.widget-configuration-panel'   #'//span[@class="widget-configuration-panel active"]'
    my_widgets_button_inside_widget_panel = '//span[text()="My Widgets"]'
    widgets_names_inside_my_widgets = '.configuration-tab .oxd-switch-label'
    employee_management_loading_spinners = '//div[text()="Loading"]'
    employee_table_first_row = '#employeeListTable tbody tr:nth-child(1)'
    filter_button = "//i[text()='oxd_filter']"
    employee_management_table_loading_spinner = '#loading-bar .bar .peg'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#employeeListTable tbody tr',
                           column_selectors={'employee_id': 'td:nth-child(2)',
                                             'name': 'td:nth-child(3) a',
                                             'job_title': 'td:nth-child(4)',
                                             'employment_status': 'td:nth-child(5)',
                                             'locations': 'td:nth-child(8)'})


    def click_on_home_button(self):
        self.step.click_on_element(self.home_button)

    def get_widget_names(self):
        return self.step.get_elements_texts(self.widget_header)

    def click_on_widget_config_button(self):
        self.step.specified_element_is_not_present(self.employee_management_loading_spinners, 15)
        self.step.click_on_element(self.widget_config_button)

    def click_on_my_widgets_button_inside_widget_panel(self):
        if self.step.wait_for_attribute_change(self.widget_config_panel, "class", "widget-configuration-panel active",10):
            self.step.click_on_element(self.my_widgets_button_inside_widget_panel)

    def get_widgets_names_inside_my_widgets(self):
        return self.step.get_elements_texts(self.widgets_names_inside_my_widgets)

    def click_on_filter_button(self):
        self.step.click_on_element(self.filter_button)

    def wait_for_table_reload(self):
        self.step.specified_element_is_not_present(self.employee_management_table_loading_spinner, 10)
