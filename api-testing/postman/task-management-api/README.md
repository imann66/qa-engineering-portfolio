# Task Management API Testing

## Overview

This project contains API tests for a Task Management API.

The objective is to validate the task lifecycle, input validation, error handling, and API behavior when interacting with task resources.

## Test Scope

### End-to-End CRUD Workflow

Validate the complete task lifecycle:

1. Create a task.
2. Retrieve the created task.
3. Update the task.
4. Verify the updated data.
5. Delete the task.
6. Verify that the deleted task can no longer be retrieved.

### Negative and Boundary Testing

Validate how the API handles:

- Empty task titles
- Incorrect title data types
- Titles exceeding the maximum length
- Invalid task statuses
- Updates to nonexistent tasks
- Deletion of nonexistent tasks
- Malformed JSON request bodies

### Database Testing

Validate API and database behavior, including:

- API and database data consistency
- Persistence of updated records
- Record deletion
- Rejection of invalid updates

## Tools

- Postman
- REST API
- HTTP
- JSON
- PostgreSQL

## Collection

The Postman collection is maintained in this directory.

Collection variables:

| Variable  | Purpose                                     |
| --------- | ------------------------------------------- |
| `baseUrl` | Base URL of the Task Management API         |
| `taskId`  | Dynamically stores the ID of a created task |

Set `baseUrl` in Postman before executing the requests.

## Execution

Refer to `execution-report.md` for execution status and results.

Refer to `test-cases.md` for the test coverage.
