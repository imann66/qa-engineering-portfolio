# Database Integration Test Cases

| ID         | Test Scenario                         | Validation Objective                                   |
| ---------- | ------------------------------------- | ------------------------------------------------------ |
| DB-INT-001 | API and database consistency          | Verify API response matches the stored database record |
| DB-INT-002 | Update through API                    | Verify updated data is persisted                       |
| DB-INT-003 | Delete through API                    | Verify the deleted record is no longer present         |
| DB-INT-004 | Invalid API update                    | Verify invalid updates are rejected                    |
| DB-INT-005 | Database NOT NULL constraint          | Verify required fields cannot be null                  |
| DB-INT-006 | Transaction rollback                  | Verify failed operations do not leave partial changes  |
| DB-INT-007 | Data integrity after failed operation | Verify database state remains consistent               |

## Notes

These scenarios summarize the integration testing areas recorded in the previous training exercise. Individual SQL statements and additional execution evidence can be added as the portfolio is expanded.
