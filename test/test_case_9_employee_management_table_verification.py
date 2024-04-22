employee_id_column_list = ['0123', '1061', '1055', '0125', '1058', '1002', '1072', '1080', '1144', '1149', '1122', '1139', '1071', '0119','1117', '1032', '1158', '1104', '1102', '1171', '1083', '1110', '1039', '1093', '1165', '0129', '1121', '201','1123', '1038', '1127', '1015', '1142', '1135', '1068', '1081', '1118', '1059', '0120', '0203', '1097', '1146','1050', '1103', '1092', '1074', '1035', '1141', '1163', '1006']
name_column_column_list = ['Mazie Abraham', 'Odis Adalwin', 'Brody Alan', 'Mary Alcala', 'Peter Anderson', 'Leah Andrews', 'Tanya Arva', 'Amadi Aswad', 'Lukas Bauer', 'Johanna Becker', 'Brad Bellic', 'Léa Bernard', 'Cece Bonaparte', 'Caitlyn Bonwick', 'Brian Butler', 'Steven Caldwell', 'Ayana Campbell', 'Charlie Carter', 'Chang Cheng', 'Mei Ling Chua', 'Chenzira Chuki', 'Paul Collings', 'Christoper Cooper', 'Robert Craig', 'Maria Cruz', 'Alannah Daglish', 'Andrew Daley', 'Anthony Davies', 'Paul Davis', 'Lincoln Davis', 'Lisa De Zousa', 'Carla Donovan', 'Laura Dubois', 'Camille Dubois', 'Alice Duval', 'Ehioze Ebo', 'Ralph Edwards', 'Amy Elliot', 'Stephan Fassbinder', 'David Fernandez', 'Tian Fieur', 'Maximilian Fischer', 'Jenny Fisher', 'Fabienne Gabor', 'Mason Gabriel', 'Goutam Ganesh', 'Martín García', 'Marion Girard', 'Mateo Gonzalez', 'Fiona Grace']
job_title_column_list = ['Marketing Executive', 'Vice President - Human Resources', 'Senior Manager Technical Support', 'Production Co-ordinator', 'CRO', 'CCO', 'Software Architect', 'Senior Software Development Manager', 'Regional HR Manager', 'Customer Support Executive', 'Software Engineer', 'Local Marketing Manager', 'Talent Acquisition Manager', 'HR Executive', 'Regional Sales Director', 'Sales Manager', 'Junior QA Engineer', 'Principal Software Engineer', 'Senior Software Development Manager', 'Marketing Executive', 'Lead QA Engineer', 'Local Marketing Manager', 'Comptroller', 'Regional Sales Manager', 'Senior QA Engineer', 'Associate Support Engineer', 'IT Technical Support', 'Project Manager', 'Software Engineer', 'Senior Manager- Digital Marketing', 'Sales Executive', 'CEO', 'Marketing Executive', 'Senior Manager- Regional Sales', 'Senior Sales Manager', 'Engineer Manager', 'Art Director', 'Assistant Manager - HR', 'Production Co-ordinator', 'CFO', 'Regional HR Manager', 'Senior Customer Success Manager', 'Software Engineer', 'Assistant Manager - HR', 'Sales Executive', 'Principal Software Engineer', 'Technical Support Engineer', 'SEO Specialist', 'Technical Support Engineer', 'Senior Lead Technical Support Engineer']
employment_status_column_list = ['Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Probation', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Probation', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Probation', 'Full-Time Permanent', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Probation', 'Full-Time Permanent', '', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Contract', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Part-Time Contract', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Permanent', 'Full-Time Probation', 'Full-Time Permanent']


def test_case_9_employee_management_table_verification(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
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
    app.assert_that(app.orangeHrm.employeeManagement.table[1]['employee_id']).is_equal_to('1061')
    app.assert_that(app.orangeHrm.employeeManagement.table[0]['name']).is_equal_to('Mazie Abraham')
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
def test_case_9_1_employee_management_table_filtering(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.orangeHrm.employeeManagement.click_on_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_filter_employee_table_header()).is_equal_to("Filter Employees By")
    app.orangeHrm.popUp.set_employee_filter_table_employment_status_dropdown("Full-Time Contract")
    app.orangeHrm.popUp.set_employee_filter_table_location_dropdown("Canada")
    app.orangeHrm.popUp.click_filter_search_button()
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

def test_case_9_2_employee_management_table_location_change(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.orangeHrm.employeeManagement.click_on_filter_button()
    app.assert_that(app.orangeHrm.popUp.get_filter_employee_table_header()).is_equal_to("Filter Employees By")
    app.orangeHrm.popUp.set_employee_filter_table_employment_status_dropdown("Full-Time Contract")
    app.orangeHrm.popUp.set_employee_filter_table_location_dropdown("Canada")
    app.orangeHrm.popUp.click_filter_search_button()
    app.orangeHrm.employeeManagement.wait_for_table_reload()
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('employment_status'))).is_equal_to(
        sorted(expected_list_for_emp_status))
    app.assert_that(sorted(app.orangeHrm.employeeManagement.table.get_column_data('locations'))).is_equal_to(
        sorted(expected_list_for_emp_locations))
    app.orangeHrm.employeeManagement.click_on_filter_button()
    app.orangeHrm.popUp.set_employee_filter_table_location_dropdown("Australia")
    app.orangeHrm.popUp.click_filter_search_button()
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