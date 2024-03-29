# Test Case 4: Verify that a user can be filtered by username
# Steps:
# 1. Navigate to the "HR Administration" section in the OrangeHRM application.
# 2. Click on the "Filter" icon/button.
# 3. Enter the username of an existing user in the Username field.
# 4. Click on the "Search" button.
# Expected Result:
# The system should filter out and display only the user(s) matching the entered username.

def test_case_4_verify_that_a_user_can_be_filtered_by_username(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_filter_table_name()).is_equal_to("Filter Users")
    app.orangeHrm.popUp.click_on_user_name_filter()
    app.orangeHrm.popUp.set_user_name_filter("Admin")
    app.orangeHrm.popUp.click_filter_search_button()
    app.assert_that(app.orangeHrm.hrAdministration.get_filtered_usernames()).contains('Admin')
    app.assert_that(app.orangeHrm.hrAdministration.get_filtered_user_roles()).contains('Default ESS, Default Supervisor, Global Admin')