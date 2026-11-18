# Test Plan – Sauce Demo

## 1. Introduction

This test plan defines the scope, objectives, testing approach, environment, and execution criteria for manual testing of the Sauce Demo web application.

The purpose is to verify key e-commerce functionality and identify defects that may affect the user experience.

## 2. Test Objectives

- Verify successful and unsuccessful user authentication.
- Validate product inventory and product information.
- Verify shopping cart operations.
- Validate the checkout workflow.
- Identify functional and usability issues.
- Record defects with reproducible steps and supporting evidence.

## 3. Scope of Testing

### In Scope

| Module           | Testing Coverage                                         |
| ---------------- | -------------------------------------------------------- |
| Login            | Valid credentials, invalid credentials, locked-out users |
| Inventory        | Product listings, names, descriptions, and images        |
| Shopping Cart    | Adding and removing products                             |
| Checkout         | Customer information and order workflow                  |
| Input Validation | Empty and invalid form inputs                            |

### Out of Scope

- Payment gateway integration.
- Production performance testing.
- Cross-browser compatibility beyond the recorded environment.
- Security penetration testing.

## 4. Test Approach

The testing activities use a combination of:

**Functional Testing**

- Execute predefined test cases.
- Compare actual results against expected results.
- Record pass and fail outcomes.

**Negative Testing**

- Use invalid credentials and unexpected inputs.
- Verify that invalid operations are rejected appropriately.

**Exploratory Testing**

- Investigate application behavior beyond predefined test cases.
- Explore product, cart, and checkout workflows.
- Record unexpected behavior and potential defects.

## 5. Test Environment

| Component      | Configuration                  |
| -------------- | ------------------------------ |
| Application    | Sauce Demo                     |
| URL            | https://www.saucedemo.com/     |
| Browser        | Google Chrome 157.0            |
| Testing Method | Manual                         |
| Test Accounts  | Sauce Demo predefined accounts |

## 6. Entry Criteria

Testing can begin when:

- The application is accessible.
- Test accounts are available.
- Test scenarios and expected results are documented.
- The browser environment is ready.

## 7. Exit Criteria

Testing activities are considered complete when:

- Planned test scenarios have been executed or their status documented.
- Identified defects have been recorded.
- Failed and inconclusive scenarios are clearly distinguished.
- Execution results have been summarized.

## 8. Defect Management

Identified defects are documented with:

- Defect ID
- Title and description
- Preconditions
- Steps to reproduce
- Expected result
- Actual result
- Severity and priority
- Test environment

## 9. Risks and Limitations

- Sauce Demo uses predefined test accounts with intentionally different behaviors.
- Defects observed with a specific test account may not affect other accounts.
- Historical execution records may not contain complete results for every scenario.
- Test results reflect the recorded learning environment and execution period.

## 10. Deliverables

- Manual test cases
- Exploratory testing report
- Bug reports
- Test execution summary
