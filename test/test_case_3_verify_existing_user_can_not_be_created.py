# Test Case 3: Verify that an existing user cannot be created again
# Steps:
# 1. Go to 'HR Administration' section in side menu
# 2. Navigate to the "Add User" section in the OrangeHRM application.
# 3. Enter "Admin" in the Username field.
# 4. Enter all other required fields with valid data.
# 5. Click on the "Save" button.
# Expected Result:
# The system should not allow creating a user with a username that already exists and should display an appropriate error message.

def test_case_3_verify_existing_user_can_not_be_created_again(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.set_username('Admin')
    app.orangeHrm.popUp.set_employee_name('Test')
    app.orangeHrm.popUp.set_password('test123')
    app.orangeHrm.popUp.set_confirm_password('test123')
    app.orangeHrm.popUp.click_on_save()
    app.assert_that(app.orangeHrm.popUp.get_user_exist_error()).is_equal_to('Already exists')