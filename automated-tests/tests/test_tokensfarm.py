"""
Tests for TokensFarm web application, including checks for dropdown visibility and interactivity.
"""

import logging

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.locators import TokensFarmLocators

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

TOKENS_FARM_URL = "https://staging.tokensfarm.com/create#/staking"


@allure.feature("TokensFarm Automation")
@allure.story("Test the dropdown on TokensFarm")
def test_chain_dropdown_locators(setup_browser: WebDriver) -> None:
    """
    Test the functionality and visibility of the dropdown menu on the TokensFarm page.

    This test navigates to the TokensFarm URL, waits for the page to load,
    and verifies the dropdown menu's clickability and visibility using both CSS and XPath locators.

    Args:
        setup_browser (WebDriver): The WebDriver instance provided by the pytest fixture.
    """
    driver: WebDriver = setup_browser
    logger.info("Navigating to the TokensFarm URL...")
    driver.get(TOKENS_FARM_URL)

    WebDriverWait(driver, 30).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
    )

    # Locate the dropdown using CSS selector
    try:
        with allure.step("Locate the dropdown using CSS selector"):
            logger.info("Attempting to locate dropdown using CSS selector.")
            dropdown_css = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(TokensFarmLocators.CHAIN_DROPDOWN_CSS)
            )
            dropdown_css.click()
            logger.info("Dropdown located and clicked using CSS selector.")

    except TimeoutException:
        logger.error("Dropdown not found or not clickable using CSS selector.")
        assert False, "Dropdown should be clickable using CSS selector"

    # Verify dropdown visibility using XPath selector
    try:
        with allure.step("Verify dropdown visibility using XPath selector"):
            logger.info("Waiting for dropdown to be visible with XPath selector.")
            dropdown_xpath = WebDriverWait(driver, 15).until(
                EC.visibility_of_element_located(
                    TokensFarmLocators.CHAIN_DROPDOWN_XPATH
                )
            )
            assert (
                dropdown_xpath.is_displayed()
            ), "Dropdown should be visible after expanding with XPath selector"
            logger.info("Dropdown is visible using XPath selector.")

    except TimeoutException:
        logger.error("Dropdown not visible using XPath selector after clicking.")
        assert False, "Dropdown should be visible using XPath selector after expanding"
