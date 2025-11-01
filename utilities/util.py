"""
@package utilities

Util class implementation
All most common utilities should be implemented here

Example:
    name = self.util.get_unique_name()
"""
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, printable
import time
from traceback import print_stack
import random
import utilities.custom_logger as cl
from logging import DEBUG


class Util(object):

    log = cl.custom_logger(DEBUG)

    def sleep(self, seconds, message = "???") -> None:
        """
        Put the program to wait for the specified time
        """
        if message is not None:
            self.log.info(f"Wait :: {seconds} :: for :: {message}")
        try:
            time.sleep(seconds)
        except InterruptedError as e:
            self.log.error(f"Error occurred - {e}")
            print_stack()

    def get_alpha_numeric(self, length: int, char_type: str = 'letters') -> str | None:
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should contain
            char_type: Type of characters string should contain, default is "letters"
            Provide lower/upper/digits/mix for different types
        """
        alpha_num = ''

        char_type_dict = {
            'lower': ascii_lowercase,
            'upper': ascii_uppercase,
            'digits': digits,
            'mix': ascii_letters + digits,
            'letters': ascii_letters,
            'printable': printable
        }
        case = char_type_dict.get(char_type.lower())
        if case is None:
            self.log.warning(f"There is no - {char_type} - character type!\n")
        else:
            return alpha_num.join(random.choice(case) for i in range(length))

    def get_password(self, length: int = 1) -> str:

        return self.get_alpha_numeric(length=length, char_type="printable")


    def get_unique_name_lower(self, char_count: int = 5):

        return self.get_alpha_numeric(char_count, char_type="lower")

    def get_unique_name_upper(self, char_count: int = 5) -> str:

        return self.get_alpha_numeric(char_count, char_type="upper")

    def verify_text_contains(self, actual_text: str, expected_text: str) -> bool | None:

        """
        Verify actual text contains expected text

        :return: True/False
        """
        self.log.info(f"Actual text from application - {actual_text}")
        self.log.info(f"Expected text to be in actual - {expected_text}\n")
        if expected_text.lower() in actual_text.lower() and (expected_text != '' and expected_text != ' '):
            self.log.info("Verification passed\n")
            return True
        elif expected_text.lower() not in actual_text.lower() and (actual_text != '' and actual_text != ' '):
            self.log.warning("Verification failed\n")
            return False
        else:
            self.log.warning("Verification was not successful! Actual or expected text can't be empty!")

    def verify_text_match(self, actual_text, expected_text) -> bool:
        """
        Verify actual text matches with expected text

        :return: True/False
        """
        self.log.info(f"--> Actual text from the application --> | {actual_text} |")
        self.log.info(f"->> Expected text from the test case --> | {expected_text} |")
        if actual_text.lower() == expected_text.lower():
            self.log.info(f"{"-" * 10}VERIFICATION PASSED --> ACTUAL TEXT CONTAINS EXPECTED TEXT{"-" * 10}")
            return True
        else:
            self.log.warning(
                f"{'*' * 10}VERIFICATION FAILED --> ACTUAL TEXT DOES NOT CONTAIN EXPECTED TEXT{'*' * 10}"
            )
            return False