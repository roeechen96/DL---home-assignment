# Home Assignment for Hord and TokensFarm Automated Tests

The project took approximately 9 hours to complete

## Table of Contents

- [Contact](#contact)
- [Dependencies](#dependencies)
- [Project Details](#project-details)
  - [Hord Tests](#hord-tests)
  - [TokensFarm Tests](#tokensfarm-tests)
- [Generating Allure Reports](#generating-allure-reports)
- [Running Tests](#running-tests)

## Contact

For questions or issues, please reach out to [roee960001@gmail.com].

## Dependencies

The project relies on the following Python libraries and tools:

- **Selenium**: For browser automation and interaction.
- **Pytest**: Testing framework for organizing and running tests.
- **Allure-Pytest**: For generating detailed reports.
- **Webdriver-Manager**: Manages Chrome WebDriver binaries.

## Project Details

## Hord Tests

test_sidebar_expansion: Verifies that the sidebar in the Hord app can expand and collapse.
test_faq_section: Checks if the FAQ section is visible and loads correctly.
test_last_airdrops: Confirms the visibility of the Last Airdrops section on the Hord Revenue Share page.

## TokensFarm Tests

test_chain_dropdown_locators: Ensures the TokensFarm dropdown is clickable and visible using both CSS and XPath locators.

## Generating Allure Reports

```bash
allure serve allure-results

## Running Tests

```bash
pytest --alluredir=allure-results
