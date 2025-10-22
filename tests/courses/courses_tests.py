from inspect import currentframe
from unittest import TestCase

import pytest

from pages.courses.courses_page import CoursesPage
from utilities import custom_logger as cl
from utilities.test_status import StatusOfTest


@pytest.mark.usefixtures("one_time_setup", "setup")
class CourseTest(TestCase):
    log = cl.custom_logger()

    @pytest.fixture(autouse=True)
    def before_each(self, one_time_setup):
        self.courses_page = CoursesPage(self.driver)
        self.status_test = StatusOfTest(self.driver)

    def test_03_check_java_course_in_all_courses(self):
        """
        Test name - Verify java course is on the screen (positive)

        Valid email
        Valid password
        """
        self.log.info(f"Running {currentframe().f_code.co_name} test method")
        self.log.info("---------------------------------------------------------------")

        self.courses_page.scroll_to_see_java_course()
        test_result = self.login_page.verify_java_course_on_screen()

        self.log.info(test_result)

        self.status_test.mark_final(
            test_number=3,
            total_tests=3,
            test_name="test_03_check_java_course_in_all_courses",
            result=test_result,
            result_message_success="Java course is shown on the screen",
            result_message_fail="Java course is not shown on the screen",
        )
