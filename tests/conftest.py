import pytest
from utilities.custom_logger import custom_logger as cl
from base.webdriverfactory import WebDriverFactory

log = cl()

@pytest.fixture(scope='class')
def one_time_setup(request, browser):
    web_driver = WebDriverFactory(browser)
    driver = web_driver.get_webdriver()
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture()
def setup():
    log.warning('   ')

    log.warning('------------------------------------------------------------------------------')
    log.warning('################################ RUNNING TEST ################################')
    log.warning('------------------------------------------------------------------------------')
    yield
    log.warning('-----------------------------------------------------------------------------------')
    log.warning('################################ STOP RUNNING TEST ################################')
    log.warning('-----------------------------------------------------------------------------------')
    log.warning('   ')

def pytest_addoption(parser):
    parser.addoption('--browser', help='Choose your browser')
    parser.addoption('--osType', help='Choose your operating system')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')