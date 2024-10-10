
from base.selenium_driver import SeleniumDriver
from utilities.custom_logger import custom_logger as cl

class TestStatus(SeleniumDriver):

    log = cl()

    def __init__(self, driver):
        """
        Inits CheckPoint class
        """
        super(TestStatus, self).__init__(driver)
        self.result_list: list[str] = []

    def set_result(self, result: bool, result_message: str = ""):
        try:
            if result is not None:
                if result:
                    self.result_list.append("Pass")
                    result_message: str = ""
                    self.log.info(f"| TEST SUCCESSFUL | {result_message}")
                else:
                    self.result_list.append("Fail")
                    self.log.warning(f"| TEST FAILED | {result_message}")
                    self.screenshot(result_message)
            else:
                self.result_list.append("Fail")
                self.log.info(f"| TEST FAILED | {result_message}")
                self.screenshot(result_message)

        except AttributeError as e:
            self.result_list.append("Fail")
            self.log.error(f"| ATTRIBUTE ERROR | {result_message} | {e}")
            self.screenshot(result_message)
        except TypeError as e:
            self.result_list.append("Fail")
            self.log.error(f"| TYPE ERROR | {result_message} | {e}")
            self.screenshot(result_message)
        except Exception as e:
            self.result_list.append("Fail")
            self.log.error(f"| EXCEPTION OCCURRED | {result_message} | {e}")
            self.screenshot(result_message)

    def mark(self, result: bool, result_message: str = ""):
        """
        Mark the result of the verification point in a test case
        """
        self.set_result(result, result_message)

    def mark_final(self, test_name: str, result: bool, result_message: str = ""):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message)

        if "Fail" in self.result_list:
            self.log.error(f"{test_name} !!! FAILED !!!")
            self.result_list.clear()
            assert True == False

        else:
            self.log.info(f"{test_name} !!! PASSED !!!")
            self.result_list.clear()
            assert True == True