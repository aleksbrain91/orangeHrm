from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

class PopUpReportAnalytics:
    add_folder_header = '//p[text()="Add Folder"]'
    add_folder_input_field = 'input[placeholder="Enter Folder Name"]'
    save_button = '//div[text()="Save"]'
    folder_success_save_message = '//div[@class="oxd-toast-content oxd-toast-content--success"]/p'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def input_new_folder_name(self, text):
        self.step.wait_for_element(self.add_folder_header)
        self.step.input_text(self.add_folder_input_field, text)

    def click_on_save_button(self):
        self.step.click_on_element(self.save_button, True)