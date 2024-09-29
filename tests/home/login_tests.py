# import logging
from pages.home.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.custom_logger import custom_logger as cl
from unittest import TestCase
from base.selenium_driver import SeleniumDriver as Driver

class LoginTest(TestCase):

    # log = cl(logging.DEBUG)

    def test_valid_login(self):
        base_url = "https://www.letskodeit.com/"
        driver = webdriver.Chrome()
        driver.implicitly_wait(4)
        driver.maximize_window()
        driver.get(base_url)
        s_driver = Driver(driver)

        lp = LoginPage(driver)
        lp.login(
            email="va3zdkh68@mozmail.com",
            password='"%+eH3>@w8nPp,')

        profile_btn = s_driver.get_element("//button[@id='dropdownMenu1']", "xpath")
        # profile_btn = driver.find_element(By.XPATH, "//button[@id='dropdownMenu1']")
        if profile_btn is not None:
            print("Login successful")
        else:
            print("Login failed")

        driver.quit()
