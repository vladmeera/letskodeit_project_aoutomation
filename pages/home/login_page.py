from base.basepage import BasePage
from utilities.custom_logger import custom_logger as cl
import os

class LoginPage(BasePage):

    log = cl()

    _email = os.environ.get('LETSKODEIT_EMAIL')
    _password = os.environ.get('LETSKODEIT_PASS')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver



    # Locators
    _login_link: str = "//a[text()='Sign In']" #xpath
    _email_field: str = "email" #id
    _password_field: str = "login-password" #id
    _login_btn: str = "login" #id

    # Element occurs after successful login
    _element_to_verify_login: str = "//div[@class='zen-course-title']" #xpath

    #Wrong password error
    _error_to_verify_password: str = "//span[text()='The password field is required.']" #xpath

    # Titles
    _titles = ["My Courses"]

    #Valid login
    _credentials = {"valid_login": "mirgorodvld@gmail.com", "valid_password": "xnDi!1Bxi09bU",
                    "invalid_login": "vld_123456@gmail.com", "invalid_password": "123456"}



    def click_login_link(self):
        self.click_element(self._login_link, "xpath")

    def enter_email(self, email):
        if email == self._credentials["valid_login"]:
            self.log.info(f"{"*" * 20}Entered email ({email}) is correct{"*" * 20}")
            self.send_keys_element(email, self._email_field)
        else:
            self.log.warning(f"{"!" * 20}Entered password ({email}) is INCORRECT{"!" * 20}")

    def enter_password(self, password = ""):
        if password == self._credentials["valid_password"]:
            self.log.info(f"{"*" * 20}Entered password ({password}) is correct!{"*" * 20}")
            self.send_keys_element(password, self._password_field)

        elif password == self._credentials["invalid_password"]:
            self.log.info(f"{"*" * 20}Entered invalid password ({password}) is correct!{"*" * 20}")
            self.send_keys_element(password, self._password_field)


    def click_login_btn(self):
        self.click_element(self._login_btn)

    def wait_until_presented(self):
        self.wait_for_element("//div[@class='zen-course-title']", "xpath")


    def login(self, email: str, password: str):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_btn()
        self.wait_until_presented()


    def verify_login_successful(self) -> bool:
        return self.is_element_present(self._element_to_verify_login, "xpath")


    def invalid_login(self, email = "", password = ""):
        self.click_login_link()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_btn()


    def verify_login_unsuccessful(self) -> bool:
        return self.is_element_present(self._error_to_verify_password, "xpath")

    def verify_title(self, title_number):
        return self.verify_page_title(self._titles[title_number])