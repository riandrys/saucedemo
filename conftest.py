import pytest
from saucedemo.utils.browser import get_browser


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on (chrome, firefox, etc.)")
    parser.addoption("--headless", action="store_true", default=False, help="Run tests in headless mode")
    parser.addoption("--mobile", action="store", default=None, help="Emulate mobile device (e.g., iPhone X)")


@pytest.fixture(scope='class')
def init_driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    mobile = request.config.getoption("--mobile")

    driver = get_browser(browser, headless, mobile)
    request.cls.driver = driver
    yield
    driver.quit()
