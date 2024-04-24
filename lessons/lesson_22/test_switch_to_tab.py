import time  # test_lesson_22_switch_to_tab
    # Open the url and go to  "Elements", "Links" section
    # Click on 'Home' link
    # Switch to the new openned tab by its link
    # Werify that you are one the home page

def test_lesson_22_switch_to_tab(app):
    app.demonstrationAppDemoQa.openUrl()
    app.demonstrationAppDemoQa.go_to_side_menu_section("Elements", "Links")
    app.demonstrationAppDemoQa.click_home_button()
    app.step.switch_to_tab_by_url("https://demoqa.com/")
    app.assert_that(app.demonstrationAppDemoQa.get_page_banner()).is_equal_to("Selenium Online Training")
    app.assert_that(app.demonstrationAppDemoQa.verify_home_page()).is_equal_to(True)
    time.sleep(3)

