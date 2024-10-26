"""
Locators for elements on the TokensFarm and Hord applications.
"""

from selenium.webdriver.common.by import By


class TokensFarmLocators:
    """Locators for elements on the TokensFarm application page."""

    # CSS and XPath selectors for the chain dropdown element
    CHAIN_DROPDOWN_CSS = (By.CSS_SELECTOR, "#farm-chain > div")
    CHAIN_DROPDOWN_XPATH = (By.XPATH, "//*[@id='farm-chain']/div")


class HordLocators:
    """Locators for elements on the Hord application pages."""

    SIDEBAR_TOGGLE = (
        By.CSS_SELECTOR,
        ".sidebar-toggle-wrapper .side-bar-toggler.pointer",
    )
    SIDEBAR_CONTAINER = (By.CSS_SELECTOR, ".duf-aside")
    FAQ_SECTION = (By.CSS_SELECTOR, "#eth-staking-faq .faq-wrapper")

    # Locator for the Last Airdrops section with a shorter XPath
    LAST_AIRDROPS = (By.XPATH, "//*[@id='root']/div[3]/div[2]/div[2]/section[2]/div[2]")
