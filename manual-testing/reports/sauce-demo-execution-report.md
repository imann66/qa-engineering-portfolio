# Sauce Demo – Manual Testing Execution Report

## 1. Overview

This report summarizes the historical manual testing execution of the Sauce Demo e-commerce application.

The report is based on the original QA training test records and documents the recorded execution outcomes, testing coverage, and identified defects.

**Application:** Sauce Demo
**Testing Type:** Manual Functional Testing
**Browser:** Google Chrome 157.0
**Test Account:** Predefined Sauce Demo test accounts
**Execution Record:** Historical QA training workbook

## 2. Execution Summary

A total of 11 test scenarios were recorded in the original test execution sheet.

| Test Status        |  Count |
| ------------------ | -----: |
| Passed             |      8 |
| Failed             |      1 |
| No Recorded Status |      2 |
| **Total**          | **11** |

Only scenarios with an explicitly recorded Passed or Failed status are included in the corresponding totals. Scenarios without a recorded status are not assumed to have passed or failed.

### Execution Status Distribution

- Passed: 72.7%
- Failed: 9.1%
- No Recorded Status: 18.2%

## 3. Testing Coverage

The manual testing activities covered the following areas:

- User authentication and login validation
- Product inventory and product information
- Shopping cart functionality
- Checkout workflow
- Input field behavior and validation
- Exploratory testing

## 4. Defect Summary

### BUG-001 – Last Name Field Affects First Name During Checkout

**Severity:** High
**Priority:** High
**Status:** Reported
**Testing Account:** problem_user

**Description:**

During checkout testing, interaction with the Last Name field affected the First Name field and prevented the expected checkout flow.

**Expected Result:**

The First Name and Last Name fields should accept and retain their respective values independently.

**Actual Result:**

Entering information in the Last Name field affected the First Name field, resulting in unexpected form behavior and preventing checkout from proceeding as expected.

**Reference:**

[BUG-001 – Detailed Bug Report](../sauce-demo/bug-reports/BUG-001.md)

## 5. Exploratory Testing Findings

The exploratory testing session using `problem_user` identified additional unexpected behavior:

- Product images did not consistently match their product information.
- A product description displayed unexpected code-like text.
- Only three products could be added to the cart during the recorded session.
- Product removal functionality was unavailable during the recorded session.

These observations require further investigation and are not counted as additional confirmed failed test cases in the 11-scenario execution summary.

See the [Exploratory Testing Report](../sauce-demo/exploratory-testing.md) for details.

## 6. Test Execution Assessment

The historical execution records demonstrate that the application was tested across several core e-commerce workflows.

The recorded failure and exploratory findings indicate areas requiring further investigation, particularly checkout form behavior and product inventory functionality.

## 7. Limitations

- This report summarizes historical test records rather than a newly executed test cycle.
- Two scenarios have no recorded execution status.
- Exploratory findings were observed using the `problem_user` account and should not automatically be generalized to other accounts.
- Screenshots and recordings were not included in the available execution records.
- Root causes of the reported defects have not been established.

## 8. Conclusion

The manual testing exercise provided practical experience in test execution, result recording, exploratory testing, defect identification, and documentation.

The results highlight the importance of maintaining traceable test records and distinguishing confirmed failures from incomplete execution records and exploratory observations.
