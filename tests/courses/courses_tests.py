from pages.courses.courses_page import CoursesPage
from unittest import TestCase
from inspect import currentframe
import pytest
from utilities.test_status import StatusOfTest
from utilities import custom_logger as cl


@pytest.mark.usefixtures("one_time_setup", "setup")
class CourseTest(TestCase):

    log = cl.custom_logger()

    @pytest.fixture(autouse=True)
    def before_each(self, one_time_setup):
        self.login_page = CoursesPage(self.driver)
        self.status_test = StatusOfTest(self.driver)

    def test_03_check_java_course_in_all_courses(self):
        """
        Test name - Verify java course is on the screen (positive)

        Valid email
        Valid password
        """
        self.log.info(f"   -------> Running {currentframe().f_code.co_name} test method <-------")
        self.log.info(f"---------------------------------------------------------------------")

        self.login_page.scroll_to_see_java_course()
        result1 = self.login_page.verify_java_course_on_screen()

        self.log.info(result1)

        self.status_test.mark_final(1, 1, "test_03_check_java_course_in_all_courses",
                                    result1, "Java course is shown on the screen",
                                    "Java course is not shown on the screen")