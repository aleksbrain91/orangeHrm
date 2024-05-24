from fixture.calendar import Calendar, CalendarType

# Test Case: Verify Recruitment ATS Table Based on Selected Date
# Step 1:Open the application
# Step 2:Login
# Step 3:Go to Recruitment ATS section
# Step 4:Click on 'Filter Candidates' button
# Step 5:Set the 'Date Applied From' field using the calendar with a valid date where records exist
# Step 6:Click on 'Search' button
# Step 7:Verify that table results correspond to that date

def test_case_16_verify_recruitment_ats_table_based_on_selected_date(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.click_on_filter_button()
    app.orangeHrm.popUp.recruitment_filter.wait_for_window_to_appear()
    app.orangeHrm.popUp.recruitment_filter.click_on_from_calendar_button()
    app.orangeHrm.popUp.recruitment_filter.calendar.set_date('10-03-2023')
    app.orangeHrm.popUp.recruitment_filter.click_on_search_button()
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.assert_that(app.orangeHrm.recruitmentAts.table.get_column_data('date_applied')).contains_only('2023-10-03')