# Authorization Testing

## 1. Overview

This project demonstrates security testing of authentication and authorization controls in a sample Flask API.

The API provides access to user accounts and implements authentication, resource ownership verification, and access restrictions.

The objective is to verify that authenticated users can access their own accounts while unauthorized users are prevented from accessing other users' information.

## 2. Testing Objectives

- Verify that valid users can access their own accounts.
- Verify that users cannot access accounts belonging to other users.
- Verify that missing and invalid authentication tokens are rejected.
- Verify that unauthorized responses do not expose sensitive account information.
- Verify handling of nonexistent resources.
- Test invalid account identifiers and token formats.

## 3. Application Under Test

| Component            | Description                       |
| -------------------- | --------------------------------- |
| Application          | Sample Flask REST API             |
| Endpoint             | `GET /api/accounts/{account_id}`  |
| Authentication       | Static token-based authentication |
| Test framework       | Pytest                            |
| HTTP client          | Flask test client                 |
| Programming language | Python                            |

### Test accounts

| User  | Account ID | Expected access  |
| ----- | ---------: | ---------------- |
| Alice |        101 | Own account only |
| Bob   |        202 | Own account only |

The application uses predefined accounts and tokens for controlled testing. It is a learning implementation, not a production authentication system.

## 4. Testing Scope

### Authentication testing

- Missing authorization header.
- Empty authorization token.
- Invalid token.
- Unknown user token.
- Case-sensitive token validation.
- Whitespace handling.

### Authorization testing

- User accesses their own account.
- User attempts to access another user's account.
- Unauthorized response does not expose account information.

### Resource and input testing

- Nonexistent account.
- Invalid account ID format.
- Negative account ID.
- Zero account ID.

## 5. Test Results Summary

The authorization test suite collected and executed 16 test cases.

| Result | Count |
| ------ | ----: |
| Passed |    16 |
| Failed |     0 |
| Total  |    16 |

All 16 test cases passed during the recorded execution.

See [Execution Report](execution-report.md) for the detailed results.

## 6. Project Structure

```text
authorization/
├── README.md
├── test-cases.md
└── execution-report.md
```

The application and automated tests are maintained under `automation/playwright/` in this repository.

## 7. Tools and Technologies

- Python 3.12.6
- Flask
- Pytest 9.2.0
- Flask test client
- PowerShell
- Git and GitHub

## 8. Learning Outcomes

This project demonstrates practical experience with:

- Authentication and authorization testing.
- Positive and negative security test scenarios.
- Access-control verification.
- HTTP response validation.
- Sensitive information exposure checks.
- Parameterized testing with Pytest.
- Security test documentation and execution reporting.

## 9. Limitations

- Static tokens are used instead of production authentication mechanisms.
- Account data is stored in application memory.
- Testing focuses on a single account retrieval endpoint.
- No production environment or external identity provider is involved.
- Passing tests do not establish that the application is free from security vulnerabilities.

## 10. Related Documentation

- [Authorization Test Cases](test-cases.md)
- [Authorization Execution Report](execution-report.md)
