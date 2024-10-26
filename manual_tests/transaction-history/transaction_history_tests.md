# Test Suite: Transaction History Tab - ChainPort App

This document provides the test suite for the Transaction History tab on the ChainPort App, focusing on UI, functional, and data validation tests.

---

## Objective

To verify that the **Transaction History** tab on the ChainPort App displays all transaction details accurately and that each interactive element functions as expected. The test suite covers UI, functional, and data integrity checks when viewing transaction history with a connected wallet.

---

## Test Cases

### 1. UI and Layout Verification

- **Title**: Verify Transaction History page layout and elements.
- **Preconditions**: User is logged in and connected with a MetaMask wallet.
- **Steps**:
  1. Navigate to the Transaction History tab.
  2. Verify the presence of the following elements:
      - Page title (e.g., “Transaction History”)
      - Filter options (Date range, Transaction type, etc.)
      - Transaction list (rows with individual transactions)
      - Columns such as Date, Transaction ID, Amount, Status, etc.
  3. Check that all elements are displayed and aligned properly.
- **Expected Result**: All UI elements are present, correctly labeled, and aligned.

### 2. Transaction Data Display

- **Title**: Verify each transaction entry displays accurate details.
- **Preconditions**: User is logged in and has transaction history in the connected account.
- **Steps**:
  1. Check the transaction details for each entry:
      - Date
      - Transaction ID
      - Amount
      - Status (e.g., Completed, Pending, Failed)
  2. Cross-reference the displayed data with transaction records from the blockchain (if accessible).
- **Expected Result**: All transaction details match the records, with no missing or incorrect information.

### 3. Filter Functionality - Date Range

- **Title**: Verify filtering transactions by date range.
- **Preconditions**: User is logged in and has multiple transactions across various dates.
- **Steps**:
  1. Set a specific date range using the Date Filter.
  2. Apply the filter.
  3. Verify that only transactions within the selected date range are displayed.
- **Expected Result**: Only transactions within the selected date range are shown.

### 4. Filter Functionality - Transaction Type

- **Title**: Verify filtering transactions by type (e.g., Transfers, Deposits).
- **Preconditions**: User is logged in and has transactions of different types.
- **Steps**:
  1. Select a transaction type using the Type Filter (e.g., Transfers).
  2. Apply the filter.
  3. Verify that only transactions of the selected type are displayed.
- **Expected Result**: Only transactions matching the selected type are displayed.

### 5. Pagination

- **Title**: Verify pagination functionality in Transaction History.
- **Preconditions**: User is logged in and has more transactions than can be displayed on a single page.
- **Steps**:
  1. Navigate to the Transaction History tab.
  2. Scroll down and verify the presence of pagination controls (e.g., Next, Previous).
  3. Click on the Next button to view subsequent pages.
  4. Verify that transactions update correctly with each page change.
- **Expected Result**: Pagination works as expected, displaying the appropriate set of transactions per page.

### 6. Transaction Details Modal/Pop-up

- **Title**: Verify transaction details modal/pop-up.
- **Preconditions**: User is logged in and has at least one transaction displayed.
- **Steps**:
  1. Click on a transaction entry to view its details.
  2. Verify that a modal/pop-up opens with expanded details:
      - Full Transaction ID
      - Gas Fee
      - Status with timestamp
      - Blockchain information (e.g., token type, contract address)
  3. Close the modal.
- **Expected Result**: Transaction details modal opens with complete information and can be closed smoothly.

### 7. Data Refresh

- **Title**: Verify data refresh functionality on Transaction History tab.
- **Preconditions**: User is logged in and has recent transactions.
- **Steps**:
  1. Initiate a new transaction in the connected wallet.
  2. Refresh the Transaction History page.
  3. Verify that the new transaction appears in the list.
- **Expected Result**: New transactions are displayed after refreshing the page.

### 8. Error Handling - Failed Transactions

- **Title**: Verify error handling for failed transactions.
- **Preconditions**: User is logged in and has at least one failed transaction in the history.
- **Steps**:
  1. Locate a failed transaction in the list.
  2. Verify that it is clearly marked with a distinct status (e.g., red text or icon).
  3. Click on the transaction to view error details.
- **Expected Result**: Failed transactions are identifiable, and clicking on them provides additional error information.

---

### Notes

- **Connected Wallet**: Ensure the user is logged into ChainPort with a MetaMask wallet to access the Transaction History.
- **Cross-Platform Testing**: Test across different browsers and devices (if responsive design is implemented).
- **Security Checks**: Confirm that no sensitive data, such as private keys, is accessible within the Transaction History tab.
