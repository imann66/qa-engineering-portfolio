# Task Management API - Test Cases

## 1. End-to-End CRUD Workflow

| ID           | Test Scenario             | Expected Result                                                  |
| ------------ | ------------------------- | ---------------------------------------------------------------- |
| API-CRUD-001 | Create a task             | HTTP 201; response contains task ID and initial status `pending` |
| API-CRUD-002 | Retrieve the created task | HTTP 200; returned task ID and title match the created task      |
| API-CRUD-003 | Update a task             | HTTP 200; updated title and status are returned                  |
| API-CRUD-004 | Verify updated task       | HTTP 200; updated values persist                                 |
| API-CRUD-005 | Delete a task             | HTTP 200; deletion confirmation is returned                      |
| API-CRUD-006 | Retrieve deleted task     | HTTP 404; task not found error is returned                       |

## 2. Negative and Boundary Testing

| ID          | Test Scenario                              | Expected Result                                  |
| ----------- | ------------------------------------------ | ------------------------------------------------ |
| API-NEG-001 | Create task with empty title               | HTTP 400 and an error message                    |
| API-NEG-002 | Submit a numeric title instead of a string | HTTP 400 and an error message                    |
| API-NEG-003 | Submit a title exceeding maximum length    | HTTP 400 and an error message                    |
| API-NEG-004 | Submit an invalid task status              | API returns the expected `Invalid status.` error |
| API-NEG-005 | Update a nonexistent task                  | HTTP 404 and `Task not found.`                   |
| API-NEG-006 | Delete a nonexistent task                  | HTTP 404 and `Task not found.`                   |
| API-NEG-007 | Submit malformed JSON                      | HTTP 400 and `Request body must be valid JSON.`  |

## 3. Database Testing

| ID         | Test Scenario                            | Validation                                |
| ---------- | ---------------------------------------- | ----------------------------------------- |
| API-DB-001 | Verify API and database data consistency | Compare API response with database record |
| API-DB-002 | Update a task through the API            | Verify updated values in the database     |
| API-DB-003 | Create a task for deletion               | Verify the record is created              |
| API-DB-004 | Delete a task through the API            | Verify the record is removed              |
| API-DB-005 | Submit an invalid PATCH request          | Verify invalid data is not persisted      |

## Notes

The database testing requests are supporting requests for manual database verification. They currently do not contain Postman automated test scripts.
