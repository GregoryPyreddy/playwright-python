import pytest
import configparser
import os
from playwright.async_api import async_playwright

# Get the directory of the current file (conftest.py)
current_dir = os.path.dirname(os.path.realpath(__file__))
# Navigate to the root directory
root_dir = os.path.abspath(os.path.join(current_dir, "../.."))
# Path to the config.ini file
config_file = os.path.join(root_dir, "config.ini")

def pytest_addoption(parser):
    config = configparser.ConfigParser()
    config.read("config.ini")
    browser_default = config.get("pytest", "browser", fallback="chrome")
    test_case_default = config.get("pytest", "test_case", fallback="login_test")
    time_out_default = config.get("pytest", "time_out", fallback="10")
    name_space_default = config.get("pytest", "name_space", fallback="dev02")

    parser.addoption("--browser", action="store", default=browser_default, help="Specify the browser")
    parser.addoption("--test-case", action="store", default=test_case_default, help="Specify the test case")
    parser.addoption("--time-out", action="store", default=time_out_default, help="Specify the timeout in seconds")
    parser.addoption("--name_space", action="store", default=name_space_default, help="Specify the namespace we are running the test")

@pytest.fixture
async def browser_type(request):
    browser = request.config.getoption("--browser")
    return browser

@pytest.fixture
async def test_case(request):
    test_case = request.config.getoption("--test-case")
    return test_case

@pytest.fixture(scope="session")
def base_url(request):
    name_space = request.config.getoption("--name_space")
    url = f"url"
    return url

@pytest.fixture(scope="session")
async def playwright_context(browser_type):
    async with async_playwright() as p:
        if browser_type == "chrome":
            browser =p.chromium.launch(headless=False)
        elif browser_type == "firefox":
            browser =p.firefox.launch(headless=False)
        else:
            raise Exception(f"Browser '{browser_type}' is not supported")
        yield browser
        await browser.close()

@pytest.fixture(scope="function")
async def browser_page(playwright_context):
    page = await playwright_context.new_page()
    yield page
    await page.close()

class TestContext:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait