from helpers.utils import Utils
from helpers.csv_helper import CSVHelper


# Step 1: - Open the application
# Step 2: - Login
# Step 3: - Go to Recruitment ATS section
# Step 4: - Filter candidates
# Step 5: - Open the filter and fill in the job title "Customer Support Specalist"
# Step 6: - Click on 'Search' button
# Step 7: - Click on 'Export to CSV' button
# Step 8: - Once CSV is exported, open it
# Step 9: - Verify that information from the table in the application corresponds to information in the exported CSV file
def test_case_13_verify_exported_candidate_information_from_recruitment_ats_section(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.click_on_filter_button()
    app.orangeHrm.popUp.recruitment_filter.wait_for_window_to_appear()
    app.orangeHrm.popUp.recruitment_filter.set_job_title("Customer Support Specalist")
    app.orangeHrm.popUp.recruitment_filter.click_on_search_button()
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    Utils.clear_download_directory()
    app.orangeHrm.recruitmentAts.export_to_csv()
    vacancy_names = CSVHelper.get_column_values('RecruitmentReport', 0, partial_name=True)
    candidate_names = CSVHelper.get_column_values('RecruitmentReport', 1, partial_name=True)
    emails = CSVHelper.get_column_values('RecruitmentReport', 5, partial_name=True)
    app.assert_that(app.orangeHrm.recruitmentAts.table.get_column_data('vacancy')).is_equal_to(vacancy_names)
    app.assert_that(app.orangeHrm.recruitmentAts.table.get_column_data('name')).is_equal_to(candidate_names)
    app.assert_that(app.orangeHrm.recruitmentAts.table.get_column_data('email')).is_equal_to(emails)

