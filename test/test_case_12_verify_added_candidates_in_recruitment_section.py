from helpers.api import Api
from helpers.utils import Utils

cand_1 = {
    "first_name": Utils.generate_random_string(8),
    "last_name": Utils.generate_random_string(8),
    "date_applied": Utils.generate_random_date(),
    "email": Utils.generate_random_email(length=8)
}
cand_2 = {
    "first_name": Utils.generate_random_string(8),
    "last_name": Utils.generate_random_string(8),
    "date_applied": Utils.generate_random_date(),
    "email": Utils.generate_random_email(length=8)
}
cand_3 = {
    "first_name": Utils.generate_random_string(8),
    "last_name": Utils.generate_random_string(8),
    "date_applied": Utils.generate_random_date(),
    "email": Utils.generate_random_email(length=8)
}

def test_case_verify_candidate_1_in_recruitment_ats_section(app):
    Api.add_candidate_recruitment_section(cand_1["first_name"], cand_1["last_name"], cand_1["date_applied"], cand_1["email"])
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.set_search(cand_1["first_name"])
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['name']).is_equal_to(cand_1["first_name"] + " " + cand_1["last_name"])
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['email']).is_equal_to(cand_1["email"])
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['date_applied']).is_equal_to(cand_1["date_applied"])

def test_case_verify_candidate_2_in_recruitment_ats_section(app):
    Api.add_candidate_recruitment_section(cand_2["first_name"], cand_2["last_name"], cand_2["date_applied"], cand_2["email"])
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.set_search(cand_2["first_name"])
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['name']).is_equal_to(cand_2["first_name"] + " " + cand_2["last_name"])
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['email']).is_equal_to(cand_2["email"])
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['date_applied']).is_equal_to(cand_2["date_applied"])

def test_case_verify_candidate_3_in_recruitment_ats_section(app):
    Api.add_candidate_recruitment_section(cand_3["first_name"], cand_3["last_name"], cand_3["date_applied"], cand_3["email"])
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.set_search(cand_3["first_name"])
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['name']).is_equal_to(cand_3["first_name"] + " " + cand_3["last_name"])
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['email']).is_equal_to(cand_3["email"])
    app.assert_that(app.orangeHrm.recruitmentAts.table[0]['date_applied']).is_equal_to(cand_3["date_applied"])