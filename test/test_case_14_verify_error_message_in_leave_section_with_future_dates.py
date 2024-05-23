# Step 1: TODO - Open the application
# Step 2: TODO - Login
# Step 3: TODO - Go to Leave section
# Step 4: TODO - Select some date far, far away in the future from the calendar for the 'From' field
# Step 5: TODO - Select some day in the future, in the far, far away future for the 'To' field from the calendar
# Step 6: TODO - Click on 'Search' button
# Step 7: TODO - Verify that message 'No records found' is displayed
import time


def test_case_14_verify_error_message_in_leave_section_with_future_dates(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Leave")
    app.orangeHrm.leave.wait_for_page_load()
    app.orangeHrm.leave.click_from_calendar_button()
    app.orangeHrm.leave.calendar.set_date('12-12-2028')
    app.orangeHrm.leave.click_to_calendar_button()
    time.sleep(3)
    app.orangeHrm.leave.calendar.set_date('12-12-2030')
    app.orangeHrm.leave.click_on_search_button()
    app.assert_that(app.orangeHrm.leave.get_result_message_text()).is_equal_to("No Records Found")
    time.sleep(5)