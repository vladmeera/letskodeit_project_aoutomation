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
        self.fail = "fail"
        self.error = "error"
        self.pass_ = "pass"

    def set_result(self, result):
        try:
            if result is not None and result:
                self.result_list.append(self.pass_)
            else:
                self.result_list.append(self.fail)
                self.screenshot()

        except Exception as e:
            self.result_list.append(self.error)
            self.log.error(f"Exception occurred - {e}")
            self.screenshot()

    def mark(self, result):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result)

    def mark_final(self, result):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result)

        if self.fail in self.result_list or self.error in self.result_list:
            self.log.warning("Test failed")
            self.result_list.clear()
            assert False

        else:
            self.log.info("Test successful")
            self.result_list.clear()
            assert True
