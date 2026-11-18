# IDOR Testing Execution Report

## 1. Execution Summary

| Item                  | Details                          |
| --------------------- | -------------------------------- |
| Project               | QA Engineering Portfolio         |
| Test suite            | IDOR Regression Testing          |
| Application           | Sample Flask API                 |
| Endpoint              | `GET /api/accounts/{account_id}` |
| Test framework        | Pytest 9.2.0                     |
| Python version        | 3.12.6                           |
| Execution environment | Windows                          |
| Execution method      | Flask test client                |

## 2. Historical Vulnerability Demonstration

During the earlier learning exercise, account ownership verification was temporarily removed from the API endpoint.

A request using Bob's token to access Alice's account returned account information without checking ownership.

This demonstrated an IDOR vulnerability.

The ownership verification was subsequently restored.

The historical vulnerable implementation was not reintroduced during the current regression execution.

## 3. Current Regression Execution Results

| Metric                     |       Result |
| -------------------------- | -----------: |
| Selected test cases        |            2 |
| Passed                     |            2 |
| Failed                     |            0 |
| Deselected from full suite |           14 |
| Execution time             | 0.54 seconds |
| Pass rate                  |         100% |

**Overall result:** Both IDOR regression test cases passed.

## 4. Regression Coverage

| Scenario                     | Expected Result | Actual Result |
| ---------------------------- | --------------- | ------------- |
| Alice accesses Bob's account | HTTP 403        | Passed        |
| Bob accesses Alice's account | HTTP 403        | Passed        |

The tests also verified that forbidden responses did not expose account balance, owner, or account ID fields.

## 5. Execution Evidence

The focused test execution used:

```powershell
D:\qa-playwright-automation\.venv\Scripts\python.exe -m pytest -v tests/test_authorization.py -k "other_users_account"
```

Working directory:

```text
D:\qa-engineering-portfolio\automation\playwright
```

Pytest summary:

```text
collected 16 items / 14 deselected / 2 selected

2 passed, 14 deselected in 0.54s
```

## 6. Findings

The historical learning exercise demonstrated an IDOR vulnerability when ownership verification was removed.

After remediation, both current cross-account regression tests passed.

No IDOR-related regression failure was observed during the recorded execution.

## 7. Limitations

- The current regression tests validate only the account retrieval endpoint.
- The historical vulnerable implementation was not re-executed during this test run.
- The application uses static tokens and in-memory account data.
- Passing regression tests do not establish that other endpoints or object types are protected against IDOR.

## 8. Conclusion

The learning exercise demonstrated how missing object ownership verification can result in unauthorized account access.

The ownership check was restored, and both cross-account regression tests passed.

This demonstrates the importance of object-level authorization checks and regression testing after security remediation.
