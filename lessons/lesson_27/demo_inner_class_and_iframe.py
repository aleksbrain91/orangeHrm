def test_case_demo(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.orangeHrm.sideMenu.click_on_side_menu_button('Training')
    app.orangeHrm.training.click_on_filter_button()
    app.orangeHrm.popUp.training_filter.set_title("test")