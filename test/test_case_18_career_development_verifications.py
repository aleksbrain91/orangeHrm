# Test Case 1: Individual Development Plans(IDP) Table
# Description: Verify that IDP table are displayed correctly.
# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Career Develpoment section
# 4. Verify that the IDP table is displayed with correct columns
# Expected Result: The IDP table is displayed with columns: checkbox, Employee Id, Employee, IDP Name, Coach, Initiated On, Closed On, and Status.
import time

expected_table_columns = ['more_horizSelect AllConfigure', 'Employee ID', 'Employee   arrow_upward', 'IDP Name', 'Coach', 'Initiated On', 'Closed On', 'Status']
def test_case_1_verify_individual_development_plans_idp(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Career Development")
    app.orangeHrm.careerDevelopment.wait_for_table_loading()
    app.assert_that(app.orangeHrm.careerDevelopment.get_table_headers_names()).is_equal_to(expected_table_columns)

# Test Case 2: Verifying the functionality of IDP checkboxes
# Description: Verify that checkboxes can be checked and unchecked.
# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Career Develpoment section
# 4. Check all checkboxes
# 5. Verify that all checkboxes are checked
# 6. Uncheck all checkboxes
# 7. Verify that all checkboxes are unchecked
# 8. Click on 3 dots in first table header and choose "Select All"
# 9. Verify that all checkboxes are checked
# 10. Click on 3 dots in first table header and choose "Deselect All"
# 11. Verify that all checkboxes are unchecked
# Expected Result: User could check and uncheck any checkbox using "Select All" and manually.

checkbox_empty_status_trigger = "ng-empty"
checkbox_not_empty_status_trigger = "ng-not-empty"
def test_case_2_verifying_the_functionality_of_idp_checkboxes(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Career Development")
    app.orangeHrm.careerDevelopment.wait_for_table_loading()
    app.orangeHrm.careerDevelopment.table.click_all_in_column("checkboxes")
    manually_checked = app.orangeHrm.careerDevelopment.get_checkboxes_status()
    for status in manually_checked:
        app.assert_that(status).does_not_contain(checkbox_empty_status_trigger)
    app.orangeHrm.careerDevelopment.table.click_all_in_column("checkboxes")
    manually_unchecked = app.orangeHrm.careerDevelopment.get_checkboxes_status()
    for status in manually_unchecked:
        app.assert_that(status).does_not_contain(checkbox_not_empty_status_trigger)
    app.orangeHrm.careerDevelopment.click_on_first_table_header()
    app.orangeHrm.careerDevelopment.click_on_select_all_option()
    auto_checked = app.orangeHrm.careerDevelopment.get_checkboxes_status()
    for status in auto_checked:
        app.assert_that(status).does_not_contain(checkbox_empty_status_trigger)
    app.orangeHrm.careerDevelopment.click_on_first_table_header()
    app.orangeHrm.careerDevelopment.click_on_deselect_all_option()
    auto_unchecked = app.orangeHrm.careerDevelopment.get_checkboxes_status()
    for status in auto_unchecked:
        app.assert_that(status).does_not_contain(checkbox_not_empty_status_trigger)

# Test Case 3: Adding and removing IDP
# Description: Verify that new IDP can be added and deleted correctly.
# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Career Develpoment section
# 4. Click on "Add" new IDP button
# 5. Type employee name in "Employee" field
# 6. Verify that "IDP Name" and "Coach" fields is autocompleted
# 7. Click "Save" button
# 8. Verify that IDP table contains newly added employee
# 9. Delete added employee
# Expected Result: New IDP for employee successfully added and removed.

employee = "Alexander Konovalov"
def test_case_3_verifying_adding_and_removing_idp(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Career Development")
    app.orangeHrm.careerDevelopment.wait_for_table_loading()
    app.orangeHrm.careerDevelopment.click_on_add_button()
    app.assert_that(app.orangeHrm.careerDevelopment.get_add_idp_header_text()).is_equal_to("Add Individual Development Plan")
    app.orangeHrm.careerDevelopment.set_employee_name(employee)
    app.assert_that(app.orangeHrm.careerDevelopment.get_idp_name_input_field_text()).is_equal_to("Individual Development Plan - Alexander Konovalov")
    app.assert_that(app.orangeHrm.careerDevelopment.get_coach_input_field_text()).is_equal_to("Prem Preet")
    app.orangeHrm.careerDevelopment.click_save_button()
    app.assert_that(app.orangeHrm.careerDevelopment.get_success_message_text()).is_equal_to("Successfully Saved")
    app.orangeHrm.careerDevelopment.click_back_button()
    app.orangeHrm.careerDevelopment.wait_for_table_loading()
    app.assert_that(app.orangeHrm.careerDevelopment.table.get_column_data('employee_name')).contains(employee)
    app.orangeHrm.careerDevelopment.find_and_click_added_employee_checkbox(employee)
    app.orangeHrm.careerDevelopment.click_on_first_table_header()
    app.orangeHrm.careerDevelopment.click_delete_selected_dropdown_option()
    app.orangeHrm.careerDevelopment.click_confirm_delete()
    app.assert_that(app.orangeHrm.careerDevelopment.get_success_message_text()).is_equal_to("Successfully Deleted")

# Test Case 4: Filtering by Sub Unit
# Description: Verify that new IDP can be filtered by Sub Unit.
# Test Steps:
# 1. Open the application
# 2. Login
# 3. Go to Career Develpoment section
# 4. Click on "Filter" button
# 5. Click on "Sub Unit" input field
# 6. Choose role from dropdown list
# 7. Click "Search" button
# 8. Verify that IDP table changed
# 9. Click on any employee in "Employee" column
# 10.Verify employee's role in the top right corner of the page
# Expected Result: The employee's role should correspond or to be related to the role selected in the "Sub Unit" filter field.

def test_case_4_filtering_by_sub_unit(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Career Development")
    app.orangeHrm.careerDevelopment.wait_for_table_loading()
    emp_before_filter = app.orangeHrm.careerDevelopment.table.get_column_data("employee_name")
    app.orangeHrm.careerDevelopment.click_on_filter_button()
    app.assert_that(app.orangeHrm.popUp.careerDevelopmentFilter.get_popup_header_text()).is_equal_to("Filter Individual Development Plans By")
    app.orangeHrm.popUp.careerDevelopmentFilter.select_from_subunit_dropdown("Quality assurance (QA)")
    app.orangeHrm.popUp.careerDevelopmentFilter.click_on_search_button()
    time.sleep(1)
    app.assert_that(app.orangeHrm.careerDevelopment.table.get_column_data("employee_name")).is_not_equal_to(emp_before_filter)
    app.orangeHrm.careerDevelopment.table.click_on_cell(0, "employee_name")
    app.assert_that(app.orangeHrm.careerDevelopment.get_employee_job_title()).is_equal_to("Senior QA Engineer")