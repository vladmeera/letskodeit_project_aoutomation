import pytest
from selenium import webdriver
from utilities.custom_logger import custom_logger as cl
from base.webdriverfactory import WebDriverFactory

log = cl()

@pytest.fixture(scope='class')
def one_time_setup(request, browser):
    wdf = WebDriverFactory(browser)
    driver = wdf.get_webdriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture()
def setup():
    print('It runs before each test')
    yield
    print('It runs after each test')

def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help='Choose your operating system')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')