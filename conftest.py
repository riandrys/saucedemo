import allure
import pytest

from saucedemo.config.browser import get_browser


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on (chrome, firefox, etc.)",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode",
    )
    parser.addoption(
        "--mobile",
        action="store",
        default=None,
        help="Emulate mobile device (e.g., iPhone X)",
    )


@pytest.fixture
def init_driver(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    mobile = request.config.getoption("--mobile")

    driver = get_browser(browser, headless, mobile)
    request.cls.driver = driver
    yield driver
    driver.quit()


# check if a test has failed
@pytest.fixture
def test_failed_check(request):
    yield
    # request.node is an "item" because we use the default
    # "function" scope
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed and request.node.rep_call.failed:
        driver = request.node.funcargs["init_driver"]
        image = driver.get_screenshot_as_png()
        allure.attach(
            image,
            name="screenshot",
            attachment_type=allure.attachment_type.PNG,
        )


# set up a hook to be able to check if a test has failed
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "rep_" + rep.when, rep)
