from inspect import currentframe
from unittest import TestCase

import pytest

from pages.home.login_page import LoginPage
from utilities import custom_logger as cl
from utilities.test_status import StatusOfTest


@pytest.mark.usefixtures("one_time_setup", "setup")
class LoginTest(TestCase):
    log = cl.custom_logger()

    @pytest.fixture(autouse=True)
    def before_each(self, one_time_setup):
        self.login_page = LoginPage(self.driver)
        self.status_test = StatusOfTest(self.driver)

    def test_02_valid_login(self):
        """
        Test name - valid login (positive)

        Valid email

        Valid password
        """
        self.log.info(f"Running {currentframe().f_code.co_name} test method")
        self.login_page.successful_login()

        result1 = self.login_page.verify_title_my_courses()
        self.status_test.mark(
            result1,
        )

        result2 = self.login_page.verify_login_successful()
        self.status_test.mark(
            result2,
        )

        result3 = self.login_page.verify_login_successful_avatar()
        self.status_test.mark_final(
            result3,
        )

    def test_01_invalid_login_no_pass(self):
        """
        Invalid login - negative

        valid email

        no password
        """
        self.log.info(f"Running {currentframe().f_code.co_name} test method")
        self.log.info(
            "-----------------------------------------------------------------"
        )

        self.login_page.unsuccessful_login_no_pass()

        result = self.login_page.verify_login_unsuccessful()
        self.status_test.mark_final(
            result,
        )
        self.login_page.delete_keys_email()
