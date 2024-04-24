import pytest


@pytest.mark.group1
def test_case_1_login_to_the_application(app):
    app.orangeHrm.open_application_and_login()
