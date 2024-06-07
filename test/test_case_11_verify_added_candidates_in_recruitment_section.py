import os

from helpers.utils import Utils
# Test Case: Verify Added Candidates in Recruitment Section

# Step 1: - Open the application
# Step 2: - Go to Recruitment section from the side menu
# Step 3: - Click on 'Add Candidate' button
# Step 4: - Fill in all required fields: First Name, Last Name, and Email
# Step 5: - Upload the resume
# Step 6: - Click on 'Save' button
# Step 7: - Find the candidate using the search field
# Step 8: - Verify if the candidate is displayed in the table
# Step 9: - Click on the candidate's name from the table
# Step 10: - In the new opened tab, verify the previously selected fields (First Name, Last Name, Email, and Resume) during creation
first_name = Utils.generate_random_string(length=5)
last_name = Utils.generate_random_string(length=5)
email = Utils.generate_random_email(length=5)
def test_case_verify_added_candidates_in_recruitment_section(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.click_on_add_candidate_button()
    app.orangeHrm.popUp.recruitment_add_candidate.wait_for_add_candidate_window_loading()
    app.orangeHrm.popUp.recruitment_add_candidate.set_first_name(first_name)
    app.orangeHrm.popUp.recruitment_add_candidate.set_last_name(last_name)
    app.orangeHrm.popUp.recruitment_add_candidate.set_email(email)
    resume_path = os.path.join(Utils.get_project_root(), "files", "test_upload.txt")  # Adjust the file name as needed
    app.orangeHrm.popUp.recruitment_add_candidate.upload_resume(resume_path)
    app.orangeHrm.popUp.recruitment_add_candidate.click_on_save_button()
    app.orangeHrm.popUp.recruitment_add_candidate.wait_for_add_candidate_window_loading()
    app.assert_that(app.orangeHrm.recruitmentAts.get_action_message_text()).is_equal_to("Successfully Saved")
    app.orangeHrm.recruitmentAts.set_search(first_name)
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['name']).is_equal_to(first_name + " " + last_name)
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['email']).is_equal_to(email)