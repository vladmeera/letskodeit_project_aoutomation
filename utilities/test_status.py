
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger as cl


class StatusOfTest(SeleniumDriver):

    log = cl()

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(StatusOfTest, self).__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message_fail=" "):
        try:
            if result is not None and result:
                self.result_list.append("Pass")
            else:
                self.result_list.append("Fail")
                self.screenshot(result_message_fail)

        except Exception as e:
            self.result_list.append("Error")
            self.log.error(f"Exception occurred - {e}")
            self.screenshot(result_message_fail)

    def mark(self, result, result_message_fail=" "):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message_fail)

    def mark_final(self, test_name, result, result_message_success = " ", result_message_fail=" "):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message_success, result_message_fail)

        if "Fail" in self.result_list:
            self.log.error(f"-------------------| {test_name} | TEST FAILED |------------")
            self.result_list.clear()
            assert False

        else:
            self.log.info(f"--> --> --> | {test_name} | TEST SUCCESSFUL | <-- <-- <--")
            self.result_list.clear()
            assert True