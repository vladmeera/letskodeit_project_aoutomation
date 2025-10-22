import os
from datetime import date, datetime
from time import time
from traceback import print_stack

from selenium.common.exceptions import (
    ElementNotSelectableException,
    ElementNotVisibleException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from utilities.custom_logger import custom_logger as cl

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
        self.driver = driver

    def navigate_page(self, direction: str = "back"):
        """
        Directions:
            back
            forward
            refresh
        """

        if direction.lower() == "back":
            self.driver.back()
            self.log.info("<-- GOING BACK <--")

        elif direction.lower() == "forward":
            self.driver.forward()
            self.log.info("--> GOING FORWARD -->")

        elif direction.lower() == "refresh":
            self.driver.refresh()
            self.log.info("--- REFRESHING THE PAGE ---")

        else:
            self.log.warning("Wrong direction")

    def screenshot(self, result_message: str = "screenshot"):
        """
        Attempts to take a screenshot and save it to the specified path.
        """
        result_message_lower = result_message.lower()
        result_message_final = result_message_lower.replace(" ", "_")

        current_date: date = datetime.now().date()
        file_name = (
            f"{result_message_final}_{current_date}_{str(round(time() * 1000))}.png"
        )
        screenshots_directory = "../screenshots/"
        relative_path = f"{screenshots_directory}{file_name}"
        current_directory = os.path.dirname(__file__)
        destination_path = os.path.join(current_directory, relative_path)
        destination_directory = os.path.join(current_directory, screenshots_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            self.driver.save_screenshot(destination_path)
            self.log.info(
                f"Screenshot saved to: {destination_path}. Screenshot: {file_name}"
            )

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
            self.log.error(f"\nError occurred: {e}\n")

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

        if locator_type in list_of_locators:
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
            self.log.info(f"Using locator type: {locator_type}, parsed as By.{by_type}")
            return by_type
        else:
            self.log.warning(
                f"Wrong locator type: {locator_type}! List of all locators: {
                    list_of_locators
                }"
            )
            return None

    # To find an element (default locator type is ID)
    def get_element(self, locator, locator_type="id"):
        element = None
        try:
            self.log.info("--> --> --> LOOKING FOR THE ELEMENT <-- <-- <--")
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                self.log.info(
                    f"The element was found! Locator: {locator} | Locator_type: {
                        locator_type
                    }"
                )
                return element
            else:
                return element

        except Exception as e:
            self.log.error(f"Exception occurred while searching for the element | {e}")
            return element

    def get_elements(self, locator, locator_type="id"):
        elements = None
        try:
            self.log.info("--> --> --> LOOKING FOR ELEMENTS <-- <-- <--")
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            if len(elements) > 0:
                self.log.info(f"Successfully found {len(elements)} elements!")
                return elements
            else:
                self.log.info(
                    f"Found {
                        len(elements)
                    } elements. Try another locator or locator type"
                )
                return elements

        except Exception as e:
            self.log.error(f"WebDriverException occurred: {e}")
            return elements

    def click_element(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element:
                element.click()
                self.log.info(
                    "-------------------| Clicked on the element |--------------------"
                )
                self.log.info(
                    "-------------------------------------------------------------\n"
                )
            else:
                self.log.warning(
                    "--------------------- Unable to click on the element ---------------------------"
                )
                self.log.warning(
                    "----------------------------------------------------------------------------\n"
                )
                return
        except Exception as e:
            self.log.debug(f"An unexpected exception occurred: {str(e)}")
            print_stack()

    def send_keys_element(self, text, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element:
                element.send_keys(text)
                self.log.info(
                    f"-----------------|Sent '{
                        text
                    }' to the element |---------------------"
                )
                self.log.info(
                    "----------------------------------------------------------------------------\n"
                )

            else:
                self.log.warning(
                    "------------ Unable to send keys to the element -------------------"
                )
                self.log.warning(
                    "----------------------------------------------------------------------------\n"
                )

                return

        except Exception as e:
            self.log.critical(f"An unexpected exception occurred: {str(e)}")
            print_stack()

    # To make sure element is presented on the page
    def is_element_present(self, locator, locator_type="id"):
        self.log.info("Trying to locate the element on the page...")
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info("Element appeared on the page!")
                return True
            else:
                self.log.warning("Element did not appear on the page...")
                return False
        except Exception as e:
            self.log.critical(f"WebDriverException occurred: {e}")
            return False

    # To check if elements are on the page
    def are_elements_present(self, locator, by_type="id"):
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
                self.log.warning(
                    f"Elements aren't presented on the page using locator: {
                        locator
                    } and locator type: {by_type}"
                )
                return False
        except Exception as e:
            self.log.critical(f"Exception occurred: {e}")
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
            element = wait.until(ec.visibility_of_element_located((by_type, locator)))

            self.log.info(
                f"Element appeared on the web page using locator: {
                    locator
                } and locator_type: {locator_type}"
            )

        except Exception as e:
            self.log.critical(f"An unexpected error occurred: {e}")
        finally:
            if not element:
                print_stack()
        return element

    def scroll_page(
        self,
        locator=None,
        locator_type="id",
        direction="no",
        x=0,
        y=0,
        into_view=False,
        to_bottom=False,
        to_top=False,
    ):
        self.log.info(
            "-----------------------------------------------------------------"
        )
        self.log.info(
            "--------------------| START SCROLLING |--------------------------"
        )
        direction_dictionary = {"direction": ("no", "up", "down")}

        def is_into_view():
            pass

        if direction.lower() == "no":
            if into_view:
                element = self.get_element(locator, locator_type)
                self.driver.execute_script("arguments[0].scrollIntoView(true)", element)
                self.log.info(f"Scrolled into view | Element - {element}")

            elif to_bottom:
                self.driver.execute_script(
                    "window.scrollTo(0,document.body.scrollHeight)"
                )
                self.log.info("Scrolled to the bottom of the page")

            elif to_top:
                self.driver.execute_script("window.scrollTo(0,0);")
                self.log.info("Scrolled to the top of the page")

        elif direction.lower() == "up":
            y = -y
            self.driver.execute_script(
                "window.scrollTo(arguments[0],arguments[1]);", x, y
            )
            self.log.info(f"Scrolled up by {y} pixels")

        elif direction.lower() == "down":
            self.driver.execute_script(
                "window.scrollTo(arguments[0],arguments[1]);", x, y
            )
            self.log.info(f"Scrolled down by {y} pixels")

        else:
            self.log.warning("!!! WRONG DIRECTION !!!")

        self.log.info(
            "--------------------------| END SCROLLING |---------------------------------"
        )
        self.log.info(
            "----------------------------------------------------------------------------"
        )

    def delete_keys(self, locator, locator_type="id"):
        try:
            element = self.get_element(locator, locator_type)
            if element:
                element.clear()
                self.log.info(
                    "-----------------|Deleted keys from the element |---------------------"
                )
                self.log.info(
                    "----------------------------------------------------------------------------\n"
                )

        except Exception as e:
            self.log.critical(f"An unexpected exception occurred: {str(e)}")
            print_stack()
