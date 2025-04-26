from base.basepage import BasePage
from utilities.custom_logger import custom_logger as cl
import os
from utilities.excel_util import ExcelLocators, ExcelAccounts


class LoginPage(BasePage):

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

    def go_back(self):
        self.navigate_page()

    def click_login_link(self):
        self.click_element(self.locators.get_locator("start",
                                                     "login link",
                                                     "xpath"),"xpath")

    def enter_email(self, email, locator_type):
        self.send_keys_element(email, self.locators.get_locator(), locator_type)

    def enter_password(self, password):
        self.send_keys_element(password, self.locators.get_locator("login",
                                                                   "password field",
                                                                   "id"))

    def click_login_btn(self):
        self.click_element(self.locators.get_locator("login",
                                                     "login button",
                                                     "id"))

    def wait_until_presented_element_courses(self):
        self.wait_for_element(self.locators.get_locator("my courses",
                                                        "element to verify login",
                                                        "xpath"), "xpath")


    def successful_login(self):
        self.click_login_link()
        self.enter_email(self.accounts.get_login(), "xpath")
        self.enter_password(self.accounts.get_password())
        self.click_login_btn()
        self.wait_until_presented_element_courses()


    def verify_login_successful(self):
        return self.is_element_present(self.locators.get_locator("my courses",
                                                                 "element to verify login",
                                                                 "xpath"), "xpath")

    def verify_login_successful_avatar(self):
        return self.is_element_present(self.locators.get_locator("my courses",
                                                                 "element to verify login avatar",
                                                                 "xpath"), "xpath")

    def verify_title_my_courses(self):
        return self.verify_page_title(self.locators.get_locator("my courses",
                                                                "title my courses page",
                                                                "name"))

    def unsuccessful_login_no_pass(self):
        self.click_login_link()
        self.enter_email(self.accounts.get_login(1, "valid"),
                         "xpath")
        self.click_login_btn()


    def verify_login_unsuccessful(self):
        return self.is_element_present(self.locators.get_locator("login",
                                                                 "error to verify no pass",
                                                                 "xpath"), "xpath")

