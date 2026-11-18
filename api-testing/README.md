# API Testing

## Overview

This section contains API testing activities performed as part of my QA Engineering learning and portfolio development.

The objective is to validate API functionality, request and response behavior, input validation, error handling, and consistency between the API and its underlying database.

## Testing Areas

### 1. Postman API Testing

API testing using Postman to validate:

- HTTP methods and status codes
- Request payloads
- Response structure and data
- CRUD operations
- Negative and boundary scenarios
- Automated assertions using Postman test scripts

### 2. Database Validation

Integration testing between the API and PostgreSQL database.

Validation includes:

- API and database data consistency
- Persistence of updated records
- Record deletion
- Invalid data handling
- Database constraints
- Transaction rollback and data integrity

## Project Structure

```text
api-testing/
├── README.md
├── postman/
│   ├── task-management-api/
│   └── user-api/
└── database-validation/
```

## Tools and Technologies

- Postman
- REST API
- HTTP
- JSON
- Python
- PostgreSQL
- SQL

## Documentation and Evidence

Each testing project contains its own test cases, execution report, and supporting collection or evidence where applicable.

Execution results are documented separately from test design to distinguish planned coverage from tests that have actually been executed.
