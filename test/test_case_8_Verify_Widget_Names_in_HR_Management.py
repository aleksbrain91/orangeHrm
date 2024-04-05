# Test Case 8: Verify Retrieval of Widget Names in HR Management Component
# Test Name: Test_Get_Widget_Names_HR_Management
# Purpose: To verify that the HR Management component is created and the method to retrieve all widget names functions as expected.
# Precondition: The user has created a new component in the project named 'HRManagement'.
# Steps:
# 1. Open the browser and navigate to the OrangeHRM URL.
# 2. Log in to the application with valid credentials.
# 3. Navigate to the 'HR Management' component from the main menu.
# 4. Click on the 'Home' button
# 5. Execute the 'get_widget_names' method to retrieve the list of widget names.
# 6. Verify that the list of retrieved widget names matches the expected list.
# Expected Result:
# The 'get_widget_names' method should return an accurate list of widget names that are present within the HR Management component.
import time


def test_case_8_verify_retrieval_of_widget_names_in_employee_management_component(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    # I'm pretty sure that the next step is not necessary, because we're already on actual page
    # app.orangeHrm.employeeManagement.click_on_home_button()
    app.assert_that(app.orangeHrm.employeeManagement.get_widget_names()).is_equal_to(['My Actions', 'Quick Access', 'Time At Work', 'Employees on Leave Today', 'Latest News', 'Latest Documents', 'Performance Quick Feedback', "Current Year's Leave Taken by Department", 'Buzz Latest Posts', 'Leave Taken on Each Day of the Week Over Time', 'Leave Scheduled in Each Month', 'Leave Taken on Each Calendar Month Over the Years', 'Headcount by Location', 'Annual Basic Payment by Location'])