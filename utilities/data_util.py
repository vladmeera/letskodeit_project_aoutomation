from csv import writer
from os import path
from pandas import read_csv
from pandas import DataFrame
from utilities import custom_logger as cl

class TestData:
    logger = cl.custom_logger()

    def __init__(self, locator_file):
        """1. Change the path to your file when creating a new instance!
        2. The path could be used as a place where you create new file as well!

        Example:
            from utillities import data_util
            data = data_util.TestData("path to your file")

            data.add_new_locator("...", "...", "...")

        """
        self.locator_file: str = locator_file

    def see_locators(self) -> DataFrame | None:
        if path.exists(self.locator_file):
            self.logger.info("File was found! Start reading the file!")
            try:
                csv_reader = read_csv(self.locator_file)
                return csv_reader

            except PermissionError:
                self.logger.error('Change permission of the file!')
        else:
            self.logger.warning("File was not found!")
            return None




    def create_file(self):
        if path.exists(self.locator_file):
            self.logger.warning(f"File already exists! File location - {self.locator_file}")
        else:
            self.logger.info(f"File was not found! Creating new file! File location - {self.locator_file}")
            try:
                with open(self.locator_file, 'w') as locators:
                    csv_writer = writer(locators)
                    data = ['element_name', 'locator_name', 'locator']
                    csv_writer.writerow(data)
            except Exception as e:
                self.logger.error(f"Unexpected error occurred - {e}")



    def add_new_locator(self, element_name: str, locator_name: str, locator: str ):

        try:
            with open(self.locator_file, "a") as locators:
                csv_writer = writer(locators)
                data: list[str] = [element_name, locator_name, locator]

                csv_writer.writerow(data)


        except IOError as e:
            self.logger.warning(f"File was not found - {e}")

    def get_locator(self, element_name: str):
        if path.exists(self.locator_file):
            reader = read_csv(self.locator_file)
            try:
                locator = reader[reader['element_name'] == str(element_name)]
                locator_ = locator.values[-1]
                if locator_ is not None:
                    return str(locator_[2])
                else:
                    self.logger.warning(f"Element found and empty string returned!")
            except (KeyError, ValueError):
                self.logger.error(f"Error has occurred! No such element - {element_name}! Please find or add another element!")

        else:
            self.logger.warning("No such file. Create a new file or change the directory path!")



