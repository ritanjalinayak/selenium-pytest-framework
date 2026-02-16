
import pytest
from pages.login_page import loginpage
from testdata.login_data import login_regression_data

@pytest.mark.regression
@pytest.mark.parametrize("username,password,expected", login_regression_data)

# Setup fixture /
def test_login_regression(initial_setup, username, password, expected):

    driver = initial_setup
    login = loginpage(driver)

    login.login(username, password)

    # Valid login case
    if expected == "success":
        assert "Logged In Successfully" in login.get_success_msg()

    # Invalid cases
    else:
        assert expected in login.get_error_msg()







  