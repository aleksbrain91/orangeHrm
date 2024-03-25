# Test Case 7: Verify Password Minimum Length Validation
# Test Name: Test_Password_Min_Length
# Purpose: To verify that the password field shows a minimum length error message when fewer than 8 characters are entered.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter a single character in the 'Password' field.
# 3. Click outside the password field to trigger validation.
# Expected Result:
# An error message stating 'Your password must have at least 8 characters.' should appear under the 'Password' field.
def test_case_7_Verify_Password_Minimum_Length_Validation(app):
    app.orangeHrm.openUrl("https://portnov_admin-trials711.orangehrmlive.com/client/#/dashboard")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.input_in_pass_field("0")
    app.orangeHrm.popUp.click_on_save()
    app.assert_that(app.orangeHrm.popUp.get_pass_field_length_message()).is_equal_to("Your password should have at least 8 characters.")

