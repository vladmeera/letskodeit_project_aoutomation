from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By

class SeleniumDriver:
    def __init__(self, driver):
        """
        Initializes the SeleniumDriver instance with the provided Webdriver.

        :param driver: The Selenium WebDriver instance used to interact with web elements.
        """
        self.driver = driver

    def get_by_type(self, locator_type: str) -> bool:
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
            print("Locator type is not supported")
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
            return element

        except NoSuchElementException:
            print(f"Element not found using locator: {locator} and locator type: {locator_type}")

        except WebDriverException as e:
            print(f"WebDriverException occurred: {str(e)}")
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
            return elements
        except NoSuchElementException:
            print(f"Elements not found using locator: {locator}, and locator_type: {locator_type}")
        except WebDriverException as e:
            print(f"WebDriverException occurred: {str(e)}")
        return None

    # To make sure element is presented on the page
    def is_element_presented(self, locator: str, by_type: str) -> bool:
        """
        Checks if a specific web element is present on the page.

        :param locator: The locator to identify the web element.
        :param by_type: The By object type to use for locating the element. ("id", "xpath", "css_selector", etc.)
        :return: True if the element is found and presented on the page, else False.
        """
        try:
            element = self.driver.find_element(by_type, locator)
            if element is not None:
                print("Element is presented")
                return True
            else:
                print("Element isn't presented on the page!")
        except NoSuchElementException:
            print(f"Element not found using locator: {locator}, and locator type: {by_type}")
        except WebDriverException as e:
            print(f"WebDriverException occurred: {str(e)}")
        return False

    # To check if elements are on the page
    def are_elements_presented(self, locator: str, by_type: str) -> bool:
        """
        Checks if one or more web elements are present on the page.

        :param locator: The locator to identify the web elements.
        :param by_type: The By object type to use for locating the elements. ("id", "xpath", "css_selector", etc.)
        :return: True if one or more elements are found, else False.
        """
        try:
            element_list = self.driver.find_elements(by_type, locator)
            if len(element_list) > 0:
                print(f"Elements are found using: {by_type}")
                return True
            else:
                print("Elements are not found")
        except NoSuchElementException:
            print(f"Elements not found using locator: {locator} and locator type: {by_type}")
        except WebDriverException as e:
            print(f"WebDriverException occurred: {str(e)}")
        return False
