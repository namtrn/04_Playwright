import logging
import pytest
from playwright.sync_api import Page

logger = logging.getLogger('__Test Login__')
logger.setLevel(logging.INFO)

@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args
    }

@pytest.fixture(scope="function", autouse=True)
def set_up_page(page: Page):
    logger.info(msg="Open Browser")
    page.goto("https://www.saucedemo.com/")
    yield page
    logger.info(msg="Close Browser")
    page.close()

