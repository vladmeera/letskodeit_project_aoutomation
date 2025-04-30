"""
@package base

WebDriver factory class implementation
It creates a webdriver instance based on browser configuration

Examples:
    wdf = WebDriverFactory(browser)
    wdf.get_webdriver()
"""

from selenium import webdriver
from utilities.custom_logger import custom_logger as cl

class WebDriverFactory:

    log = cl()

    def __init__(self, browser):

        self.browser = browser


    def get_webdriver(self):
        """
        Get WebDriver instance based on browser configuration

        :return: WebDriver instance
        """
        base_url = "https://www.letskodeit.com/"

        if self.browser == "chrome":
            driver = webdriver.Chrome()
            self.log.warning(f"\n")
            self.log.warning(f"{" " * 20}")
            self.log.warning(f"{"#" * 120}")
            self.log.warning(f"{"#" * 50} NEW SESSION STARTED {'#' * 50}")
            self.log.warning(f"{"#" * 120}")
            self.log.warning(f"{" " * 20}")
            self.log.warning("Running tests on chrome")
            self.log.warning(f"Open browser with provided url: {base_url}")
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            self.log.warning(f"{" " * 20}")
            self.log.warning(f"{"#" * 120}")
            self.log.warning(f"{"#" * 50} NEW SESSION STARTED {'#' * 50}")
            self.log.warning(f"{"#" * 120}")
            self.log.warning(f"{" " * 20}")
            self.log.warning("Running tests on firefox")
            self.log.warning(f"Open browser with provided url: {base_url}")
        elif self.browser == "safari":
            driver = webdriver.Safari()
            self.log.warning(f"{"#" * 120}")
            self.log.warning(f"{"#" * 50} NEW SESSION STARTED {'#' * 50}")
            self.log.warning(f"{"#" * 120}")
            self.log.warning("Running tests on safari")
            self.log.warning(f"Open browser with provided url: {base_url}")
        elif self.browser == "iexplorer":
            driver = webdriver.Ie()
            self.log.warning(f"{"#" * 120}")
            self.log.warning(f"{"#" * 50} NEW SESSION STARTED {'#' * 50}")
            self.log.warning(f"{"#" * 120}")
            self.log.warning("Running tests on internet explorer")
            self.log.warning(f"Open browser with provided url: {base_url}")
        elif self.browser == "edge":
            driver = webdriver.Edge()
            self.log.warning(f"{"#" * 120}")
            self.log.warning(f"{"#" * 50} NEW SESSION STARTED {'#' * 50}")
            self.log.warning(f"{"#" * 120}")
            self.log.warning("Running tests on edge")
            self.log.warning(f"Open browser with provided url: {base_url}")
        else:
            driver = webdriver.Chrome()
            self.log.warning(f"{"#" * 120}")
            self.log.warning(f"{"#" * 50} NEW SESSION STARTED {'#' * 50}")
            self.log.warning(f"{"#" * 120}")
            self.log.warning("Running tests on chrome")
            self.log.warning(f"Open browser with provided url: {base_url}")

        driver.implicitly_wait(2)
        driver.maximize_window()
        driver.get(base_url)
        return driver