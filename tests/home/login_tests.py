from pages.home.login_page import LoginPage
from selenium import webdriver
from unittest import TestCase
from inspect import currentframe
import pytest


@pytest.mark.usefixtures("one_time_setup", "setup")
class LoginTest(TestCase):

    @pytest.fixture(autouse=True)
    def before_each(self, one_time_setup):
        self.lp = LoginPage(self.driver)

    #Credentials
    _email = 'va3zdkh68@mozmail.com'
    _password = '"%+eH3>@w8nPp,'

    @pytest.mark.run(order=2)
    def test_valid_login(self) -> None:
        print(f"Run {currentframe().f_code.co_name} test method")

        self.lp.login(
            email="{}".format(self._email),
            password="{}".format(self._password))

        result = self.lp.verify_login_successful()
        assert result == True

    @pytest.mark.run(order=1)
    def test_invalid_login(self) -> None:

        print(f"Run {currentframe().f_code.co_name} test method")

        self.lp.login_invalid(
            email="{}".format(self._email))

        result = self.lp.verify_login_unsuccessful()
        assert result == True
