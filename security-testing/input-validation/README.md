# Input Validation Testing

## Overview

This section documents input validation testing performed against the sample Flask API in the QA Engineering Portfolio.

The objective is to verify how the API handles invalid, malformed, and unsupported account identifiers.

## Application Under Test

- **Application:** Sample Flask Account API
- **Framework:** Flask
- **Endpoint:** `GET /api/accounts/{account_id}`
- **Route parameter:** `account_id`
- **Authentication:** Static token-based authentication
- **Test framework:** Pytest
- **Test file:** `automation/playwright/tests/test_authorization.py`

## Testing Objectives

The tests focus on verifying that the API:

- Rejects account identifiers containing non-numeric characters.
- Handles requests for nonexistent accounts correctly.
- Handles zero and negative account identifiers.
- Does not return account information when the requested resource does not exist.

## Test Scenarios

| Test ID | Scenario                                 | Expected Result |
| ------- | ---------------------------------------- | --------------- |
| INP-001 | Request a nonexistent account (`999`)    | HTTP 404        |
| INP-002 | Use an alphabetic account ID (`abc`)     | HTTP 404        |
| INP-003 | Use an invalid account ID (`invalid`)    | HTTP 404        |
| INP-004 | Use an alphanumeric account ID (`12abc`) | HTTP 404        |
| INP-005 | Use a negative account ID (`-101`)       | HTTP 404        |
| INP-006 | Use a zero account ID (`0`)              | HTTP 404        |

## Implementation Notes

The API uses Flask's integer route converter:

`/api/accounts/<int:account_id>`

This converter prevents non-integer path values from reaching the endpoint function. Such requests receive HTTP 404.

Negative and zero values can pass the integer route converter, but they do not match an existing account in the application's account data. The API therefore returns HTTP 404 when the resource lookup fails.

These tests verify the current application's behavior. They do not demonstrate comprehensive input validation or protection against every form of malformed input.

## Related Testing

Authentication token input checks, including incorrect casing and leading or trailing whitespace, are documented in:

- [Authorization Testing](../authorization/README.md)

Cross-account access and IDOR regression tests are documented in:

- [IDOR Testing](../idor/README.md)

## Tools and Technologies

- Python
- Flask
- Pytest
- Flask test client
- PowerShell

## Limitations

- The application uses in-memory sample account data.
- Testing is performed through Flask's test client, not a deployed production API.
- The current implementation relies on Flask's integer route converter and resource lookup.
- HTTP 404 responses do not establish that all input validation requirements are satisfied.
- These tests do not constitute a comprehensive security assessment.

## Learning Outcomes

This exercise demonstrates how to:

- Identify input validation boundaries in an API.
- Test malformed and unsupported path parameters.
- Verify behavior for nonexistent resources.
- Distinguish route parameter conversion from application-level validation.
- Document expected API responses using repeatable automated tests.
