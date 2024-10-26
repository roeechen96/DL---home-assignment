# Test Suite: Protocol Selection and Fees Based on Thresholds - ChainPort App

This document provides the test suite for verifying protocol selection (ChainPortX vs. CCTP) and associated fees based on transaction thresholds on the ChainPort App.

---

## Objective

To verify that the correct protocol (ChainPortX or CCTP) and associated fees are applied based on the transaction amount and the chain being used (Ethereum, Avalanche, or Optimism).

---

## Test Cases

### 1. Protocol Selection on Ethereum Chain (Below Threshold)

- **Title**: Verify protocol selection and fees on Ethereum when porting amount is **below the threshold**.
- **Preconditions**:
  - User is attempting to port from Ethereum.
  - Amount is below the threshold.
- **Steps**:
    1. Initiate a porting transaction on Ethereum.
    2. Enter an amount **below the threshold**.
    3. Verify that **CCTP** is automatically selected as the protocol.
    4. Confirm that the correct **CCTP fee** is displayed.
- **Expected Result**:
  - CCTP protocol is selected.
  - Fees align with CCTP’s fee structure for below-threshold amounts.

### 2. Protocol Selection on Ethereum Chain (Above Threshold)

- **Title**: Verify protocol selection and fees on Ethereum when porting amount is **above the threshold**.
- **Preconditions**:
  - User is attempting to port from Ethereum.
  - Amount is above the threshold.
- **Steps**:
    1. Initiate a porting transaction on Ethereum.
    2. Enter an amount **above the threshold**.
    3. Verify that **ChainPortX** is automatically selected as the protocol.
    4. Confirm that the correct **ChainPortX fee** is displayed.
- **Expected Result**:
  - ChainPortX protocol is selected.
  - Fees match ChainPortX’s structure for above-threshold transactions.

### 3. Protocol Selection on Avalanche Chain (Only CCTP Supported)

- **Title**: Verify protocol selection and fees on Avalanche where only CCTP is supported.
- **Preconditions**:
  - User is porting on the Avalanche chain.
- **Steps**:
    1. Initiate a porting transaction on Avalanche.
    2. Enter any amount (below or above the threshold).
    3. Verify that **CCTP** is selected as the default protocol.
    4. Confirm that the appropriate **CCTP fee** is displayed.
- **Expected Result**:
  - CCTP protocol is automatically selected.
  - CCTP fee is accurately applied regardless of the amount.

### 4. Protocol Selection on Optimism Chain (Below Threshold)

- **Title**: Verify protocol selection and fees on Optimism for amounts **below the threshold**.
- **Preconditions**:
  - User is attempting to port from Optimism.
  - Amount is below the threshold.
- **Steps**:
    1. Initiate a porting transaction on Optimism.
    2. Enter an amount **below the threshold**.
    3. Verify that **CCTP** is selected as the protocol.
    4. Confirm that the correct **CCTP fee** is displayed.
- **Expected Result**:
  - CCTP protocol is selected.
  - CCTP’s below-threshold fee structure applies.

### 5. Protocol Selection on Optimism Chain (Above Threshold)

- **Test Case ID**: PROTOCOL-OPT-02
- **Title**: Verify protocol selection and fees on Optimism for amounts **above the threshold**.
- **Preconditions**:
  - User is attempting to port from Optimism.
  - Amount is above the threshold.
- **Steps**:
    1. Initiate a porting transaction on Optimism.
    2. Enter an amount **above the threshold**.
    3. Verify that **ChainPortX** is automatically selected as the protocol.
    4. Confirm that the correct **ChainPortX fee** is displayed.
- **Expected Result**:
  - ChainPortX protocol is selected.
  - ChainPortX’s above-threshold fee structure applies.

---

### Notes

- **Threshold Validation**: Ensure each threshold is applied correctly per chain and protocol.
- **Fee Verification**: Confirm that fees displayed in the UI match the expected fees based on the selected protocol and amount range.
- **Cross-Protocol Testing**: Validate that switching between protocols where applicable (Ethereum and Optimism) adheres to the threshold logic accurately.

This test suite provides a minimal but comprehensive check for the protocol and fee logic based on thresholds across Ethereum, Avalanche, and Optimism chains.
"""
