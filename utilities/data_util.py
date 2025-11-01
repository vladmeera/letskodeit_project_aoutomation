from os import path
from pandas import read_csv
from utilities import custom_logger as logger

class TestData:
    logger_ = logger.custom_logger()

    def __init__(self, locator_file):
        self.locator_file: str = locator_file

    def get_locator(self, element_name: str):
        if path.exists(self.locator_file):
            reader = read_csv(self.locator_file)
            try:
                locator = reader[reader['element_name'] == str(element_name)]
                locator_ = locator.values[-1]
                if locator_ is not None:
                    return str(locator_[2])
                else:
                    self.logger_.warning("Element found and empty string returned!")
            except (KeyError, ValueError):
                self.logger_.error(f"Error has occurred! No such element - {element_name}! Please find or add another element!")

        else:
            self.logger_.warning("No such file. Create a new file or change the directory path!")



