"""
@package utilities

Util class implementation
All most common utilities should be implemented here

Example:
    name = self.util.get_unique_name()
"""
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, printable
from time import sleep
from traceback import print_stack
from random import choice
import utilities.custom_logger as cl
from logging import DEBUG
from os import path
from pandas import read_csv
from os.path import join

class Util:

    log = cl.custom_logger(DEBUG)
    def __init__(self):
        self.locator_file = join("..", "locators.csv")

    def sleep_(self, seconds, message = "sleeping") -> None:
        """
        Put the program to wait for the specified time
        """
        if message is not None:
            self.log.info(f"Waiting {seconds} seconds; {message}")
        try:
            sleep(seconds)
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

        return alpha_num.join(choice(case) for i in range(length))

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
        self.log.info(f"Actual text - {actual_text}")
        self.log.info(f"Expected text - {expected_text}\n")
        if expected_text.lower() in actual_text.lower() and (expected_text != '' and expected_text != ' '):
            return True
        else:
            self.log.error("Verification failed\n")
            return False

    def verify_text_match(self, actual_text, expected_text) -> bool:
        """
        Verify actual text matches with expected text

        :return: True/False
        """
        self.log.info(f"Actual text - {actual_text}")
        self.log.info(f"Expected text - {expected_text}\n")
        if actual_text.lower() == expected_text.lower():
            return True
        else:
            self.log.warning("Verification failed")
            return False


    def get_locator(self, element_name: str):
        if not path.exists(self.locator_file):
            self.log.error("File not found")
            return None

        try:
            reader = read_csv(self.locator_file)
            locator = reader[reader["element_name"] == str(element_name)]
            locator_ = locator.values[-1]
            if locator_ is not None:
                return str(locator_[2])
            else:
                self.log.warning("Element found and empty string returned!")
        except (KeyError, ValueError):
            self.log.error(
                f"Error has occurred! No such element - {element_name}! Please find or add another element!"
            )

