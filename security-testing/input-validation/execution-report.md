# Input Validation Execution Report

## Execution Summary

| Item                 | Details                  |
| -------------------- | ------------------------ |
| Application          | Sample Flask Account API |
| Test Area            | Input Validation         |
| Test Framework       | Pytest                   |
| Python Version       | 3.12.6                   |
| Pytest Version       | 9.2.0                    |
| Operating System     | Windows                  |
| Execution Method     | Flask test client        |
| Total Selected Tests | 6                        |
| Passed               | 6                        |
| Failed               | 0                        |
| Errors               | 0                        |
| Deselected           | 10                       |
| Execution Time       | 0.35 seconds             |
| Overall Result       | PASS                     |

## Test Execution

The input validation scenarios were executed from:

`D:\qa-engineering-portfolio\automation\playwright`

Command:

```powershell
D:\qa-playwright-automation\.venv\Scripts\python.exe -m pytest -v tests/test_authorization.py -k "nonexistent_account or invalid_account_id_format or negative_and_zero_account_id"
```

## Execution Results

| Test ID | Scenario                          | Actual Result | Status |
| ------- | --------------------------------- | ------------- | ------ |
| INP-001 | Nonexistent account (`999`)       | HTTP 404      | PASS   |
| INP-002 | Alphabetic account ID (`abc`)     | HTTP 404      | PASS   |
| INP-003 | Invalid account ID (`invalid`)    | HTTP 404      | PASS   |
| INP-004 | Alphanumeric account ID (`12abc`) | HTTP 404      | PASS   |
| INP-005 | Negative account ID (`-101`)      | HTTP 404      | PASS   |
| INP-006 | Zero account ID (`0`)             | HTTP 404      | PASS   |

## Execution Outcome

All six selected input validation scenarios passed.

The API returned the expected HTTP 404 response for each tested account identifier.

The observed behavior differs depending on the input:

- Non-integer values were rejected by Flask's integer route converter before reaching the endpoint.
- Nonexistent, negative, and zero account IDs reached the endpoint but did not match an existing account.
- No account information was returned for these requests.

## Related Regression Coverage

The six selected tests are part of the broader authorization test module.

The complete authorization test module was also executed separately:

- 16 tests passed.
- 0 failed.
- Execution time: 0.63 seconds.

The six input validation tests are included within those 16 tests. These results must not be added together as separate test totals.

Authentication token format checks are covered by the authorization tests, not included in the six-test input validation execution above.

## Limitations

- This execution used Flask's test client rather than a deployed API.
- The test cases cover a limited set of account identifier inputs.
- HTTP 404 is the expected behavior of this implementation, not proof of comprehensive input validation.
- No database-backed validation or broader fuzz testing was performed.
- Passing tests demonstrate expected behavior for the tested cases only.

## Conclusion

The tested account identifier scenarios behaved as expected.

The results provide repeatable evidence of basic route parameter handling and resource lookup behavior in the sample Flask API. Further validation would be needed to assess broader input validation requirements.
