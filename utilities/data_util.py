from os import path
from pandas import read_csv
from utilities import custom_logger as logger

class TestData:
    logger_ = logger.custom_logger()

    locator_file: str = path.join('..', 'locators.csv')

    def get_locator(self, element_name: str):
        if not path.exists(self.locator_file):
            self.logger_.error("File not found")
            return None

        try:
            reader = read_csv(self.locator_file)
            locator = reader[reader['element_name'] == str(element_name)]
            locator_ = locator.values[-1]
            if locator_ is not None:
                return str(locator_[2])
            else:
                self.logger_.warning("Element found and empty string returned!")
        except (KeyError, ValueError):
            self.logger_.error(f"Error has occurred! No such element - {element_name}! Please find or add another element!")




