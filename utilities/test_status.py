
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

    def set_result(self, test_number, total_tests, result, result_message_success=" ", result_message_fail=" "):
        try:
            if result is not None and result:
                self.result_list.append("Pass")

                self.log.info(f"--> --> --> | TEST {test_number}/{total_tests} SUCCESSFUL | {result_message_success} <-- <-- <--")
                self.log.info(f"------------------------------------------------------------------------------------------------")
                self.log.info(f"   ")

            else:
                self.result_list.append("Fail")

                self.log.info(f"->> ->> ->> ->> | TEST {test_number}/{total_tests} FAIL | {result_message_fail} <<- <<- <<- <<-")
                self.log.info(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.log.info(f"   ")

                self.screenshot(result_message_fail)

        except Exception as e:
            self.result_list.append("Fail")

            self.log.error(f"************************************************************************")
            self.log.error(f"-------------------| EXCEPTION OCCURRED | {e} |------------")
            self.log.error(f"************************************************************************")

            self.screenshot(result_message_fail)

    def mark(self, test_number, total_tests, result, result_message_success = " ", result_message_fail=" "):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(test_number, total_tests, result, result_message_success, result_message_fail)

    def mark_final(self, test_number, total_tests, test_name, result, result_message_success = " ", result_message_fail=" "):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(test_number, total_tests, result, result_message_success, result_message_fail)

        if "Fail" in self.result_list:
            self.log.error(f"********************************************************************************")
            self.log.error(f"-------------------| {test_name} | TEST FAILED |------------")
            self.log.error(f"********************************************************************************")

            self.result_list.clear()
            assert True == False

        else:
            self.log.info(f"----------------------------------------------------------------------")
            self.log.info(f"--> --> --> | {test_name} | TEST SUCCESSFUL | <-- <-- <--")
            self.log.info(f"----------------------------------------------------------------------")

            self.result_list.clear()
            assert True == True