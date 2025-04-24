"""
@package utilities

Util class implementation
All most common utilities should be implemented here

Example:
    name = self.util.get_unique_name()
"""
import time
import traceback
import random, string
import utilities.custom_logger as cl
import openpyxl
from logging import DEBUG


class Util(object):

    log = cl.custom_logger(DEBUG)

    def sleep(self, seconds, message = "") -> None:
        """
        Put the program to wait for the specified time
        """

        if message is not None:
            self.log.info(f"Wait :: {seconds} :: for :: {message}")
        try:
            time.sleep(seconds)
        except InterruptedError as e:
            self.log.error(f"| INTERRUPTED ERROR | {e}")
            traceback.print_stack()

    def get_alpha_numeric(self, length, char_type ="letters") -> str:
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should contain
            char_type: Type of characters string should contain, default is "letters"
            Provide lower/upper/digits/mix for different types
        """

        alpha_num = ''
        if char_type == "lower":
            case = string.ascii_lowercase
        elif char_type == "upper":
            case = string.ascii_uppercase
        elif char_type == "digits":
            case = string.digits
        elif char_type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, char_count: int = 5):
        """
        Get unique name

        :param char_count: amount of characters
        :return: unique name as string
        """
        return self.get_alpha_numeric(char_count, char_type="lower")

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text

        :return: True/False
        """
        self.log.info(f"------------------------------------------------------------------------")
        self.log.info(f"---------------------| VERIFYING TEXT |---------------------------------")

        self.log.info(f"--> Actual text from application --> | {actual_text} |")
        self.log.info(f"->> Expected text from test case ->> | {expected_text} |")
        if expected_text.lower() in actual_text.lower():
            self.log.info(f"{"-" * 10}VERIFICATION PASSED --> ACTUAL TEXT CONTAINS EXPECTED TEXT{"-" * 10}")
            self.log.info(f"------------------------------------------------------------------------")
            return True
        else:
            self.log.warning(
                f"{"*" * 10}VERIFICATION FAILED --> ACTUAL TEXT DOES NOT CONTAIN EXPECTED TEXT{"*" * 10}")
            self.log.info(f"------------------------------------------------------------------------")

            return False

    def verify_text_match(self, actual_text, expected_text):
        """
        Verify actual text matches with expected text

        :return: True/False
        """
        self.log.info(f"------------------------------------------------------------------------")
        self.log.info(f"---------------------| VERIFYING TEXT |---------------------------------")

        self.log.info(f"--> Actual text from application --> | {actual_text} |")
        self.log.info(f"->> Expected text from test case --> | {expected_text} |")
        if actual_text.lower() == expected_text.lower():
            self.log.info(f"{"-" * 10}VERIFICATION PASSED --> ACTUAL TEXT CONTAINS EXPECTED TEXT{"-" * 10}")
            self.log.info(f"------------------------------------------------------------------------")
            return True
        else:
            self.log.warning(
                f"{"*" * 10}VERIFICATION FAILED --> ACTUAL TEXT DOES NOT CONTAIN EXPECTED TEXT{"*" * 10}")
            self.log.info(f"------------------------------------------------------------------------")

            return False