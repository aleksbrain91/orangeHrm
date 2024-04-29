def test_logging(app):
    try:
        print("Opening URL...")
        app.orangeHrm.openUrl()
        print("Logging into the application...")
        app.orangeHrm.login_to_the_application()
        print("Asserting header text...")
        assert app.orangeHrm.get_header_text() == 'Employee Management'
        print("Clicking on HR Administration side menu button...")
        app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
        print("Clicking on filter button...")
        app.orangeHrm.hrAdministration.click_on_filter()
        print("Clicking on filter reset button...")
        app.orangeHrm.popUp.click_on_filter_reset_button()
        print("Waiting for filter pop-up to stop being displayed...")
        app.orangeHrm.popUp.wait_filter_pop_up_stop_displayed()
        print("Clicking on filter button again...")
        app.orangeHrm.hrAdministration.click_on_filter()
        print("Setting username...")
        app.orangeHrm.popUp.set_username("Admin")
        print("Setting employee name...")
        app.orangeHrm.popUp.set_employee_name("wer")
        print("Setting ESS role input dropdown...")
        app.orangeHrm.popUp.set_ess_role_input_dropdown("Default ESS")
        print("Setting admin role input dropdown...")
        app.orangeHrm.popUp.set_admin_role_input_dropdown("Leave Admin")
        print("Setting supervisor role dropdown...")
        app.orangeHrm.popUp.set_supervisor_role_dropdown("Default Supervisor")
        print("Setting status input dropdown...")
        app.orangeHrm.popUp.set_status_input_dropdown("Disabled")
        print("Setting location input dropdown...")
        app.orangeHrm.popUp.set_location_input_dropdown("Australia")
        print("Clicking on filter cancel button...")
        app.orangeHrm.popUp.click_on_filter_cancel_button()
        print("Waiting for filter pop-up to stop being displayed...")
        app.orangeHrm.popUp.wait_filter_pop_up_stop_displayed()
        print("Clicking on filter button again...")
        app.orangeHrm.hrAdministration.click_on_filter()
        print("Asserting ESS role selected dropdown value...")
        assert app.orangeHrm.popUp.get_ess_role_selected_dropdown_value() == "Default ESS"
        print("Asserting admin role selected dropdown value...")
        assert app.orangeHrm.popUp.get_admin_role_selected_dropdown_value() == "Leave Admin"
        print("Asserting supervisor role selected dropdown value...")
        assert app.orangeHrm.popUp.get_supervisor_role_selected_dropdown_value() == "Default Supervisor"
        print("Asserting status selected dropdown value...")
        assert app.orangeHrm.popUp.get_status_selected_dropdown_value() == "Disabled"
        print("Asserting location selected dropdown value...")
        assert "Australia" in app.orangeHrm.popUp.get_location_selected_dropdown_value()
    except Exception as e:
        print("An error occurred:", e)
        # Fail the test explicitly
        assert False, f"Test failed due to exception: {e}"
