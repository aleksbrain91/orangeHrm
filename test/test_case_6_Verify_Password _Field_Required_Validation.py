# Test Case 6: Verify Password Field Required Validation
# Test Name: Test_Password_Field_Required
# Purpose: To verify that the password field shows a 'required' error message when left empty.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Login to the application with valid credentials.
# 3. Navigate to the 'HR Administration' section from the left menu.
# 4. Click on the 'Add User' button.
# 5. Leave the 'Password' and 'Confirm Password' fields empty.
# 6. Click outside the password fields to trigger validation.
# Expected Result:
# An error message stating 'Required' should appear under both 'Password' and 'Confirm Password' fields.


def test_case_6_verify_password_field_required_validation(app):
    app.orangeHrm.openUrl("https://portnov_admin-trials711.orangehrmlive.com/client/#/dashboard")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_password_field()
    app.orangeHrm.popUp.click_on_save()
    app.assert_that(app.orangeHrm.popUp.get_confirm_pass_required_message()).is_equal_to("Required")
    app.assert_that(app.orangeHrm.popUp.get_pass_required_message()).is_equal_to("Required")
