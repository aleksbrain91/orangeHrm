# Test Case 3: Verify that a user's status can be enabled or disabled
# Steps:
# 1. Navigate to the "HR Administration" section in the OrangeHRM application.
# 2. Click on the "Filter" icon/button.
# 3. Enter the username of non-existing user in the Username field.
# 4. Click on the "Search" button.
# Expected Result:
# The system should filter out and display empty list of users.
# The Message: 'No Records Found' should be displayed.
import pytest


@pytest.mark.group1
def test_case_5_verify_that_a_users_status_can_be_enabled_or_disabled(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_filter_table_name()).is_equal_to("Filter Users")
    app.orangeHrm.popUp.click_on_user_name_filter()
    app.orangeHrm.popUp.set_user_name_filter("someuser")
    app.orangeHrm.popUp.click_on_filter_search_button()
    app.assert_that(app.orangeHrm.hrAdministration.get_filter_no_record_message()).is_equal_to("No Records Found")
    app.assert_that(app.orangeHrm.hrAdministration.make_sure_that_user_not_found()).is_equal_to(False)