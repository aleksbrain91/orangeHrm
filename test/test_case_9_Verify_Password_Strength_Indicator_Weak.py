# Test Case 9: Verify Password Strength Indicator - Weak
# Test Name: Test_Password_Strength_Weak
# Purpose: To verify that the password strength indicator shows 'Weak' when the password includes two uppercase letters.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'AA000000' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Weak' message.
def test_case_9_Verify_Password_Strength_Indicator_Weak(app):
    app.orangeHrm.openUrl("https://portnov_admin-trials711.orangehrmlive.com/client/#/dashboard")
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.input_in_pass_field("AA00000A")
    app.orangeHrm.popUp.click_on_save()
    app.assert_that(app.orangeHrm.popUp.get_pass_strength_message()).is_equal_to("Weak")
    #it won't show "Weak" with provided pass"AA000000",but will do with this "AA00000A",for example