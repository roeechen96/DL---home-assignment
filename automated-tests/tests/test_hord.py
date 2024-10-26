"""
Tests for Hord web application, including sidebar expansion and FAQ visibility checks.
"""

import logging

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils.locators import HordLocators

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

HORD_URL = "https://staging-app.hord.fi"
HORD_REVENUE_SHARE_URL = "https://staging-app.hord.fi/revenue-share"


@allure.feature("Hord Automation")
@allure.story("Test the sidebar and FAQ functionality on Hord")
def test_sidebar_expansion(setup_browser: WebDriver) -> None:
    """
    Test the expansion and collapse functionality of the sidebar.

    Args:
        setup_browser (WebDriver): The WebDriver instance set up by the pytest fixture.
    """
    logger.info("Navigating to the Hord staging app...")
    setup_browser.get(HORD_URL)

    wait = WebDriverWait(setup_browser, 20)

    logger.info("Checking the initial sidebar state.")
    sidebar = wait.until(EC.presence_of_element_located(HordLocators.SIDEBAR_CONTAINER))
    initial_width = sidebar.value_of_css_property("min-width")
    assert initial_width in [
        "224px",
        "280px",
    ], f"Expected sidebar width to be 224px or 280px, but got {initial_width}"
    logger.info(
        "Sidebar confirmed to be expanded with initial width: %s", initial_width
    )

    logger.info("Attempting to collapse the sidebar by modifying the class directly.")
    setup_browser.execute_script(
        "document.querySelector('.duf-aside').classList.remove('sidebar-expanded');"
    )
    wait.until(lambda driver: sidebar.value_of_css_property("min-width") == "68px")
    collapsed_width = sidebar.value_of_css_property("min-width")
    assert (
        collapsed_width == "68px"
    ), f"Expected sidebar to collapse to 68px width, but got {collapsed_width}"
    logger.info("Sidebar successfully collapsed.")

    logger.info("Attempting to re-expand the sidebar by re-adding the class.")
    setup_browser.execute_script(
        "document.querySelector('.duf-aside').classList.add('sidebar-expanded');"
    )
    wait.until(
        lambda driver: sidebar.value_of_css_property("min-width") in ["224px", "280px"]
    )
    expanded_width = sidebar.value_of_css_property("min-width")
    assert expanded_width == initial_width, (
        f"Expected re-expanded width to match initial ({initial_width}), "
        f"but got {expanded_width}"
    )
    logger.info("Sidebar successfully re-expanded.")


@allure.feature("Hord Automation")
@allure.story("Test the FAQ section")
def test_faq_section(setup_browser: WebDriver) -> None:
    """
    Test the visibility of the FAQ section on the Hord application.

    Args:
        setup_browser (WebDriver): The WebDriver instance set up by the pytest fixture.
    """
    logger.info("Navigating to the Hord FAQ section...")
    driver: WebDriver = setup_browser
    driver.get(HORD_URL)

    try:
        with allure.step("Wait for the FAQ section to be visible"):
            logger.info("Waiting for FAQ section to be visible...")
            faq_section = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(HordLocators.FAQ_SECTION)
            )
            assert (
                faq_section.is_displayed()
            ), "FAQ section should be visible on the page"
            logger.info("FAQ section is visible on the page.")

    except TimeoutException:
        assert (
            False
        ), "FAQ section was not found or not visible within the timeout period"


## Bonus
@allure.feature("Hord Automation")
@allure.story("Test the Last Airdrops section on the Revenue Share page")
def test_last_airdrops(setup_browser: WebDriver) -> None:
    """
    Test the visibility of the Last Airdrops section on the Hord Revenue Share page.

    Args:
        setup_browser (WebDriver): The WebDriver instance set up by the pytest fixture.
    """
    logger.info("Navigating to the Hord Revenue Share page...")
    driver: WebDriver = setup_browser
    driver.get(HORD_REVENUE_SHARE_URL)

    try:
        with allure.step("Wait for the Last Airdrops section to be visible"):
            logger.info("Waiting for Last Airdrops section to be visible...")
            last_airdrops = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(HordLocators.LAST_AIRDROPS)
            )
            assert (
                last_airdrops.is_displayed()
            ), "Last Airdrops section should be visible on the page"
            logger.info("Last Airdrops section is visible on the page.")

    except TimeoutException:
        assert (
            False
        ), "Last Airdrops section was not found or did not become visible with the timeout period"
