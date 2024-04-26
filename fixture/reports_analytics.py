from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class ReportsAnalytics:
    loading_spinner = '.oxd-loading-spinner'
    new_folder_button = 'button[tooltip="New Folder"]'
    folder_success_save_message = '//div[@class="oxd-toast-content oxd-toast-content--success"]/p'
    folder_names_list = '.reports-accordion-header-title p'


    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def wait_for_page_loading(self):
        self.step.specified_element_is_not_present(self.loading_spinner, 30)

    def click_on_new_folder_button(self):
        self.step.click_on_element(self.new_folder_button)

    def get_succcess_meassage_text(self):
        return self.step.get_elements_texts(self.folder_success_save_message)

    def get_folder_names_list(self):
        return self.step.get_elements_texts(self.folder_names_list)