def test_lesson_18_table_values_displaying(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.wait_for_table()
    a = app.orangeHrm.hrAdministration.table.get_column_data('user_name')
    b = app.orangeHrm.hrAdministration.table.get_column_data('user_role')
    c = app.orangeHrm.hrAdministration.table[1]['user_name']
    d = app.orangeHrm.hrAdministration.table[6]['user_role']
    app.orangeHrm.hrAdministration.table[4].click_column_button('check_box')
    app.orangeHrm.hrAdministration.table.click_all_in_column('check_box')
