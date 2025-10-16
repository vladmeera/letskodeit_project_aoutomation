from base.basepage import BasePage
from utilities.custom_logger import custom_logger as cl
from os.path import dirname, join
from os import getenv

from utilities.data_util import TestData as LocatorsData
from dotenv import load_dotenv


class LoginPage(BasePage):

    log = cl()
    path = dirname(__file__)
    path_ = join(path, "..", "..", 'utilities\\locators.csv')
    locators = LocatorsData(path_)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def configure(self):
        load_dotenv()

    def get_account(self, key):
        load_dotenv()
        return getenv(key)

    def go_back(self):
        self.navigate_page()

    def click_login_link(self):
        self.click_element(self.locators.get_locator('login_link'), locator_type="xpath")

    def enter_email(self, email):
        self.send_keys_element(email, locator=self.locators.get_locator('email_field'))

    def enter_password(self, password):
        self.send_keys_element(password, self.locators.get_locator("password_field"))

    def click_login_btn(self):
        self.click_element(self.locators.get_locator("login_button"))

    def delete_keys_email(self):
        self.delete_keys(self.locators.get_locator("email_field"))

    def wait_until_presented_element_courses(self):
        self.wait_for_element(self.locators.get_locator("element_to_verify_login_avatar"), "xpath")


    def successful_login(self):
        self.enter_email(self.get_account("LOGIN_VALID_1"))
        self.enter_password(self.get_account("PASSWORD_VALID_1"))
        self.click_login_btn()
        self.wait_until_presented_element_courses()


    def verify_login_successful(self):
        return self.is_element_present(self.locators.get_locator("element_to_verify_login_java_course"), "xpath")

    def verify_login_successful_avatar(self):
        return self.is_element_present(self.locators.get_locator("element_to_verify_login_avatar"), "xpath")

    def verify_title_my_courses(self):
        return self.verify_page_title("My Courses")

    def unsuccessful_login_no_pass(self):
        self.click_login_link()
        self.enter_email(self.get_account("LOGIN_VALID_1"))
        self.click_login_btn()


    def verify_login_unsuccessful(self):
        return self.is_element_present(self.locators.get_locator("error_to_verify_no_pass"), "xpath")

