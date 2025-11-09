from utilities.custom_logger import custom_logger as cl
from utilities.data_util import TestData as Locators
from pages.home.login_page import LoginPage
from base.selenium_driver import SeleniumDriver


class CoursesPage:
    log = cl()
    locators = Locators()



    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.driver_function = SeleniumDriver(self.driver)

    def go_back(self):
        self.driver_function.navigate_page()

    def open_courses_page(self):
        self.login_page.successful_login()
        self.driver_function.click_element(self.locators.get_locator("all_courses_link"), "xpath")

    def scroll_to_see_java_course(self):
        self.open_courses_page()
        self.driver_function.scroll_page_bottom()


    def verify_java_course_on_screen(self):
        return self.is_element_present(self.locators.get_locator("all courses"))
