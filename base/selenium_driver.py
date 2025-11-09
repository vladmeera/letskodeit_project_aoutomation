import os
from datetime import date, datetime
from time import time
from traceback import print_stack

from django.db.models import Expression
from selenium.common.exceptions import (
    ElementNotSelectableException,
    ElementNotVisibleException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from utilities.custom_logger import custom_logger as cl
from utilities.util import Util

# from selenium import webdriver
# dr = webdriver.Chrome()
# dr.back()


class SeleniumDriver:
    log = cl()

    def __init__(self, driver):
        """
        Initializes the SeleniumDriver instance with the provided Webdriver.

        :param driver: The Selenium WebDriver instance.
        """
        self.utility = Util()
        self.driver = driver

    def navigate_page(self, direction: str = "back"):
        """
        Directions:
            back
            forward
            refresh
        """

        direction_list_ = ("back", "forward", "refresh")
        if (
            direction == " "
            or direction.lower() not in direction_list_
            or direction is None
        ):
            self.log.warning("Wrong direction")
            raise TypeError("Wrong direction!")

        def page_back():
            self.driver.back()

        def page_forward():
            self.driver.forward()

        def refresh():
            self.driver.refresh()


        direction_map = {"back": page_back, "forward": page_forward, "refresh": refresh}

        return direction_map[direction]()

    def screenshot(self) -> None:
        """
        Takes a screenshot if the directory exists. If not, creates and then takes a screenshot.
        """

        current_date: date = datetime.now().date()

        file_name: str = f"{current_date}_{str(round(time() * 1000))}.png"

        relative_path = os.path.join("..", "screenshots", file_name)

        current_directory = os.path.dirname(__file__)
        destination_path = os.path.join(current_directory, relative_path)
        destination_directory = os.path.join(current_directory, "..", "screenshots")

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            self.driver.save_screenshot(destination_path)

        except Exception as e:
            self.log.error(f"Error occurred while saving a screenshot: {e}")

    def get_title(self):
        """
        Gets title of the current page.

        :return: title as a string.
        """
        try:
            title = self.driver.title
            return title
        except Exception as e:
            self.log.error(f"Error occurred: {e}")

    # To get By.type
    def get_by_type(self, locator_type: str):
        """
        Get the Selenium By type based on a string identifier. Default is ID.

        :param locator_type: 'id', 'css_selector', 'xpath'.
        :return: Selenium By method for the provided locator type.
        """
        list_of_locators = (
            "id",
            "name",
            "xpath",
            "css",
            "class",
            "link",
            "partial_link",
            "tag",
        )
        locator_type = locator_type.lower()

        if locator_type not in list_of_locators:
            self.log.warning(
                f"Wrong locator type: {locator_type}! List of all locators: {
                    list_of_locators
                }\n"
            )
            return None

        by_types = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "link": By.LINK_TEXT,
            "partial_link": By.PARTIAL_LINK_TEXT,
            "tag": By.TAG_NAME,
        }
        by_type = by_types.get(locator_type, By.ID)
        return by_type

    # To find an element (default locator type is ID)
    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                return element
            else:
                self.log.warning("Element was not found\n")
                return element

        except Exception as e:
            self.log.error(f"Exception occurred while searching for the element - {e}")
            return element

    def get_elements(self, locator, locator_type="id"):
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            if len(elements) > 0:
                return elements
            else:
                self.log.warning(f"Found {len(elements)} elements\n")
                return elements

        except Exception as e:
            self.log.error(f"WebDriverException occurred: {e}")
            return elements

    def click_element(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element:
                element.click()
            else:
                self.log.warning("Unable to click on the element\n")
        except Exception as e:
            self.log.error(f"An unexpected exception occurred: {e}\n")
            print_stack()

    def send_keys_element(self, text, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element:
                element.send_keys(text)
            else:
                self.log.warning("Unable to send keys to the element")
                return

        except Exception as e:
            self.log.error(f"An unexpected exception occurred: {str(e)}")
            print_stack()

    # To make sure element is presented on the page
    def is_element_present(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                return True
            else:
                return False
        except Exception as e:
            self.log.error(f"WebDriverException occurred: {e}")
            return False

    # To check if elements are on the page
    def elements_present(self, locator, by_type="id"):
        """
        Checks if one or more web elements are present on the page.

        :param locator: The locator to identify the web elements.
        :param by_type: The By object type to use for locating the elements. ("id", "xpath", "css_selector", etc.)
        :return: True if one or more elements are found, else False.
        """
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info(
                    f"Elements are presented locator: {locator} and locator type: {
                        by_type
                    }"
                )
                return True
            else:
                self.log.warning(f"Found {len(element_list)} elements")
                return False
        except Exception as e:
            self.log.error(f"Exception occurred: {e}")
        return False

    def wait_for_element(
        self, locator, locator_type="id", timeout=3, poll_frequency=0.5
    ):
        """Waits for an element to be visible on the web page.

        Args:
            locator (str): The locator for the element to be found.
            locator_type (str): Type of locator (id, name, xpath, etc.). Default is "id".
            timeout (int): Duration to wait before timing out. Default is 3 seconds.
            poll_frequency (float): Frequency to poll the DOM. Default is 0.5 seconds.

        Returns:
            Optional[WebElement]: The WebElement if found, else None.
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info(
                f"Waiting for {timeout} seconds for element to appear: {locator}"
            )
            wait = WebDriverWait(
                self.driver,
                timeout=timeout,
                poll_frequency=poll_frequency,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException,
                ],
            )
            element = wait.until(expected_conditions.visibility_of_element_located((by_type, locator)))

            self.log.info(
                f"Element appeared on the web page using locator: {
                    locator
                } and locator_type: {locator_type}"
            )

        except Exception as e:
            self.log.error(f"An unexpected error occurred: {e}")

        return element

    def scroll_page_up(self, pixels):
        y = -pixels
        x = 0
        try:
            self.driver.execute_script(
                "window.scrollTo(arguments[0],arguments[1]);", x, y
            )
            self.log.info(f"Scrolled up by {pixels} pixels")
        except Exception as e:
            self.log.error(f"Exception occurred - {e}")

    def scroll_page_down(self, pixels):
        x = 0
        try:
            self.driver.execute_script("window.scrollTo(arguments[0],arguments[1]);", x, pixels)
            self.log.info(f"Scrolled down by {pixels} pixels")

        except Exception as e:
            self.log.error(f"Exception occurred - {e}")

    def scroll_page_bottom(self):
        try:
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.log.info("Scrolled to the bottom of the page")
        except Exception as e:
            self.log.error(f"Exception occurred - {e}")

    def scroll_page_top(self):
        try:
            self.driver.execute_script("window.scrollTo(0,0);")
            self.log.info("Scrolled to the top of the page")
        except Exception as e:
            self.log.error(f"Exception occurred - {e}")


    def scroll_into_view(
        self,
        locator,
        locator_type="id",
    ):
        element = self.get_element(locator, locator_type)
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true)", element)
            self.log.info(f"Scrolled into view - {element}")
        except Exception as e:
            self.log.error(f"Exception occurred - {e}")

    def delete_keys(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element:
                element.clear()
        except Exception as e:
            self.log.error(f"An unexpected exception occurred: {str(e)}")
            print_stack()

    def verify_page_title(self, title_to_verify) -> bool:
        """
        Verify page title

        :param title_to_verify: Title on the page that needs to be verified
        """

        try:
            actual_title = self.get_title()
            if actual_title is not None:
                return self.utility.verify_text_contains(actual_title, title_to_verify)
            else:
                return False
        except Exception as e:
            self.log.error(f"Error occurred - {e}")
            print_stack()
            return False
