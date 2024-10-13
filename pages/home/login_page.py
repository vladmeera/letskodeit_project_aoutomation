from time import sleep
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger as cl

class LoginPage(SeleniumDriver, BasePage):

    log = cl()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators
    _login_link: str = "//a[text()='Sign In']" #xpath
    _email_field: str = "email" #id
    _password_field: str = "login-password" #id
    _login_btn: str = "login" #id

    # Element occurs after successful login
    _element_to_verify_login: str = "//button[@id='dropdownMenu1']" #xpath

    #Wrong password error
    _error_to_verify_password: str = "//span[text()='The password field is required.']" #xpath

    # Titles
    _titles = ["Login"]



    def click_login_link(self) -> None:
        self.click_element(self._login_link, "xpath")

    def enter_email(self, email: str) -> None:
        self.send_keys_element(email, self._email_field)

    def enter_password(self, password: str) -> None:
        self.send_keys_element(password, self._password_field)

    def click_login_btn(self) -> None:
        self.click_element(self._login_btn)


    def login(self, email: str, password: str) -> None:
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        sleep(2)
        self.click_login_btn()

    def verify_login_successful(self) -> bool:
        return self.is_element_present(self._element_to_verify_login, "xpath")


    def invalid_login(self, email: str, password: str = "") -> None:
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        sleep(2)
        self.click_login_btn()

    def verify_login_unsuccessful(self) -> bool:
        return self.is_element_present(self._error_to_verify_password, "xpath")

    def verify_title(self):
        return self.verify_page_title(self._titles)