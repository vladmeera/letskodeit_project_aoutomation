"""
@package utilities

Util class implementation
All most common utilities should be implemented here

Example:
    name = self.util.get_unique_name()
"""
try:
    from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits
    import time
    import traceback
    import random
    import utilities.custom_logger as cl
    from logging import DEBUG
except (ImportError, ModuleNotFoundError):
    print(f'Error occurred importing packages/dependencies! Please, make sure you have them all installed on your system!')


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
            self.log.error(f"| INTERRUPTED ERROR | {e}")
            traceback.print_stack()

    def get_alpha_numeric(self, length, char_type) -> str:
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
            'letters': ascii_letters
        }
        case = char_type_dict[char_type]

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