import sys
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--node_port", action="store", default="5555")
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--platform", action="store", default="windows")


@pytest.fixture(scope="function")
def driver(pytestconfig):
    is_debug = bool(pytestconfig.getoption("debug"))

    # Local driver
    if is_debug:
        driver = webdriver.Chrome()

    # Grid Remote: send arguments to Hub
    else:
        node_port = pytestconfig.getoption("node_port")
        browser_name = pytestconfig.getoption("browser")
        platform_name = pytestconfig.getoption("platform")

        driver = webdriver.Remote(
            command_executor="http://localhost:5000/wd/hub",
            desired_capabilities={"browserName": browser_name,
                                  "platform": platform_name,
                                  "node": node_port}
        )

    yield driver
    driver.quit()
