
import pytest
from base.base_test import BaseTest
from pages.login_page import loginpage
from testdata.login_data import login_regression_data


class TestLogin(BaseTest):    

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password,expected", login_regression_data)
    def test_login_regression(self, username, password, expected):

        login = loginpage(self.driver)
        login.login(username, password)

        # # Valid login case
        if expected == "success":
            assert "Logged In Successfully" in login.get_success_msg()

        # # Invalid cases
        else:
            assert expected in login.get_error_msg()







  