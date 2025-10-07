import time

from base.basepage import BasePage
from utilities.custom_logger import custom_logger as cl
import os
from utilities.data_util import ExcelLocators, ExcelAccounts
from pages.home.login_page import LoginPage


class CoursesPage(BasePage):
    current_dir = os.path.dirname(__file__)
    excel_files_path = os.path.join(current_dir, "..", "..")
    excel_locators_file = os.path.join(excel_files_path, "locators.xlsx")
    excel_accounts_file = os.path.join(excel_files_path, "accounts.xlsx")

    locators = ExcelLocators(excel_locators_file)
    accounts = ExcelAccounts(excel_accounts_file)

    log = cl()


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_page = LoginPage(driver)

    def go_back(self):
        self.navigate_page()

    def open_courses_page(self):
        self.login_page.successful_login()
        self.click_element(self.locators.get_locator("header",
                                                     "all courses link",
                                                     "xpath"), "xpath")

    def scroll_to_see_java_course(self):
        self.open_courses_page()
        self.scroll_page(to_bottom=True)


    def verify_java_course_on_screen(self):
        return self.is_element_present(self.locators.get_locator("all courses",
                                                   "selenium webdriver 4 with java",
                                                   "xpath"), "xpath")
