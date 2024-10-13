"""
@package base

Base page class implementation
It implements methods which are common to all pages throughout the application

This class needs to be inherited by all page classes
This should not be used by creating object instances

Example:
    class LoginPage(BasePage):
"""

from selenium.common import WebDriverException

from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util

class BasePage(SeleniumDriver):

    def __init__(self, driver) -> None:
        """
        Inits BasePage class

        :return None
        """
        super(BasePage, self).__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, title_to_verify: str) -> bool:
        """
        Verify page title

        :param title_to_verify: Title on the page that needs to be verified
        """

        try:
            actual_title: str = self.get_title()
            return self.util.verify_text_contains(actual_title, title_to_verify)
        except AttributeError as e:
            self.log.error(f"| ATTRIBUTE ERROR | {e}")
            print_stack()
        except TypeError as e:
            self.log.error(f"| TYPE ERROR | {e}")
            print_stack()
        except WebDriverException as e:
            self.log.error(f"| WEB DRIVER ERROR | {e}")
            print_stack()
        except Exception as e:
            self.log.error(f"| GENERIC ERROR | {e}")
            print_stack()