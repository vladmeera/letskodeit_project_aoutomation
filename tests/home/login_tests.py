from pages.home.login_page import LoginPage
from unittest import TestCase
from inspect import currentframe
import pytest
from utilities.test_status import TestStatus


@pytest.mark.usefixtures("one_time_setup", "setup")
class LoginTest(TestCase):

    @pytest.fixture(autouse=True)
    def before_each(self, one_time_setup):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    #Credentials
    _email = 'va3zdkh68@mozmail.com'
    _password = '"%+eH3>@w8nPp,'


    @pytest.mark.run(order=2)
    def test_valid_login(self) -> None:
        print(f"Run {currentframe().f_code.co_name} test method")

        self.lp.login(
            email="{}".format(self._email),
            password="{}".format(self._password))
        result1 = self.lp.verify_title()
        self.ts.mark(result1, "Title is not matching")

        result2 = self.lp.verify_login_successful()
        self.ts.mark_final("test_valid_login" ,result2, "Login is not successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self) -> None:

        print(f"Run {currentframe().f_code.co_name} test method")

        self.lp.invalid_login(
            email="{}".format(self._email))

        result = self.lp.verify_login_unsuccessful()
        self.ts.mark_final("test_invalid_login" ,result, "Login is successful | The wrong message is displayed/Not displayed at all")
