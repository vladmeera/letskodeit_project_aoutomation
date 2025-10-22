"""
@package base

Base page class implementation
It implements methods which are common to all pages throughout the application

This class needs to be inherited by all page classes
This should not be used by creating object instances

Example:
    class LoginPage(BasePage):
"""

from traceback import print_stack

from base.selenium_driver import SeleniumDriver
from utilities.util import Util


class BasePage(SeleniumDriver):
    def __init__(self, driver):
        """
        Inits BasePage class

        :return None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, title_to_verify) -> bool:
        """
        Verify page title

        :param title_to_verify: Title on the page that needs to be verified
        """

        try:
            actual_title = self.get_title()
            if actual_title is not None:
                return self.util.verify_text_contains(actual_title, title_to_verify)
            else:
                return False
        except Exception as e:
            self.log.error(f"Error occurred - {e}")
            print_stack()
            return False
