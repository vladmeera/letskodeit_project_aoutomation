from pages.home.login_page import LoginPage
from unittest import TestCase
from inspect import currentframe
import pytest
from utilities.test_status import StatusOfTest
from utilities import custom_logger as cl


@pytest.mark.usefixtures("one_time_setup", "setup")
class LoginTest(TestCase):

    log = cl.custom_logger()

    @pytest.fixture(autouse=True)
    def before_each(self, one_time_setup):
        self.login_page = LoginPage(self.driver)
        self.status_test = StatusOfTest(self.driver)



    # @pytest.mark.run(order=2)
    def test_02_valid_login(self):
        """
        Test name - valid login (positive)

        Valid email

        Valid password
        """
        self.log.info(f"   -------> Running {currentframe().f_code.co_name} test method <-------")
        self.log.info(f"---------------------------------------------------------------------")

        self.login_page.successful_login()

        result1 = self.login_page.verify_title_my_courses()
        self.status_test.mark(1, 3, result1,
                              "Title matches the original",
                              "Title does not match the original")

        result2 = self.login_page.verify_login_successful()
        self.status_test.mark(2, 3,
                            result2,
                            "Login is successful, my courses were on the page",
                            "Login was not successful, my courses were not presented on the page")

        result3 = self.login_page.verify_login_successful_avatar()
        self.status_test.mark_final(3, 3,
                                    "test_02_valid_login",
                                    result3,
                                    "Login was successful, avatar was presented on the page",
                                    "Login was not successful, avatar was not presented on the page")

    # @pytest.mark.run(order=1)
    def test_01_invalid_login_no_pass(self):
        """
        Invalid login - negative

        valid email

        no password
        """
        self.log.info(f"   -------> Running {currentframe().f_code.co_name} test method <-------")
        self.log.info(f"---------------------------------------------------------------------")

        self.login_page.unsuccessful_login_no_pass()

        result = self.login_page.verify_login_unsuccessful()
        self.status_test.mark_final(1, 1, "test_01_invalid_login_no_pass"
                                    ,result,
                                    "Error message is displayed",
                                    "Error message is not displayed")
