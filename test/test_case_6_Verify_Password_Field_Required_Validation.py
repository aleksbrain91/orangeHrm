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
import time

import pytest


@pytest.mark.group2
def test_case_6_Verify_Password_Field_Required_Validation(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_password_field()
    app.orangeHrm.popUp.input_in_pass_field("0")
    app.orangeHrm.popUp.input_in_pass_field("")
    app.orangeHrm.popUp.click_on_empty()
    app.assert_that(app.orangeHrm.popUp.get_confirm_pass_required_message()).is_equal_to("Required")
    app.assert_that(app.orangeHrm.popUp.get_pass_required_message()).is_equal_to("Required")

# Test Case 6.1: Verify Password Minimum Length Validation
# Test Name: Test_Password_Min_Length
# Purpose: To verify that the password field shows a minimum length error message when fewer than 8 characters are entered.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter a single character in the 'Password' field.
# 3. Click outside the password field to trigger validation.
# Expected Result:
# An error message stating 'Your password must have at least 8 characters.' should appear under the 'Password' field.
@pytest.mark.group2
def test_case_6_1_Verify_Password_Minimum_Length_Validation(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_password_field()
    app.orangeHrm.popUp.input_in_pass_field("0")
    app.orangeHrm.popUp.click_on_empty()
    app.assert_that(app.orangeHrm.popUp.get_pass_required_message()).is_equal_to("Your password should have at least 8 characters.")



# Test Case 6.2: Verify Password Strength Indicator - Very Weak
# Test Name: Test_Password_Strength_Very_Weak
# Purpose: To verify that the password strength indicator shows 'Very Weak' when 8 identical characters are entered.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter '00000000' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Very Weak' message.
@pytest.mark.group2
def test_case_6_2_Verify_Password_Strength_Indicator_Very_Weak(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_password_field()
    app.orangeHrm.popUp.input_in_pass_field("00000000")
    app.orangeHrm.popUp.click_on_empty()
    app.assert_that(app.orangeHrm.popUp.get_pass_strength_message()).is_equal_to("Very Weak")

# Test Case 6.3: Verify Password Strength Indicator - Weak
# Test Name: Test_Password_Strength_Weak
# Purpose: To verify that the password strength indicator shows 'Weak' when the password includes two uppercase letters.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'AA000000' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Weak' message.
@pytest.mark.group2
def test_case_6_3_Verify_Password_Strength_Indicator_Weak(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_password_field()
    app.orangeHrm.popUp.input_in_pass_field("AA00000A")
    app.orangeHrm.popUp.click_on_empty()
    app.assert_that(app.orangeHrm.popUp.get_pass_strength_message()).is_equal_to("Weak")

# Test Case 6.4: Verify Password Strength Indicator - Better
# Test Name: Test_Password_Strength_Better
# Purpose: To verify that the password strength indicator shows 'Better' when the password includes three uppercase letters.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'AAA00000' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Better' message.
@pytest.mark.group2
def test_case_6_4_Verify_Password_Strength_Indicator_Better(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_password_field()
    app.orangeHrm.popUp.input_in_pass_field("AA0000AA")
    app.orangeHrm.popUp.click_on_empty()
    app.assert_that(app.orangeHrm.popUp.get_pass_strength_message()).is_equal_to("Better")

# Test Case 6.5: Verify Password Strength Indicator - Strongest
# Test Name: Test_Password_Strength_Strongest
# Purpose: To verify that the password strength indicator shows 'Strongest' when the password includes a mix of uppercase letters, lowercase letters, numbers, and special symbols.
# Steps:
# 1. Follow steps 1-4 from Test Case 6.
# 2. Enter 'Aa1!Aa1!' in the 'Password' field.
# 3. Observe the password strength indicator.
# Expected Result:
# The password strength indicator should display a 'Strongest' message.
@pytest.mark.group2
def test_case_6_5_Verify_Password_Strength_Indicator_Strongest(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_add_user()
    app.orangeHrm.popUp.click_on_password_field()
    app.orangeHrm.popUp.input_in_pass_field("Al1e?m-sd2#B.!Nn2!Zz3!")
    app.orangeHrm.popUp.click_on_empty()
    app.assert_that(app.orangeHrm.popUp.get_pass_strength_message()).is_equal_to("Strongest")