# Login Test Cases – Sauce Demo

## 1. Overview

This document contains manual test cases designed to verify the login functionality of the Sauce Demo application.

Testing covers valid authentication, invalid credentials, locked-out users, and input validation.

## 2. Test Environment

| Attribute    | Details                   |
| ------------ | ------------------------- |
| Application  | Sauce Demo                |
| Browser      | Google Chrome 157.0       |
| Testing Type | Manual Functional Testing |

## 3. Test Cases

### TC-LOGIN-001 – Login with Valid Credentials

| Attribute         | Details                                                |
| ----------------- | ------------------------------------------------------ |
| Preconditions     | User is on the login page.                             |
| Test Data         | Valid username and password                            |
| Steps             | Enter valid credentials and click Login.               |
| Expected Result   | User is successfully redirected to the inventory page. |
| Historical Status | Passed                                                 |

### TC-LOGIN-002 – Login with Invalid Password

| Attribute         | Details                                                          |
| ----------------- | ---------------------------------------------------------------- |
| Preconditions     | User is on the login page.                                       |
| Test Data         | Valid username and invalid password                              |
| Steps             | Enter the credentials and click Login.                           |
| Expected Result   | Login is rejected and an appropriate error message is displayed. |
| Historical Status | Passed                                                           |

### TC-LOGIN-003 – Login with Invalid Username

| Attribute         | Details                                                                                             |
| ----------------- | --------------------------------------------------------------------------------------------------- |
| Preconditions     | User is on the login page.                                                                          |
| Test Data         | Invalid username and password                                                                       |
| Steps             | Enter invalid credentials and click Login.                                                          |
| Expected Result   | Login is rejected.                                                                                  |
| Historical Status | Recorded in historical test scenarios; individual execution result not separately established here. |

### TC-LOGIN-004 – Login with Locked-Out User

| Attribute         | Details                                                  |
| ----------------- | -------------------------------------------------------- |
| Preconditions     | User is on the login page.                               |
| Test Data         | `locked_out_user` with its valid password                |
| Steps             | Enter the credentials and click Login.                   |
| Expected Result   | Login is rejected and the locked-out error is displayed. |
| Historical Status | Passed                                                   |

### TC-LOGIN-005 – Login with Empty Username

| Attribute         | Details                                                         |
| ----------------- | --------------------------------------------------------------- |
| Preconditions     | User is on the login page.                                      |
| Test Data         | Empty username and valid password                               |
| Steps             | Leave the username empty, enter a password, and click Login.    |
| Expected Result   | Login is rejected with an appropriate validation message.       |
| Historical Status | Not individually confirmed in the available historical records. |

### TC-LOGIN-006 – Login with Empty Password

| Attribute         | Details                                                         |
| ----------------- | --------------------------------------------------------------- |
| Preconditions     | User is on the login page.                                      |
| Test Data         | Valid username and empty password                               |
| Steps             | Enter a username, leave the password empty, and click Login.    |
| Expected Result   | Login is rejected with an appropriate validation message.       |
| Historical Status | Not individually confirmed in the available historical records. |

## 4. Historical Execution Summary

The original manual testing workbook recorded:

| Result              |  Count |
| ------------------- | -----: |
| Passed              |      8 |
| Failed              |      1 |
| No recorded status  |      2 |
| **Total scenarios** | **11** |

The six detailed test cases above provide representative examples of the login testing performed. They are not a replacement for the complete original 11-scenario execution record.

## 5. Notes

- Historical results are preserved rather than presented as newly executed tests.
- The two scenarios without recorded status are not counted as passed or failed.
- Additional test cases can be added as the testing scope expands.
