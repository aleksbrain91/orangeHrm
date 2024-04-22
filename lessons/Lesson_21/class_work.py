# 1 - Combine 3 lines related to Login into one method
# - go to orange_hrm.py file and find 'def open_application_and_login(self):' method
# - add more lines there:
# - app.orangeHrm.openUrl()
# - app.orangeHrm.login_to_the_application()
# - replace the original three login lines in all tests with the new method

# 2 - Create a method to set all values for HR Administration Pop-Up
# - go to pop_up.py file and find 'def set_hr_administration_drop_downs(self, user_name=None, employee_name=None, ess_role=None):' method
# - expand it with other set methods related to the pop up
# - app.orangeHrm.openUrl()
# - app.orangeHrm.login_to_the_application()
# - go to 'def test_case_7_3_Verify_Reset_Button_Functionality(app):'
# - replace all lines related to setting values with that one method

# 3 - Add @pytest markers to tests and execute tests with them
# - add @pytest.mark.group1, @pytest.mark.group2, or @pytest.mark.group3 to all your tests (you can choose tests to add markers)
# - practice with executing different groups of tests based on markers added
