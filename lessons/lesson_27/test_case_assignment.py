# Test Case: Verification of Added Course


# Step 1: - Open the application
# Step 2: - Click on 'Training' from the side menu
# Step 3: - Click on 'Add Course' button
# Step 4: - Add title to the course
# Step 5: - Add coordinator
# Step 6: - Click on 'Save' button
# Step 7: - Go to 'Courses'
# Step 8: - Click on 'Filter' button
# Step 9: - Add the title of the created course in the filter
# Step 10: - Click 'Search'
# Step 11: - Verify that the created course is displayed in the table

test_title = "Test-Test-Test"
def test_case_training_section_functionality(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Training")
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.training.click_on_add_course_button()
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.training.set_course_title(test_title)
    app.orangeHrm.training.set_course_coordinator("Brody")
    app.orangeHrm.training.click_on_save_button()
    app.assert_that(app.orangeHrm.training.get_save_confirmation_message_text()).is_equal_to("Successfully Updated")
    app.orangeHrm.training.click_on_go_to_courses_button()
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.training.click_on_filter_button()
    app.assert_that(app.orangeHrm.popUp.training_filter.get_filter_courses_header_text()).is_equal_to("Filter Courses")
    app.orangeHrm.popUp.training_filter.set_title(test_title)
    app.orangeHrm.popUp.click_on_filter_search_button()
    app.orangeHrm.training.wait_for_table_reload()
    app.assert_that(app.orangeHrm.training.table.get_column_data('title')).contains(test_title)


