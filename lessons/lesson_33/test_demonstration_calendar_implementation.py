import time

def test_demonstration_calendar_implementation(app):
    app.orangeHrm.open_application_and_login()
    # app.orangeHrm.sideMenu.click_on_side_menu_button("Leave")
    # app.orangeHrm.leave.calendar.set_date('12-12-2005')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.calendar.set_date('12-12-2005')
    time.sleep(3)