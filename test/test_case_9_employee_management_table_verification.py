import pytest
employee_id_column_list = ['0202', '0203', '1006', '1007', '1008', '1009', '1014', '1015', '1019', '1020', '1021', '1023', '1031', '1032', '1038', '1039', '1040', '1041', '1052', '1055', '1056', '1058', '1084', '1089', '1090', '1092', '1095', '1113', '1114', '1120', '1121', '1122', '1123', '1124', '1126', '1127', '136', '199']
name_column_column_list = ['Aaliyah Haq', 'Aaron Hamilton', 'Andrew Daley', 'Brad Bellic', 'Brody Alan', 'Carla Donovan', 'Christoper Cooper', 'Christopher Morgan', 'David Fernandez', 'David Grossi', 'Dereck Morris', 'Dorothy Wilkins', 'Fiona Grace', 'Frank Williams', 'Grant Mason', 'Gretchen Morgan', 'Jacob Oram', 'Jacqueline Wagner', 'John Mathews', 'Jordan Amester Mathews', 'Julian Taylor', 'Kai Keegan', 'Kenneth Mathews', 'Lien Ko', 'Lincoln Davis', 'Lisa De Zousa', 'Luke Wright', 'Maggie Manning', 'Mark Sallinger', 'Mason Gabriel', 'Melodie Leonie', 'Muhammad Khan', 'Nicky Silverstone', 'Paul Davis', 'Peter Anderson', 'Rebecca Harmony', 'Steven Caldwell', 'Xandra Xavier']
job_title_column_list = ['Assistant Manager - HR', 'CEO', 'CFO', 'CHRO', 'CRO', 'Comptroller', 'Finance Manager', 'Finance Manager', 'IT Executive', 'IT Technical Support', 'Principal Software Engineer', 'Regional HR Manager', 'Regional Marketing Manager', 'Regional Sales Manager', 'Regional Sales Manager', 'SEO Specialist', 'Sales Executive', 'Sales Executive', 'Sales Executive', 'Sales Executive', 'Sales Executive', 'Sales Manager', 'Senior Front End Developer', 'Senior Lead QA Engineer', 'Senior Lead QA Engineer', 'Senior Lead QA Engineer', 'Senior Lead Technical Support Engineer', 'Senior Manager Technical Support', 'Senior Manager- Digital Marketing', 'Senior Production Manager', 'Senior Sales Executive', 'Senior Sales Executive', 'Senior Sales Executive', 'Senior Technical Support Engineer', 'Senior Vice President - Production', 'Senior Web Developer', 'Software Engineer', 'Software Engineer']
employment_status_column_list = ['', 'Full-Time Contract', 'Full-Time Contract', 'Full-Time Contract', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Probation']

@pytest.mark.group3
def test_case_9_employee_management_table_verification(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('employee_id'))).is_equal_to(
        sorted(employee_id_column_list))
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('name'))).is_equal_to(
        sorted(name_column_column_list))
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('job_title'))).is_equal_to(
        sorted(job_title_column_list))
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('employment_status'))).is_equal_to(
        sorted(employment_status_column_list))
    app.assert_that(app.orangeHrm.employeeManagement.table[1]['employee_id']).is_equal_to('1058')
    app.assert_that(app.orangeHrm.employeeManagement.table[0]['name']).is_equal_to('Brody Alan')
    app.assert_that(app.orangeHrm.employeeManagement.table[4]['employment_status']).is_equal_to('Full-Time Permanent')

    # 1 Create a new object of the table class inside the employee management component (based on the example from hr_administration).
    # 2 Find selectors: For list of rows and list of column elements (Employee Id, Name, Job Title, Employment Status).
    # 3 Get list of elements from each defined column and assert them with the expected one.
    # 4 Get second element from the 'Employee Id' column and assert it with the expected one.
    # 5 Get first element from the 'Name' column and assert it with the expected one.
    # 6 Get fifth element from the 'Employment Status' column and assert it with the expected one.
expected_list_for_emp_status = ['Full-Time Contract', 'Full-Time Contract', 'Full-Time Contract', 'Full-Time Contract']
expected_list_for_emp_locations = ['Canadian Development Center', 'Canadian Development Center', 'Canadian Development Center', 'Canadian Development Center']
expected_list_for_emp_locations2 = ['Australia office', 'Australia office', 'Australia office', 'Australia office']
@pytest.mark.group3
def test_case_9_1_employee_management_table_filtering(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.orangeHrm.employeeManagement.click_on_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_filter_employee_table_header()).is_equal_to("Filter Employees By")
    app.orangeHrm.popUp.set_employee_filter_table_employment_status_dropdown("Full-Time Contract")
    app.orangeHrm.popUp.set_employee_filter_table_location_dropdown("Canada")
    app.orangeHrm.popUp.click_on_filter_search_button()
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('employment_status'))).is_equal_to(
        sorted(expected_list_for_emp_status))
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('locations'))).is_equal_to(
        sorted(expected_list_for_emp_locations))


    #  Click on the filter button in the Employee Management section
    #  In the filter pop-up, set 'Employment Status' to 'Full-Time Contract'
    #  Set 'Location' to 'Canada'
    #  Click the search button
    #  Wait for the table to load (ensure the table is refreshed with the filter applied)
    #  Using the previously created table component, get list of users Names and Assert the list of users with the expected ones
    #  Get list of 'Employment Statuses' and assert it with the expected 'Full-Time Contract'
    #  Get list of 'Locations' for each listed user and assert it with the expected 'Canada'

@pytest.mark.group3
def test_case_9_2_employee_management_table_location_change(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.orangeHrm.employeeManagement.click_on_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_filter_employee_table_header()).is_equal_to("Filter Employees By")
    app.orangeHrm.popUp.set_employee_filter_table_employment_status_dropdown("Full-Time Contract")
    app.orangeHrm.popUp.set_employee_filter_table_location_dropdown("Canada")
    app.orangeHrm.popUp.click_on_filter_search_button()
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('employment_status'))).is_equal_to(
        sorted(expected_list_for_emp_status))
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('locations'))).is_equal_to(
        sorted(expected_list_for_emp_locations))
    app.orangeHrm.employeeManagement.click_on_filter_button()
    app.orangeHrm.popUp.set_employee_filter_table_location_dropdown("Australia")
    app.orangeHrm.popUp.click_on_filter_search_button()
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('employment_status'))).is_equal_to(
        sorted(expected_list_for_emp_status))
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('locations'))).is_equal_to(
        sorted(expected_list_for_emp_locations2))

    #  Click on the filter button in the Employee Management section
    #  In the filter pop-up, set 'Employment Status' to 'Full-Time Contract'
    #  Set 'Location' to 'Canada'
    #  Click the search button
    #  Wait for the table to load (ensure the table is refreshed with the filter applied)
    #  Using the previously created table component, get list of users and Assert the list of users with the expected ones
    #  Get list of 'Employment Statuses' and assert it with the expected 'Full-Time Contract'
    #  Get list of 'Locations' for each listed user and assert it with the expected 'Canada'

    #  Click on the filter button again in the Employee Management section
    #  Change 'Location' to 'Australia'
    #  Click the search button
    #  Wait for the table to load (ensure the table is refreshed with the new location)
    #  Using the previously created table component, get list of users and Assert the list of users with the expected ones
    #  Get list of 'Employment Statuses' and assert it with the expected 'Full-Time Contract'
    #  Get list of 'Locations' for each listed user and assert it with the expected 'Australia'