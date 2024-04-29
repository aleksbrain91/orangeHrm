import time

from selenium.webdriver.common.by import By

# Demonstrate how to use debugger
def test_debugger_demonstration_usage(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Links")
    app.demonstrationAppDemoQa.click_home_button()
    app.step.switch_to_tab_by_url("https://demoqa.com/")
    page_banner = app.demonstrationAppDemoQa.get_page_banner()
    page_url = app.demonstrationAppDemoQa.get_home_page_url()
    app.assert_that(app.demonstrationAppDemoQa.get_page_banner()).is_equal_to("Selenium Online Training")
    app.assert_that(app.demonstrationAppDemoQa.get_home_page_url()).is_equal_to('https://demoqa.com/')

# PRACTICAL EXAMPLES:
def test_drag_and_drop_functionality(app):
    # Navigate to the draggable demo page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/dragabble")
    # Perform drag and drop on the specified element
    app.demonstrationAppDemoQa.drag_and_drop_dragabble() # element attribute is not needed here

def test_dropdown_menu_interaction(app):
    # Open the URL for the select menu page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/select-menu")
    # Select an item from the dropdown
    app.demonstrationAppDemoQa.select_value_from_select_one_dropdown("Other") # there are no "title" in dropdown

def test_dropdown_menu_interaction1(app):
    # Open the default URL set in the openUrl method
    app.demonstrationAppDemoQa.openUrl()
    # Navigate to the draggable demo page
    app.demonstrationAppDemoQa.go_to_side_menu_section("Widgets", "Select Menu") # There are no "home" in sub menu items
    # Select 'White' from the dropdown menu
    app.demonstrationAppDemoQa.select_value_from_select_one_dropdown('Other') # There are no "White" in dropdown or wrong dropdown selected

def test_dropdown_menu_interaction2(app):
    # Navigate to the select menu page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/select-menu")
    # Select an item from the dropdown
    app.demonstrationAppDemoQa.select_one_more_value_from_select_one_dropdown('Other')
    # Mistake in called methode (double click on same element), also there are no "White" in selected dropdown

def test_file_upload_functionality(app):
    # Navigate to the file upload page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/upload-download")
    # Upload a file using an absolute path
    app.demonstrationAppDemoQa.upload_my_file(r'C:\Users\Alexbrain\PycharmProjects\orangeHrm\files\some_file.txt')

def test_navigation_to_home(app):
    # Open the main page of the site
    app.demonstrationAppDemoQa.openUrl()
    # Go to Links section
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Links")
    # Click the home button to navigate to the home page
    app.demonstrationAppDemoQa.click_home_button()
    # Assert the URL to check if it's correct
    app.step.switch_to_tab_by_url("https://demoqa.com/") # First we need to switch wd to a new tab
    app.assert_that(app.demonstrationAppDemoQa.get_home_page_url()).is_equal_to("https://demoqa.com/") # Then assert page url

def test_modal_dialog_interaction(app):
    # Open the modal dialogs page
    app.demonstrationAppDemoQa.openUrl("https://demoqa.com/modal-dialogs")
    # Click to Open the small modal without checking if it's open
    time.sleep(3)                                          # This wait needed because of appearing advertising windows that interrupts click
    app.step.scroll_element_into_center("#showSmallModal") # Then we need to scroll this element also because of appearing advertising windows that interrupts click
    app.demonstrationAppDemoQa.wd.find_element(By.ID, "showSmallModal").click() # Provided id "closeSmallModal" was wrong
    # Get the text from the modal title and store it
    modal_title_text = app.demonstrationAppDemoQa.wd.find_element(By.ID, "example-modal-sizes-title-sm").text
    # Assert that the modal title text matches expected text
    assert modal_title_text == 'Small Modal'