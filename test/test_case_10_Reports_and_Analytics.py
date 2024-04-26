# Test case 10 - verify folders creation functionality
# TODO: Open the application
# TODO: Login
# TODO: Click on Reports and Analytics
# TODO: Click on New Folder
# TODO: Fill in the folder name
# TODO: Click Save
# TODO: Verify that New Folder appeared in the list of folders

def test_case_10_verify_folders_creation_functionality(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Reports and Analytics")
    app.orangeHrm.reportsAnalytics.wait_for_page_loading()
    app.orangeHrm.reportsAnalytics.click_on_new_folder_button()
    app.orangeHrm.popUpreportsAnalytics.input_new_folder_name("NewFolder")
    app.orangeHrm.popUpreportsAnalytics.click_on_save_button()
    app.assert_that(app.orangeHrm.reportsAnalytics.get_succcess_meassage_text()).contains("Successfully Saved")
    app.orangeHrm.reportsAnalytics.wait_for_page_loading()
    app.assert_that(app.orangeHrm.reportsAnalytics.get_folder_names_list()).contains("NewFolder")
