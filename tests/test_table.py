

import pytest

from base.base_test import BaseTest
from pages.login_page import loginpage
from pages.table_page import TablePage


class TestTable(BaseTest):

    @pytest.mark.sanity
    def test_table(self):
        obj = loginpage(self.driver)
        obj.login("student", "Password123")

        tableObj = TablePage(self.driver)
        assert tableObj.verifyCourseTable() == True

    @pytest.mark.sanity
    def test_table_level(self):
        obj = loginpage(self.driver)
        obj.login("student", "Password123")

        tableObj = TablePage(self.driver)
        assert tableObj.verify_course_begineer() == True

           
    @pytest.mark.sanity
    def test_table_enrollment(self):
        obj = loginpage(self.driver)
        obj.login("student", "Password123")

        tableObj = TablePage(self.driver)
        assert tableObj.Check_Minenrollments() == True
