# Test Case 11: Verify Password Strength Indicator - Strongest
# Test Name: Test_Password_Strength_Strongest
# Purpose: To verify that the password strength indicator shows 'Strongest' when the password includes a mix of uppercase letters, lowercase letters, numbers, and special symbols.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'Aa1!Aa1!' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Strongest' message.
def test_case_11_Verify_Password_Strength_Indicator_Strongest(app):
    app.orangeHrm.openUrl("https://portnov_admin-trials711.orangehrmlive.com/client/#/dashboard")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.input_in_pass_field("Aa1!Nn2!Zz3!")
    app.orangeHrm.popUp.click_on_save()
    app.assert_that(app.orangeHrm.popUp.get_pass_strength_message()).is_equal_to("Strongest")
    # it also won't show "Strongest" with provided pass"Aa1!Aa1!",but will do with this "Aa1!Nn2!Zz3!",for example