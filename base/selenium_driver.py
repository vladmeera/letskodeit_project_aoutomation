from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException,
    TimeoutException, WebDriverException, ElementNotInteractableException, StaleElementReferenceException,
)
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from typing import Optional
from traceback import print_stack
from utilities.custom_logger import custom_logger as cl
# from logging import DEBUG

class SeleniumDriver:

    log = cl()

    def __init__(self, driver: WebDriver):
        """
        Initializes the SeleniumDriver instance with the provided Webdriver.

        :param driver: The Selenium WebDriver instance used to interact with web elements.
        """
        self.driver = driver

    def get_by_type(self, locator_type: str):
        """
        Converts a locator type string to a Selenium By object for use in locating elements.

        :param locator_type: A string representing the type of locator (e.g., 'id', 'css_selector', 'xpath', etc.).
        :return: Corresponding Selenium By method for the provided locator type. Returns False if the locator type is not supported.
        """
        locatorType = locator_type.lower()
        if locatorType == "id":
            return By.ID
        elif (locatorType == "css_selector"
              or locatorType == "css selector"
              or locatorType == "css"):
            return By.CSS_SELECTOR
        elif locatorType == "xpath":
            return By.XPATH
        elif (locatorType == "class"
              or locatorType == "class_name"
              or locatorType == "class name"
              or locatorType == "classname"):
            return By.CLASS_NAME
        else:
            self.log.info("Locator type is not supported")
        return False

    # To find elements (default locator type is ID)
    def get_element(self, locator: str, locator_type: str ="id"):
        """
        Attempts to locate a single web element using the specified locator and locator type.

        :param locator: The locator to identify the web element.
        :param locator_type: The type of the locator (default is "id"). It can be other types like "name", "xpath", etc.
        :return: The web element if found, else None.
        """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            self.log.info(f"Found element with locator: {locator} and locator_type: {locator_type}")
            return element

        except NoSuchElementException:
            self.log.warning(f"Element not found using locator: {locator} and locator type: {locator_type}")

        except WebDriverException as e:
            self.log.critical(f"WebDriverException occurred: {str(e)}")
        return element


    def get_elements(self, locator: str, locator_type: str ="id"):
        """
        Attempts to locate multiple web elements using the specified locator and locator type.

        :param locator: The locator to identify the web elements.
        :param locator_type: The type of the locator (default is "id"). It can be other types like "name", "xpath", etc.
        :return: A list of web elements if found, else None.
        """
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            elements = self.driver.find_elements(by_type, locator)
            self.log.info(f"Found elements with locator: {locator} and locator_type: {locator_type}")
            return elements
        except NoSuchElementException:
            self.log.warning(f"Elements not found using locator: {locator}, and locator_type: {locator_type}")
        except WebDriverException as e:
            self.log.critical(f"WebDriverException occurred: {str(e)}")
        return None

    def click_element(self, locator: str, locator_type: str ="id") -> None:
        """
        Attempts to click on a web element located by the specified locator and locator type.

        :param locator: The locator to identify the web element.
        :param locator_type: The type of locator to use (default is "id"). It can be other types like "name", "xpath", etc.
        :return: None
        :raises: NoSuchElementException if the element is not found. ElementNotInteractableException if the element is not interactable. StaleElementReferenceException if the element is no longer attached to the DOM. WebDriverException for any driver-related issues.

        This method tries to find the specified web element and perform a click action on it.
        It handles exceptions to ensure that the appropriate error message is displayed
        if the element is not found or if there are driver-related issues.
        """
        try:
            element = self.get_element(locator, locator_type)
            if element:
                element.click()
                self.log.info(f"Clicked on element with locator: {locator} and locator_type: {locator_type}")
            else:
                self.log.info(f"Unable to click on element. Element with locator: {locator} and locator_type: {locator_type} not found.")
        except NoSuchElementException:
            self.log.warning(f"Element not found using locator: {locator} and locator_type: {locator_type}")
        except ElementNotInteractableException:
            self.log.warning(f"Element not interactable using locator: {locator} and locator_type: {locator_type}")
        except StaleElementReferenceException:
            self.log.critical(f"Element is stale using locator: {locator} and locator_type: {locator_type}")
        except WebDriverException as e:
            self.log.critical(f"WebDriverException occurred: {str(e)}")
        except Exception as e:
            self.log.debug(f"An unexpected exception occurred: {str(e)}")
            print_stack()

    def send_keys_element(self, text: str, locator: str, locator_type: str = "id") -> None:
        """
        Attempts to send text to a web element located by the specified locator and locator type.

        :param locator: The locator to identify the web element.
        :param text: The text to send to the web element.
        :param locator_type: The type of locator to use (default is "id"). It can be other types like "name", "xpath", etc.
        :return: None
        :raises: NoSuchElementException if the element is not found. ElementNotInteractableException if the element is not interactable. StaleElementReferenceException if the element is no longer attached to the DOM. WebDriverException for any driver-related issues.

        This method tries to find the specified web element and sends the given text to it.
        It handles exceptions to ensure that the appropriate error message is displayed
        if the element is not found or if there are driver-related issues.
        """
        try:
            element = self.get_element(locator, locator_type)
            if element:
                element.send_keys(text)
                self.log.info(f"Sent keys to element with locator: {locator} and locator_type: {locator_type}")
            else:
                self.log.info(
                    f"Unable to send keys to element. Element with locator: {locator} and locator_type: {locator_type} not found.")
        except NoSuchElementException:
            self.log.warning(f"Element not found using locator: {locator} and locator_type: {locator_type}")
        except ElementNotInteractableException:
            self.log.warning(f"Element not interactable using locator: {locator} and locator_type: {locator_type}")
        except StaleElementReferenceException:
            self.log.critical(f"Element is stale using locator: {locator} and locator_type: {locator_type}")
        except WebDriverException as e:
            self.log.critical(f"WebDriverException occurred: {str(e)}")
        except Exception as e:
            self.log.debug(f"An unexpected exception occurred: {str(e)}")
            print_stack()

    # To make sure element is presented on the page
    def is_element_presented(self, locator: str, locator_type: str = "id") -> bool:
        """
        Checks if a specific web element is present on the page.

        :param locator: The locator to identify the web element.
        :param locator_type: The By object type to use for locating the element. ("id", "xpath", "css_selector", etc.)
        :return: True if the element is found and presented on the page, else False.
        """
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                self.log.info(f"Element is presented using locator: {locator} and locator_type: {locator_type}")
                return True
            else:
                self.log.info(f"Element isn't presented on the page using locator: {locator} and locator_type: {locator_type}")
        except NoSuchElementException:
            self.log.warning(f"Element not found using locator: {locator}, and locator type: {locator_type}")
        except WebDriverException as e:
            self.log.critical(f"WebDriverException occurred: {str(e)}")
        return False

    # To check if elements are on the page
    def are_elements_presented(self, locator: str, by_type: str = "id") -> bool:
        """
        Checks if one or more web elements are present on the page.

        :param locator: The locator to identify the web elements.
        :param by_type: The By object type to use for locating the elements. ("id", "xpath", "css_selector", etc.)
        :return: True if one or more elements are found, else False.
        """
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                self.log.info(f"Elements are presented locator: {locator} and locator type: {by_type}")
                return True
            else:
                self.log.info(f"Elements aren't presented on the page using locator: {locator} and locator type: {by_type}")
        except NoSuchElementException:
            self.log.warning(f"Elements not found using locator: {locator} and locator type: {by_type}")
        except WebDriverException as e:
            self.log.critical(f"WebDriverException occurred: {str(e)}")
        return False

    def wait_for_element(self, locator: str, locator_type: str="id",
                       timeout: int = 10, poll_frequency: float = 0.5) -> Optional[WebElement]:
        """Waits for an element to be visible on the web page.

        Args:
            locator (str): The locator for the element to be found.
            locator_type (str): Type of locator (id, name, xpath, etc). Default is "id".
            timeout (int): Duration to wait before timing out. Default is 10 seconds.
            poll_frequency (float): Frequency to poll the DOM. Default is 0.5 seconds.

        Returns:
            Optional[WebElement]: The WebElement if found, else None.
        """
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info(f"Waiting for {timeout} seconds for element to appear: {locator}")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=[NoSuchElementException,
                                                                                           ElementNotVisibleException,
                                                                                           ElementNotSelectableException])
            element = wait.until(ec.visibility_of_element_located((by_type, locator)))

            self.log.info(f"Element appeared on the web page using locator: {locator} and locator_type: {locator_type}")

        except TimeoutException:
            self.log.warning(f"Element did not appear on the web page within {timeout} seconds.")
        except NoSuchElementException:
            self.log.warning("Element not found in the DOM.")
        except ElementNotVisibleException:
            self.log.warning("Element is not visible in the DOM.")
        except ElementNotSelectableException:
            self.log.warning("Element is not selectable in the DOM.")
        except Exception as e:
            self.log.critical(f"An unexpected error occurred: {e}")
        finally:
            if not element:
                print_stack()
        return element

