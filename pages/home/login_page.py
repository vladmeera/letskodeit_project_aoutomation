from os import getenv

from dotenv import load_dotenv

from utilities.custom_logger import custom_logger as cl
from utilities.data_util import TestData as Locators
from base.selenium_driver import SeleniumDriver

class LoginPage:
    log = cl()
    locators = Locators()

    def __init__(self, driver):
        self.driver = driver
        self.driver_function = SeleniumDriver(self.driver)

    def configure(self):
        load_dotenv()

    def get_account(self, key):
        load_dotenv()
        return getenv(key)

    def go_back(self):
        self.driver_function.navigate_page()

    def go_forward(self):
        self.driver_function.navigate_page(direction="forward")

    def refresh(self):
        self.driver_function.navigate_page(direction="refresh")

    def click_login_link(self):
        self.driver_function.click_element(
            self.locators.get_locator("login_link"), locator_type="xpath"
        )

    def enter_email(self, email):
        self.driver_function.send_keys_element(email, locator=self.locators.get_locator("email_field"))

    def enter_password(self, password):
        self.driver_function.send_keys_element(password, self.locators.get_locator("password_field"))

    def click_login_btn(self):
        self.driver_function.click_element(self.locators.get_locator("login_button"))

    def delete_keys_email(self):
        self.driver_function.delete_keys(self.locators.get_locator("email_field"))

    def wait_until_presented_element_courses(self):
        self.driver_function.wait_for_element(
            self.locators.get_locator("element_to_verify_login_avatar"), "xpath"
        )

    def successful_login(self):
        self.enter_email(self.get_account("LOGIN_VALID_1"))
        self.enter_password(self.get_account("PASSWORD_VALID_1"))
        self.click_login_btn()
        self.wait_until_presented_element_courses()

    def unsuccessful_login_no_pass(self):
        self.click_login_link()
        self.enter_email(self.get_account("LOGIN_VALID_1"))
        self.click_login_btn()


    def verify_login_successful(self) -> bool:
        return self.driver_function.is_element_present(
            self.locators.get_locator("element_to_verify_login_java_course"), "xpath"
        )

    def verify_login_successful_avatar(self) -> bool:
        return self.driver_function.is_element_present(
            self.locators.get_locator("element_to_verify_login_avatar"), "xpath"
        )

    def verify_title_my_courses(self) -> bool:
        return self.driver_function.verify_page_title("My Courses")


    def verify_login_unsuccessful(self) -> bool:
        return self.driver_function.is_element_present(
            self.locators.get_locator("error_to_verify_no_pass"), "xpath"
        )
