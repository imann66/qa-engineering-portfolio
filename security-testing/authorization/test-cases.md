# Authorization Test Cases

## 1. Overview

This document describes the automated test scenarios used to validate authentication, authorization, resource access, and input handling in the sample Flask API.

**Endpoint:** `GET /api/accounts/{account_id}`

**Test framework:** Pytest

## 2. Test Cases

### A. Positive Authorization

| Test ID  | Scenario                       | Test Data                | Expected Result          |
| -------- | ------------------------------ | ------------------------ | ------------------------ |
| AUTH-001 | Alice accesses her own account | Alice token, account 101 | HTTP 200; owner is Alice |
| AUTH-002 | Bob accesses his own account   | Bob token, account 202   | HTTP 200; owner is Bob   |

### B. Negative Authorization

| Test ID  | Scenario                               | Test Data                | Expected Result     |
| -------- | -------------------------------------- | ------------------------ | ------------------- |
| AUTH-003 | Alice attempts to access Bob's account | Alice token, account 202 | HTTP 403; Forbidden |
| AUTH-004 | Bob attempts to access Alice's account | Bob token, account 101   | HTTP 403; Forbidden |

Additional assertions verify that unauthorized responses do not expose `balance`, `owner`, or `account_id`.

### C. Authentication Validation

| Test ID  | Scenario                     | Test Data            | Expected Result |
| -------- | ---------------------------- | -------------------- | --------------- |
| AUTH-005 | Missing authorization header | No header            | HTTP 401        |
| AUTH-006 | Empty authorization token    | Empty token          | HTTP 401        |
| AUTH-007 | Invalid authorization token  | `invalid-token`      | HTTP 401        |
| AUTH-008 | Unknown user token           | `unknown-user-token` | HTTP 401        |

### D. Resource Existence

| Test ID  | Scenario                   | Test Data                | Expected Result             |
| -------- | -------------------------- | ------------------------ | --------------------------- |
| AUTH-009 | Access nonexistent account | Alice token, account 999 | HTTP 404; Account not found |

### E. Invalid Account ID Format

| Test ID  | Scenario                      | Test Data | Expected Result |
| -------- | ----------------------------- | --------- | --------------- |
| AUTH-010 | Alphabetic account ID         | `abc`     | HTTP 404        |
| AUTH-011 | Invalid text account ID       | `invalid` | HTTP 404        |
| AUTH-012 | Mixed alphanumeric account ID | `12abc`   | HTTP 404        |

### F. Token Case and Whitespace Validation

| Test ID  | Scenario                          | Test Data       | Expected Result |
| -------- | --------------------------------- | --------------- | --------------- |
| AUTH-013 | Incorrect token capitalization    | `Alice-token`   | HTTP 401        |
| AUTH-014 | Token with surrounding whitespace | ` alice-token ` | HTTP 401        |

### G. Negative and Zero Account IDs

| Test ID  | Scenario            | Test Data | Expected Result |
| -------- | ------------------- | --------- | --------------- |
| AUTH-015 | Negative account ID | `-101`    | HTTP 404        |
| AUTH-016 | Zero account ID     | `0`       | HTTP 404        |

## 3. Test Implementation

Automated tests are implemented in:

`automation/playwright/tests/test_authorization.py`

The suite uses Pytest parameterization to execute multiple input variations against the same test function.

The Flask test client sends requests directly to the application without requiring a separately running API server.

## 4. Validation Assertions

The tests validate:

- HTTP response status codes.
- JSON response error messages.
- Correct account ownership.
- Rejection of unauthorized access.
- Absence of sensitive account fields in forbidden responses.

## 5. Expected Outcome

All test scenarios should produce their expected HTTP responses.

A failed assertion indicates that the application behavior differs from the expected result and requires investigation.
