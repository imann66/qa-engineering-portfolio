# IDOR Test Cases

## 1. Overview

This document describes the scenarios used to demonstrate and verify protection against Insecure Direct Object Reference (IDOR) in the sample Flask API.

**Endpoint:** `GET /api/accounts/{account_id}`

**Test framework:** Pytest

## 2. Historical Vulnerability Demonstration

| Test ID  | Scenario                                                             | Test Data              | Vulnerable Behavior                                         |
| -------- | -------------------------------------------------------------------- | ---------------------- | ----------------------------------------------------------- |
| IDOR-001 | Bob accesses Alice's account after ownership verification is removed | Bob token, account 101 | Account information returned without ownership verification |

During the exercise, the ownership check was temporarily removed. The API returned account information belonging to Alice when the request was made using Bob's token.

This historical demonstration is separate from the current regression execution.

## 3. Remediation and Regression Test Cases

| Test ID  | Scenario                               | Test Data                | Expected Result    |
| -------- | -------------------------------------- | ------------------------ | ------------------ |
| IDOR-002 | Alice attempts to access Bob's account | Alice token, account 202 | HTTP 403 Forbidden |
| IDOR-003 | Bob attempts to access Alice's account | Bob token, account 101   | HTTP 403 Forbidden |

## 4. Security Assertions

The regression tests validate:

- Cross-account requests are rejected.
- The API returns HTTP 403 Forbidden.
- The response contains the expected `Forbidden` error.
- Sensitive fields such as `balance`, `owner`, and `account_id` are not exposed in the forbidden response.

## 5. Test Implementation

The automated regression tests are implemented in:

`automation/playwright/tests/test_authorization.py`

The test function uses Pytest parameterization to verify both directions of unauthorized account access.

## 6. Expected Outcome

Both cross-account access attempts must be rejected with HTTP 403 Forbidden.

A successful HTTP 200 response containing another user's account information would indicate an authorization failure and potential IDOR vulnerability.
