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

    def __init__(self, browser) -> None:

        self.browser = browser


    def get_webdriver(self):
        """
        Get WebDriver instance based on browser configuration

        :return: WebDriver instance
        """
        base_url = "https://www.letskodeit.com/"

        if self.browser == "chrome":
            driver = webdriver.Chrome()
            self.log.info("Running tests on chrome")
            self.log.info(f"Open browser with provided url: {base_url}")
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
            self.log.info("Running tests on firefox")
            self.log.info(f"Open browser with provided url: {base_url}")
        elif self.browser == "safari":
            driver = webdriver.Safari()
            self.log.info("Running tests on safari")
            self.log.info(f"Open browser with provided url: {base_url}")
        elif self.browser == "iexplorer":
            driver = webdriver.Ie()
            self.log.info("Running tests on internet explorer")
            self.log.info(f"Open browser with provided url: {base_url}")
        elif self.browser == "edge":
            driver = webdriver.Edge()
            self.log.info("Running tests on edge")
            self.log.info(f"Open browser with provided url: {base_url}")
        else:
            driver = webdriver.Chrome()
            self.log.info("Running tests on chrome")
            self.log.info(f"Open browser with provided url: {base_url}")

        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(base_url)
        return driver