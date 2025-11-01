from base.basepage import BasePage
from utilities.custom_logger import custom_logger as cl
from utilities.data_util import TestData as Locators
from pages.home.login_page import LoginPage
from os.path import dirname, join



class CoursesPage(BasePage):
    log = cl()
    path = dirname(__file__)
    path_ = join(path, "..", "..", "locators.csv")
    locators = Locators(path_)


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.login_page = LoginPage(driver)

    def go_back(self):
        self.navigate_page()

    def open_courses_page(self):
        self.login_page.successful_login()
        self.click_element(self.locators.get_locator("all_courses_link"), "xpath")

    def scroll_to_see_java_course(self):
        self.open_courses_page()
        self.scroll_page(to_bottom=True)


    def verify_java_course_on_screen(self):
        return self.is_element_present(self.locators.get_locator("all courses",
                                                   "selenium webdriver 4 with java",
                                                   "xpath"), "xpath")
