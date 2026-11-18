# Input Validation Test Cases

## Test Environment

- Application: Sample Flask Account API
- Endpoint: `GET /api/accounts/{account_id}`
- Test framework: Pytest
- Test file: `automation/playwright/tests/test_authorization.py`
- Test execution: Flask test client

## Test Cases

| Test ID | Scenario                       | Test Input | Expected HTTP Status | Expected Behavior          |
| ------- | ------------------------------ | ---------- | -------------------- | -------------------------- |
| INP-001 | Request a nonexistent account  | `999`      | 404                  | Return `Account not found` |
| INP-002 | Use an alphabetic account ID   | `abc`      | 404                  | Reject the request         |
| INP-003 | Use an invalid account ID      | `invalid`  | 404                  | Reject the request         |
| INP-004 | Use an alphanumeric account ID | `12abc`    | 404                  | Reject the request         |
| INP-005 | Use a negative account ID      | `-101`     | 404                  | Return `Account not found` |
| INP-006 | Use a zero account ID          | `0`        | 404                  | Return `Account not found` |

## Detailed Test Cases

### INP-001: Nonexistent Account

- **Objective:** Verify that the API handles requests for accounts that do not exist.
- **Input:** Account ID `999`
- **Authentication:** Valid Alice token
- **Expected Result:** HTTP 404 with `Account not found`.

### INP-002: Alphabetic Account ID

- **Objective:** Verify that alphabetic characters are rejected as account identifiers.
- **Input:** Account ID `abc`
- **Authentication:** Valid Alice token
- **Expected Result:** HTTP 404.

### INP-003: Invalid Account ID

- **Objective:** Verify that an unsupported text value is rejected.
- **Input:** Account ID `invalid`
- **Authentication:** Valid Alice token
- **Expected Result:** HTTP 404.

### INP-004: Alphanumeric Account ID

- **Objective:** Verify that mixed numeric and alphabetic characters are rejected.
- **Input:** Account ID `12abc`
- **Authentication:** Valid Alice token
- **Expected Result:** HTTP 404.

### INP-005: Negative Account ID

- **Objective:** Verify that a negative account identifier does not return account data.
- **Input:** Account ID `-101`
- **Authentication:** Valid Alice token
- **Expected Result:** HTTP 404 with `Account not found`.

### INP-006: Zero Account ID

- **Objective:** Verify that zero does not return account data.
- **Input:** Account ID `0`
- **Authentication:** Valid Alice token
- **Expected Result:** HTTP 404 with `Account not found`.

## Test Coverage Notes

- INP-001, INP-005, and INP-006 reach the endpoint and test account resource lookup.
- INP-002, INP-003, and INP-004 are rejected by Flask's integer route converter before the endpoint executes.
- Authentication token format tests are covered separately in the Authorization test cases.
