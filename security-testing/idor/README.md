# IDOR (Insecure Direct Object Reference) Testing

## 1. Overview

This project demonstrates the identification, exploitation, remediation, and regression testing of an Insecure Direct Object Reference (IDOR) vulnerability in a sample Flask API.

IDOR occurs when an application allows a user to access an object belonging to another user without properly verifying ownership or authorization.

The exercise uses account identifiers to demonstrate how manipulating a resource ID can expose another user's information.

## 2. Testing Objectives

- Understand how IDOR vulnerabilities occur.
- Verify whether account ownership is enforced.
- Demonstrate unauthorized access through account ID manipulation.
- Identify sensitive information exposed through unauthorized requests.
- Apply an ownership validation control.
- Verify the remediation through regression tests.

## 3. Application Under Test

| Component            | Description                       |
| -------------------- | --------------------------------- |
| Application          | Sample Flask REST API             |
| Endpoint             | `GET /api/accounts/{account_id}`  |
| Authentication       | Static token-based authentication |
| Authorization        | Account ownership verification    |
| Test framework       | Pytest                            |
| HTTP client          | Flask test client                 |
| Programming language | Python                            |

## 4. Vulnerability Demonstration

During the learning exercise, the account ownership verification was temporarily removed from the endpoint.

An authenticated user could then request another user's account by changing the account ID.

Example:

```http
GET /api/accounts/101
Authorization: bob-token
```

Account `101` belongs to Alice, but the request was made using Bob's token.

The vulnerable implementation returned account information instead of rejecting the request.

This demonstrated an IDOR vulnerability and unauthorized exposure of account information.

## 5. Remediation

The ownership verification was restored:

```python
if account["owner"] != username:
    return jsonify({
        "error": "Forbidden"
    }), 403
```

The application now checks whether the authenticated user owns the requested account before returning its information.

## 6. Regression Testing

The current implementation is tested in both directions:

- Alice attempts to access Bob's account.
- Bob attempts to access Alice's account.

Both requests are expected to return HTTP 403 Forbidden.

The current focused regression execution completed with two passing test cases.

See [Test Cases](test-cases.md) and [Execution Report](execution-report.md).

## 7. Tools and Technologies

- Python 3.12.6
- Flask
- Pytest 9.2.0
- Flask test client
- PowerShell
- Git and GitHub

## 8. Learning Outcomes

This exercise demonstrates practical understanding of:

- Insecure Direct Object Reference (IDOR).
- Broken object-level authorization.
- Account ownership verification.
- Unauthorized data exposure.
- Security remediation.
- Regression testing.

## 9. Limitations

- The exercise uses a local sample application.
- Authentication relies on predefined static tokens.
- Account data is stored in application memory.
- Testing is limited to a single account retrieval endpoint.
- The historical vulnerable implementation is documented as a learning exercise; the current application contains the ownership check.

## 10. Related Documentation

- [IDOR Test Cases](test-cases.md)
- [IDOR Execution Report](execution-report.md)
