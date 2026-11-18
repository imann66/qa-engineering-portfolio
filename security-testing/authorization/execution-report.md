# Authorization Testing Execution Report

## 1. Execution Summary

| Item                  | Details                          |
| --------------------- | -------------------------------- |
| Project               | QA Engineering Portfolio         |
| Test suite            | Authorization Testing            |
| Application           | Sample Flask API                 |
| Endpoint              | `GET /api/accounts/{account_id}` |
| Test framework        | Pytest 9.2.0                     |
| Python version        | 3.12.6                           |
| Execution environment | Windows                          |
| Execution method      | Flask test client                |
| Execution result      | Passed                           |

## 2. Test Execution Results

| Metric                  |       Result |
| ----------------------- | -----------: |
| Total test cases        |           16 |
| Passed                  |           16 |
| Failed                  |            0 |
| Errors during execution |            0 |
| Pass rate               |         100% |
| Execution time          | 0.63 seconds |

**Overall result:** All 16 authorization test cases passed.

## 3. Coverage Results

| Test Area                            |  Cases | Result     |
| ------------------------------------ | -----: | ---------- |
| Positive authorization               |      2 | Passed     |
| Negative authorization               |      2 | Passed     |
| Authentication validation            |      4 | Passed     |
| Resource existence                   |      1 | Passed     |
| Invalid account ID format            |      3 | Passed     |
| Token case and whitespace validation |      2 | Passed     |
| Negative and zero account IDs        |      2 | Passed     |
| **Total**                            | **16** | **Passed** |

## 4. Key Observations

### Authentication

The application rejected requests containing missing, empty, invalid, and unknown authentication tokens with HTTP 401 responses.

### Authorization

Alice and Bob successfully accessed their respective accounts.

Cross-account access attempts were rejected with HTTP 403 responses.

The tests also confirmed that forbidden responses did not expose the account balance, owner, or account ID.

### Resource and Input Handling

The application returned HTTP 404 responses for nonexistent accounts and invalid account identifiers.

Token capitalization and surrounding whitespace variations were also rejected.

## 5. Defects and Findings

No unexpected behavior was identified during this execution.

All implemented test assertions passed.

This result demonstrates that the tested authentication and authorization controls behaved as expected. It does not establish that the application is free from other security vulnerabilities.

## 6. Execution Evidence

The test suite was executed using:

```powershell
D:\qa-playwright-automation\.venv\Scripts\python.exe -m pytest -v tests/test_authorization.py
```

Working directory:

```text
D:\qa-engineering-portfolio\automation\playwright
```

Pytest summary:

```text
collected 16 items

16 passed in 0.63s
```

The test execution was performed against the application and test files stored in the QA portfolio repository.

## 7. Limitations

- Testing was performed against a local sample application.
- Authentication uses predefined static tokens.
- The API stores account data in memory.
- Only the account retrieval endpoint was tested.
- No external identity provider, database-backed authentication, or production environment was involved.
- The test suite validates implemented scenarios and does not provide comprehensive security assurance.

## 8. Conclusion

The authorization test execution completed successfully with 16 passing test cases and no failures.

The results demonstrate practical application of positive and negative security testing, authentication validation, access-control verification, response validation, and automated testing with Pytest.
