from pages.home.login_page import LoginPage
from unittest import TestCase
from inspect import currentframe
import pytest
from utilities.test_status import StatusOfTest
from utilities import custom_logger as cl
import os


@pytest.mark.usefixtures("one_time_setup", "setup")
class LoginTest(TestCase):

    cl = cl.custom_logger()

    @pytest.fixture(autouse=True)
    def before_each(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        self.ts = StatusOfTest(self.driver)

    #Credentials
    _credentials_list = {"email_correct": "mirgorodvld@gmail.com", "password_correct": "xnDi!1Bxi09bU",
                        "email_incorrect": "vld_123456@gmail.com", "password_incorrect": "123456"}
    # _email = "mirgorodvld@gmail.com"
    # _password = "xnDi!1Bxi09bU"


    @pytest.mark.run(order=2)
    def test_valid_login(self) -> None:
        """
        Happy path
        valid login
        valid password
        """
        self.cl.info(f"Run {currentframe().f_code.co_name} test method")

        self.lp.login(
            email="{}".format(self._credentials_list["email_incorrect"]),
            password="{}".format(self._credentials_list["password_correct"]))
        result1 = self.lp.verify_title(0)
        self.ts.mark(result1, "Title is not matching")

        result2 = self.lp.verify_login_successful()
        self.ts.mark_final("test_valid_login" ,result2, "Login is not successful")

    @pytest.mark.run(order=1)
    def test_invalid_login_pass(self) -> None:
        """
        Invalid login
        valid login
        no password
        """

        self.cl.info(f"Run {currentframe().f_code.co_name} test method")

        self.lp.invalid_login(
            email="{}".format(self._credentials_list["email_correct"]))

        result = self.lp.verify_login_unsuccessful()
        self.ts.mark_final("test_invalid_login" ,result, "Error message is not displayed")
