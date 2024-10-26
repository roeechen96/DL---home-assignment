"""
conftest module - sets up and tears down the browser environment for tests.
"""

import logging
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@pytest.fixture
def setup_browser() -> Generator[WebDriver, None, None]:
    """
    Fixture to initialize and yield a Chrome WebDriver for browser-based tests.
    Sets up and maximizes the browser window and tears down after tests.

    Yields:
        WebDriver: A Selenium WebDriver instance for Chrome.
    """
    print("Fixture is being used")
    logger.debug("Setting up the Chrome WebDriver")
    try:
        driver: WebDriver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install())
        )
        driver.maximize_window()
        logger.debug("Chrome WebDriver setup complete")
    except Exception as e:
        logger.error("Error setting up Chrome WebDriver: %s", e)
        raise e

    yield driver

    logger.debug("Tearing down the Chrome WebDriver")
    try:
        driver.quit()
        logger.debug("Chrome WebDriver teardown complete")
    except Exception as e:
        logger.error("Error tearing down Chrome WebDriver: %s", e)
        raise e
